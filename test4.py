import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6497653856:AAHqt39YeEOdlFGptYijL-xIPd5YMFxkJYY')

# Dictionary to store user-provided names and temporary descriptions
user_data = {}

# Step 1: Capture the user's input for the name
@bot.message_handler(commands=['start', 'setname'])
def set_name(message):
    bot.send_message(message.chat.id, "Please send the name you want to use as the caption.")
    bot.register_next_step_handler(message, save_name)

def save_name(message):
    user_id = message.from_user.id
    user_data[user_id] = {"name": message.text, "description": ""}
    bot.send_message(message.chat.id, f"Name '{message.text}' saved! Now, send an audio file.")

# Step 2: Handle audio file and ask if the user wants to add a description
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    user_id = message.from_user.id

    # Check if the user has set a name
    if user_id not in user_data or not user_data[user_id].get("name"):
        bot.send_message(message.chat.id, "Please set a name first using /setname.")
        return

    # Store the audio file_id for later use
    user_data[user_id]["audio_file_id"] = message.audio.file_id

    # Ask the user if they want to add a description
    bot.send_message(message.chat.id, "Would you like to add a description for this song? If yes, please type it. If not, type 'no'.")
    bot.register_next_step_handler(message, handle_description)

def handle_description(message):
    user_id = message.from_user.id
    if message.text.lower() != 'no':
        # Save the description provided by the user
        user_data[user_id]["description"] = message.text
    else:
        user_data[user_id]["description"] = ""

    # Send the audio with the new caption
    send_audio_with_caption(user_id, message.chat.id)

def send_audio_with_caption(user_id, chat_id):
    # Retrieve the user's name, description, and audio file_id
    name = user_data[user_id]["name"]
    description = user_data[user_id]["description"]
    audio_file_id = user_data[user_id]["audio_file_id"]

    # Formulate the caption
    caption = f"\'{name}\'"
    if description:
        caption += f" \n{description}"
    caption += "\n@me_beingnerd"

    # Re-send the audio using the file_id with the new caption
    bot.send_audio(
        chat_id=chat_id,
        audio=audio_file_id,
        caption=caption
    )

    # Clear the description for the next song
    user_data[user_id]["description"] = ""

# Start polling
bot.polling()

# Telegram Channel Ban Bot

This is a Telegram bot that helps channel administrators ban and unban members. This bot is written in Python and uses the `python-telegram-bot` library.

## Features

- Ban members from the channel
- Unban banned members from the channel
- Usage restricted to administrators only
- Ability to ban/unban by username or user ID
- Logging functionality to track all ban and unban actions
- Error handling for invalid user inputs
- Support for multiple administrators

## Requirements

- Python 3.6 or higher
- `python-telegram-bot` library

## Installation

1. First, install the required library:

pip install python-telegram-bot --upgrade

2. Clone the repository or download the code:

git clone https://github.com/yourusername/telegram-channel-ban-bot.git
cd telegram-channel-ban-bot

## Usage Instructions

1. Get a Bot Token:
- Search for `@BotFather` on Telegram
- Create a new bot using the `/newbot` command
- You will receive a token after creating the bot

2. Find your User ID:
- Go to the `@userinfobot` and send the `/start` command
- Copy your User ID

3. Configure the code:
- Open the `channel_ban_bot.py` file
- Replace `TOKEN = "YOUR_BOT_TOKEN_HERE"` with your bot token
- Add your Telegram User ID(s) to the `ADMIN_IDS = [123456789, 987654321]` line

4. Run the bot:

python channel_ban_bot.py

5. Add the bot to your Telegram channel and grant it administrator privileges

## Commands

- `/start` - Used to start the bot
- `/ban @username` - Ban a user with the specified username
- `/ban user_id` - Ban a user with the specified user ID
- `/unban @username` - Unban a user with the specified username
- `/unban user_id` - Unban a user with the specified user ID
- `/help` - Show all available commands and their usage

## Important Information

- This bot only works for Telegram channels, it will not work on WhatsApp
- You must be a channel administrator to use this bot
- If any other user tries to ban/unban, they will be notified that they don't have permission
- Make sure the bot has appropriate admin permissions in the channel to ban/unban members

## Troubleshooting

- If the bot doesn't respond to commands, check if it's running and has proper internet connection
- Make sure you've correctly configured the bot token and admin IDs
- Verify that the bot has been added to the channel with admin permissions

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## Author

Created by [Arup Halder](https://github.com/yourusername)

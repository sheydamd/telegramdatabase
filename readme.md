# Telegram User Registration Bot

This project is a simple Telegram Bot built with python-telegram-bot that registers users in a SQLite database when they use the /start command.

It also supports basic commands and message responses.

The bot is designed as a beginner-friendly example of:
- Telegram bot development
- Asynchronous handlers
- SQLite database usage
- User data persistence
 _______________________________________________________________
## Features
1. Registers users on /start
2. Stores user data in SQLite
3. Prevents duplicate user entries
4. Simple text responses (hi, bye, echo)
5. Saves registration timestamp
6. Logging enabled for debugging
________________________________________________________________

### Database Structure
The bot automatically creates a SQLite database file named databasetel.db with the following table:
```sql
users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    first_name TEXT,
    username TEXT,
    start_time TEXT
)
```
_________________________________________________________________
### How It Works
- /start Command

Checks if the user already exists in the database
If yes : sends a welcome back message

If no : saves user information and confirms registration

- /help Command

Sends a simple help message

- Text Messages

hi : replies with hello

bye : replies with bye

Any other text : echoes the same message
___________________________________________________________________
### Installation
install bot Library by: pip install python-telegram-bot
___________________________________________________________________
### How to Run
Replace the bot token with your own Telegram Bot Token
Run the script:

python bot.py
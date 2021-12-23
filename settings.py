import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "&&"

# The bot token. Keep this secret!
BOT_TOKEN = "ODk0ODM2MDE0MTM1MjU5MTM4.YVvy-w.u3IRCecxtR-XQRPYIltd46MjYGQ"

# Message to display when joining server
WELCOME = "Hello! My prefix is"

# The now playing game. Set this to anything false-y ("", None) to disable it
NP_STATUS = COMMAND_PREFIX + "commands"
#Set the RPC mode. Available options: GAME, LISTEN, STREAM, WATCH
NP_MODE = "GAME"
#URL for STREAM mode, Twitch only. (for other mode leave this setting as blank)
NP_URL = ""

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

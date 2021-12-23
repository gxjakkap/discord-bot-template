

# Discord bot template
This is a fork of [discord-bot-template](https://github.com/agubelu/discord-bot-template) which has been migrated to [nextcord](https://github.com/nextcord/nextcord) instead of discord.py . Also included some minor improvement.

Check [example_command.py](https://github.com/gxjakkap/discord-bot-template/blob/master/commands/example_command.py) and [example_event.py](https://github.com/gxjakkap/discord-bot-template/blob/master/events/example_event.py) for an example on how to implement commands and events, or keep reading for more detailed info.

## Pre-requisites
- Python >= 3.8 (required by [nextcord](https://github.com/nextcord/nextcord#:~:text=Python%203.8%20or%20higher%20is%20required))
- You need to [register your bot and get a Discord API token](https://discordapp.com/developers/applications/me).
- You should be at least familiar with Python 3 and with the basics of the [nextcord](https://github.com/nextcord/nextcord) [(docs)](https://nextcord.readthedocs.io/en/latest/) library.
- You should also have some basic knowledge about what asynchronous programming is and [how it works in Python](https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/), but to be fairly honest you don't really have to in order to make this thing work. You can just throw in `async` or `await` whenever Python complains.
- You should know what a `virtualenv` is and how to set up one. Check [this](http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv) out if the file name `requirements.txt` doesn't speak to you.

## Installation

1. Set up virtualenv

  Check out how to [here](https://docs.python.org/3/library/venv.html).

2. Install All required dependencies

  `pip3 install -r requirements.txt`

3. Fill out settings-example.py and rename it to settings.py

4. Run bot.py

  Linux: `python3 bot.py`

  Windows: `python -3 bot.py`

## More Info

Check out info [here](https://github.com/gxjakkap/discord-bot-template/blob/master/Info.md).

## License
[GPL-3.0](https://github.com/gxjakkap/discord-bot-template/blob/master/LICENSE)

# Discord World Time Bot

This is a small discord bot, that display the time in different timezones.

## Installation

Please clone the repository and navigate to the working directory and build the Docker container.

```bash
docker build -t dicord-world-time-bot .
```

After the operation you can start the bot, you need to change your token.

```bash
docker run --detach -e "token=[Your Token]" --name dicord-bot-worldtime dicord-world-time-bot
```
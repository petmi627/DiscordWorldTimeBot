import discord, datetime, pytz, random, logging, sys, os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class WorldTimeClient(discord.Client):

    greetings = ["I'm one with the time so here is your list", "as requested here is the time list",
                 "my only purpose in this world is to suffer, so I need to do this",
                 "does gravity bend time and space in the 4th dimension",
                 "neicht geht iwwert e gudden Kachkeis an keen versteht mech",
                 "ich hab die Patente 1, 2 ,3 und die 6. Ich fahr die großen Pödde.",
                 "the Earth has different timezones because it is round!",
                 "need an ambulance? Call CGDIS!", "177013 is great!",
                 "my Master would you like something to eat, a bath or would you like to get the time"
                 ]

    async def on_ready(self):
        logger.info("I started up. Beep Bop")

    async def on_message(self, message):
        if message.author == client.user:
            return

        if "help" in message.content and client.user in message.mentions:
            logger.info("Message from " + str(message.author) + " contains " + message.content)
            await message.channel.send('Type $time or $timezones to view the time in different timezones')

        if message.content in ["$time", '$timezones']:
            logger.info("Message from " + str(message.author) + " contains " + message.content)
            now_utc = datetime.datetime.now(tz=pytz.utc)
            now_luxembourg = now_utc.astimezone(pytz.timezone('Europe/Luxembourg'))
            now_new_york = now_utc.astimezone(pytz.timezone('America/New_york'))
            now_los_angeles = now_utc.astimezone(pytz.timezone('America/Los_angeles'))
            now_chongqing = now_utc.astimezone(pytz.timezone('Asia/Chongqing'))
            now_melbourne = now_utc.astimezone(pytz.timezone('Australia/Melbourne'))

            msg  = "Hi {}, {}\n\n{} or {}\n{} or {}\n{} or {}\n{} or {}\n{} or {}\n{} or {}".format(message.author.mention, random.choice(self.greetings),
                       datetime.datetime.strftime(now_utc, "%H:%M"), datetime.datetime.strftime(now_utc, "%I:%M %p %Z%z: Universal Time"),
                       datetime.datetime.strftime(now_luxembourg, "%H:%M"), datetime.datetime.strftime(now_luxembourg, "%I:%M %p %Z%z: Central European Standard Time"),
                       datetime.datetime.strftime(now_new_york, "%H:%M"), datetime.datetime.strftime(now_new_york, "%I:%M %p %Z%z: Eastern Time, America East Coast"),
                       datetime.datetime.strftime(now_los_angeles, "%H:%M"), datetime.datetime.strftime(now_los_angeles, "%I:%M %p %Z%z: Pacific Time: America West Coast"),
                       datetime.datetime.strftime(now_melbourne, "%H:%M"), datetime.datetime.strftime(now_melbourne, "%I:%M %p %Z%z: Australian Eastern Standard Time"),
                       datetime.datetime.strftime(now_chongqing, "%H:%M"), datetime.datetime.strftime(now_chongqing, "%I:%M %p %Z%z: Asia China East Coast")
                       )
            await message.channel.send(msg)


if '__main__' == __name__:
    client = WorldTimeClient()
    client.run(os.environ['token'])
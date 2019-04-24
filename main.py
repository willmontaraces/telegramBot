from telegram.ext import Updater, CommandHandler
import tweepy

version = "Twitter piper v0.2"

import DataStoringModule

auth = DataStoringModule.Auth();
auth.process()



def handleTweet(text):
    if text.startswith("RT") or text.startswith("@"):
        return False
    botTe.broadcastMSG(text)


class twitterBot:

    def __init__(self):

        class MyStreamListener(tweepy.StreamListener):
            def on_status(self, status):
                print(status.text)
                handleTweet(status.text)

            def on_error(self, status_code):
                if status_code == 420:
                    return False
                else:
                    print(status_code)

            def on_exception(self, exception):
                print(exception)
                from threading import Timer
                Timer(30.0, twitterBot).start()

        twitterAuth = tweepy.OAuthHandler(auth.twitterAPIKey, auth.twitterAPISecretKey)
        twitterAuth.set_access_token(auth.twitterAccessToken, auth.twitterAccessTokenSecret)

        api = tweepy.API(twitterAuth)
        myStreamListener = MyStreamListener()
        self.myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        print(auth.twitterFollows)
        self.myStream.filter(follow=auth.twitterFollows, is_async=True)


class telegramBot:

    def __init__(self):
        print(auth.telegramUsers)
        self.updater = Updater(auth.telegram)
        self.botito = self.updater.bot;

        def start(bot, update):
            chid = update.message.chat_id
            auth.addTelegramUser(chid)
            bot.send_message(chat_id=chid, text="Hi, welcome to " + version)

        def echoAll(bot, update):
            self.broadcastMSG("" + update.message.from_user.first_name + " " +
                                                    update.message.from_user.last_name + " said hi")

        def wol(bot, update):
            import subprocess
            try:
                subprocess.call("./wol.sh", shell=True)
                bot.send_message(chat_id=update.message.chat_id, text="Wol successfully initiated")
            except:
                #shuould never enter here
                import sys
                bot.send_message(chat_id=update.message.chat_id, text="Wol failed" + sys.exc_info()[0])

        dispatcher = self.updater.dispatcher
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        echoAll_handler = CommandHandler('echoAll', echoAll)
        dispatcher.add_handler(echoAll_handler)

        wol_handler = CommandHandler('wol', wol)
        dispatcher.add_handler(wol_handler)

        self.updater.start_polling()

    def broadcastMSG(self, msg):
        for temp in auth.telegramUsers:
            self.botito.send_message(chat_id=temp, text=msg)


botTe = telegramBot()


auth.deleteFollow("32771325")
# follow number twitter for debugging purposes
# auth.addFollow("32771325")

# follow liinex
auth.addFollow("305539696")
# follow forocoches admin
auth.addFollow("39278447")

botTw = twitterBot()












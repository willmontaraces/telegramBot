from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

version = "ArduinoPasarela"

import DataStoringModule
import AccesoArduino

auth = DataStoringModule.Auth();
auth.process()


class telegramBot:
    def __init__(self):
        print(auth.telegramUsers)
        self.updater = Updater(auth.telegram)
        self.botito = self.updater.bot

        def start(update: Update, context : CallbackContext) -> None:
            chid = update.message.chat_id
            auth.addTelegramUser(chid)
            update.message.reply_text("Hi, welcome to " + version)

        def echoAll(update: Update, context : CallbackContext) -> None:
            self.broadcastMSG("" + update.message.from_user.first_name + " " +
                                                    update.message.from_user.last_name + " said hi")

        def arduino(update: Update, context : CallbackContext) -> None:
            AccesoArduino.enviarOrdenArduino(update.message.text)
            update.message.reply_text("Orden " +  update.message.text + " enviada")

        def wol(update: Update, context : CallbackContext) -> None:
            import subprocess
            try:
                subprocess.call("./wol.sh", shell=True)
                self.updater.bot.send_message(chat_id=update.message.chat_id, text="Wol successfully initiated")
            except:
                #shuould never enter here
                import sys
                self.updater.bot.send_message(chat_id=update.message.chat_id, text="Wol failed" + sys.exc_info()[0])

        dispatcher = self.updater.dispatcher
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        echoAll_handler = CommandHandler('echoAll', echoAll)
        dispatcher.add_handler(echoAll_handler)

        wol_handler = CommandHandler('wol', wol)
        dispatcher.add_handler(wol_handler)

        arduino_handler = CommandHandler('arduino', arduino)
        dispatcher.add_handler(arduino_handler)

        self.updater.start_polling()

    def broadcastMSG(self, msg):
        for temp in auth.telegramUsers:
            self.botito.send_message(chat_id=temp, text=msg)


botTe = telegramBot()












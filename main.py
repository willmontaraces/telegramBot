from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

version = "ArduinoPasarela"
btName = "WoLBT"

import DataStoringModule
import AccesoArduino
import bt

auth = DataStoringModule.Auth();
auth.process()

def stripHeader(input):
    output = input.split(" ")
    if len(output) > 1:
        output = output[1:]
    else:
        output = ""
    return output

class telegramBot:
    def __init__(self):
        print(auth.telegramUsers)
        self.updater = Updater(auth.telegram)
        self.botito = self.updater.bot
        try:
            bt.connect(btName)
        except:
            print("Could not connect to BT")

        def start(update: Update, context : CallbackContext) -> None:
            chid = update.message.chat_id
            auth.addTelegramUser(chid)
            update.message.reply_text("Hi, welcome to " + version)

        def echoAll(update: Update, context : CallbackContext) -> None:
            self.broadcastMSG("" + update.message.from_user.first_name + " " +
                                                    update.message.from_user.last_name + " said hi")

        def arduino(update: Update, context : CallbackContext) -> None:
            mensaje = update.message.text
            respuesta = AccesoArduino.enviarOrdenArduino(stripHeader(mensaje))
            update.message.reply_text("Orden " + update.message.text + " enviada \n" + respuesta)

        def wol(update: Update, context : CallbackContext) -> None:
            respuesta = bt.sendMsg("WOL")
            update.message.reply_text(respuesta)

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












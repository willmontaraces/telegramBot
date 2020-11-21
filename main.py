from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

version = "ArduinoPasarela"
btName = "WoLBT"

import DataStoringModule
import AccesoArduino
import bt
import http_server

auth = DataStoringModule.Auth()
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

        #authentication needed to start interfacing with the ESP
        def start(update: Update, context : CallbackContext) -> None:
            chid = update.message.chat_id
            auth.addTelegramUser(chid)
            update.message.reply_text("Hi, welcome to " + version)

        #If connected to wifi to an arduino will send the attached command to the ESP by wifi
        def arduino(update: Update, context : CallbackContext) -> None:
            mensaje = update.message.text
            respuesta = AccesoArduino.enviarOrdenArduino(stripHeader(mensaje))
            update.message.reply_text("Orden " + update.message.text + " enviada \n" + respuesta)

        #Will trigger the relay as a button
        def wol(update: Update, context : CallbackContext) -> None:
            respuestaBT = bt.sendMsg("W")
            if(respuestaBT == "O"):
                respuestaTelegram = "Done"
            else:
                respuestaTelegram = "Error"
            update.message.reply_text(respuestaTelegram)

        dispatcher = self.updater.dispatcher
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        wol_handler = CommandHandler('wol', wol)
        dispatcher.add_handler(wol_handler)

        arduino_handler = CommandHandler('arduino', arduino)
        dispatcher.add_handler(arduino_handler)

        self.updater.start_polling()

http_server.run()
botTe = telegramBot()












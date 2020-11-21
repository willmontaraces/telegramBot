import sys
import socket
import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

#Currently only works once, if connection is dropped bt module stops working
#TODO fix persistence
def connect(target_name):
#    target_name = "WoLBT"
    target_address=None

    nearby_devices = bluetooth.discover_devices(lookup_names=True)

    for address, name in nearby_devices:
        if target_name == name:
            target_address = address
            break

    if target_address is not None:
        print("found target bluetooth device with address "+ target_address)
    else:
        print("could not find target bluetooth device nearby")

    sock.connect((target_address, 0x0001))

#Currently not working, so no fault tolerance
def disconnect():
    sock.close()

#Sends msg to the bt slave, this message should be one character long
#The response will also be one character long
def sendMsg(message):
    sock.send(message)
    rawResponse = sock.recv(1024)
#    rawResponse += sock.recv(1024)
    if not rawResponse:
        return "Error"
    else:
        return repr(rawResponse)[2:-1]



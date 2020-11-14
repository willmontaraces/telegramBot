import sys
import socket
import bluetooth

target_name = "WoLBT"
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

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, 0x0001))

while True:
    data = input()
    if not data:
        break
    sock.send(data)
    data = sock.recv(1024)
    print("Data received:", str(data))

sock.close()

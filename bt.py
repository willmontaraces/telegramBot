import sys
import socket
import bluetooth

target_name = "WoLBT"
target_address=None

nearby_devices = bluetooth.discover_devices(lookup_names=True)

for bt in nearby_devices:
    if target_name == bt.name:
        target_address = bt.address
        break

if target_address is not None:
    print("found target bluetooth device with address "+ target_address)
else:
    print("could not find target bluetooth device nearby")

sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
sock.connect((target_address, 0x1001))

while True:
    data = input()
    if not data:
        break
    sock.send(data)
    data = sock.recv(1024)
    print("Data received:", str(data))

sock.close()

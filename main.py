from os import *
from requests import *
from threading import Thread
from pyautogui import *
from sys import exit
sys.stderr.write("\x1b[2J\x1b[H")
message = get('https://usefull-api.herokuapp.com/show').json()["message"]
def send(message):
	username = popen("pwd").read().split('/')[2]
	try:
		get(f'https://usefull-api.herokuapp.com/save/{username}/{message.replace("/", "")}')
	except AttributeError:
		exit()
def recieve():
	global message
	while True:
		request = get('https://usefull-api.herokuapp.com/show')
		content = request.json()
		if content["message"] != message:
			message = content["message"]
			print(content['time'], ": ", content['author'], ": ", content['message'])
			system(f"notify '{content['author']}' '{content['message']}'")
		else:
			pass
def startchat():
	while True:
		message = prompt(text='enter a text:', title='NCP' , default='')
		send(message)
if __name__ == '__main__':
    Thread(target = startchat).start()
    Thread(target = recieve).start()

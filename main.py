import sys, argparse, time, re, os, json
import requests
from pync import Notifier

root = "https://www.codechef.com/api/rankings/"

# The notifier function
def notify(contName, notif):
	for msg in notif:
		Notifier.notify(msg['user_handle'] + " solved " + msg['problem'] + " with score " + str(msg['score']), title="Codechef "+contName+" Rank", group=os.getpid(), open="https://www.codechef.com/"+contName, appIcon="logo.png")

def onlyInstitute(param, instiName):
	notif = []

	url = root + param + instiName
	req = requests.get(url)
	print req.status_code

	if(req.status_code != 200):
		raise Exception('Cannot connect Code Chef\'s server')
	else:
		data = req.json()['list']

		if not os.path.isfile('instiLog.json'):
			file = open('instiLog.json', 'w')
			file.write(json.dumps(data))
		else:
			file = open('instiLog.json', 'r')
			prevData = json.loads(file.read())
			file = open('instiLog.json', 'w')
			file.write(json.dumps(data))

			for user in data:
				found = False
				prevUser = {}
				for iterateUser in prevData:
					if iterateUser['user_handle'] == user['user_handle']:
						found = True
						prevUser = iterateUser

				if not found:
					print "Cannot find "+ user['user_handle']
				else:

					if user['score'] != prevUser['score']:
						for prob in user['problems_status']:
							if not prevUser['problems_status'].has_key(prob):
								notif.append({ 'user_handle': user['user_handle'], 'problem': prob, 'score': user['problems_status'][prob]['score'] })
	print notif
	return notif



parser = argparse.ArgumentParser()

parser.add_argument('-c', '--contest', action="store_true")
parser.add_argument('contName', type=str)
parser.add_argument('-i', '--institute', action="store_true")
parser.add_argument('instiName', type=str)
parser.add_argument('-u', '--user', action="store_true")
args = parser.parse_args()

if not Notifier.is_available():
	print "Upgrade your system to OS X10.8+"
	quit()

try:
	if args.contName == None or args.contName == "":
		raise Exception('Mention contest name.')
	else:
		root = root + args.contName
except ValueError as e:
	print e

try:
	while True:
		if args.institute:
			instiName = re.sub(' ', '%20', args.instiName)
			param = "?filterBy=Institution%3D"
			notifs = onlyInstitute(param, instiName)

			if len(notifs) != 0:
				notify(args.contName, notifs)
			time.sleep(3)
except ValueError as e:
	print e

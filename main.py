import sys, argparse, time, re, os, json
import requests

root = "https://www.codechef.com/api/rankings/"

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



parser = argparse.ArgumentParser()

parser.add_argument('-c', '--contest', action="store_true")
parser.add_argument('contName', type=str)
parser.add_argument('-i', '--institute', action="store_true")
parser.add_argument('instiName', type=str)
parser.add_argument('-u', '--user', action="store_true")
args = parser.parse_args()

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
			onlyInstitute(param, instiName)
			time.sleep(3)
except ValueError as e:
	print e

import sys, argparse, time, re, os, json
import requests

root = "https://www.codechef.com/api/rankings/"

def onlyInstitute(param, instiName):
	url = root + param + instiName
	req = requests.get(url)
	print req.status_code

	if(req.status_code != 200):
		raise Exception('Cannot connect Code Chef\'s server')
	else:
		data = req.json()['list']
		# print json.dumps(data['list'])

		if not os.path.isfile('instiLog.json'):
			file = open('instiLog.json', 'w')
			file.write(json.dumps(data))
		else:
			file = open('instiLog.json', 'r')
			prevData = json.loads(file.read())

		


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
			time.sleep(1)
except ValueError as e:
	print e

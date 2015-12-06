import sys, argparse, time, re
import requests

def func(insti):
	insti = re.sub(' ', '%20', insti)
	url = "https://www.codechef.com/api/rankings/DEC15?filterBy=Institution%3D" + insti
	req = requests.get(url)
	print req.status_code

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--institute', action="store_true")
parser.add_argument('insti', type=str)
args = parser.parse_args()

# thread = threading.Timer(3, func, [args.insti])
while True:
	func(args.insti)
	time.sleep(3)

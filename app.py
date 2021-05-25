from flask import Flask, request
from utils import *

app = Flask(__name__)

keys = []
all_keys = []
for code in all_codes:
	all_keys.append(code['code'])


@app.route('/reset', methods=['GET'])
def reset():
	global keys
	keys = []
	return 'ok', 200


@app.route('/', methods=['GET'])
def get_all():
	return {
		       'keys': keys,
		       'keys_left': len(all_codes) - len(keys),
	       }, 200


@app.route('/addcode', methods=['GET'])
def add_code():
	code = request.args.get('code')
	if code in all_keys:
		if code not in keys:
			keys.append(code)
		return {
			       'keys': keys,
			       'keys_left': len(all_codes) - len(keys),
		       }, 200
	else:
		return 'Неправильний код', 400

@app.route('/unprinted', methods=['GET'])
def unprinted():
	for code in all_keys:
		if code not in keys:
			keys.append(code)
		return {
			       'keys_left': keys,
			       'keys_left_amount': len(all_codes) - len(keys),
		       }, 200
	else:
		return 'Неправильний код', 400


@app.route('/hint', methods=['GET'])
def get_hint():
	if len(all_codes) - len(keys) <1:
		return 'Підказок вже не залишилося', 200
	if len(all_codes) - len(keys) > 0 and len(keys) >= int(len(all_codes) / 2):
		for code in all_codes:
			if code['code'] not in keys:
				return code['hint'], 200
	else:
		return 'Підказки недоступні поки не здайдено хоча б половину кодів', 200


if __name__ == '__main__':
	app.run()
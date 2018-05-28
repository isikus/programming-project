import flask

app = flask.Flask(__name__)


if __name__ == '__main__':
	import os
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'
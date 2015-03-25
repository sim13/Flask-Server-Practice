from flask import Flask , redirect , url_for 
app = Flask(__name__)

@app.route('/')
def  render() :
	return app.send_static_file('simwahal.html')

@app.route('/<path:path>')
def  static_proxy(path) :
	 return app.send_static_file(path)

if __name__ == '__main__' :
	app.run()

	
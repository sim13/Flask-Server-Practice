from flask import Flask
from flask_restful import Resource , Api 

app =Flask(__name__)
api =Api(app, catch_all_404s =True)

class HelloWorld(Resource):
	def get(self) :
	 return {'hello' :'world'}
class TestResponse(Resource) :
	def get(self):
		return {'Etag' :'some-opaque-string'}
@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response 

api.add_resource(HelloWorld, '/json')
api.add_resource(TestResponse , '/testresponse')

if __name__ == '__main__' :
  app.run(debug=True)
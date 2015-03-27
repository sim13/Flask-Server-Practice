from flask import Flask
from flask_restful import Resource , Api 

app =Flask(__name__)
api =Api(app)

User_info {
	
	'username' : 'Simrin Wahal' ,
	'user_id'  : 	'1313' , 

}
class HelloWorld(Resource):
	def get(self) :
	 return {'hello' :'world'}

api.add_resource(HelloWorld, '/json')

if __name__ == '__main__' :
  app.run(debug=True)
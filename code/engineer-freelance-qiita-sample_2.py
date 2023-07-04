from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
api = Api(app)
jwt = JWTManager(app)

class Login(Resource):
	def post(self):
		username = request.form['username']
		password = request.form['password']
		if username == 'admin' and password == 'password':
			access_token = create_access_token(identity=username)
			return {'access_token': access_token}, 200
		else:
			return {'message': 'Invalid credentials'}, 401

api.add_resource(Login, '/login')

if __name__ == '__main__':
	app.run()

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld1(Resource):
    def get(self):
        name = request.args.get('name')
        if name == None:
            name = "world"
        return {'hello': name}
    
    def post(self):
        data = request.get_json()
        return {'hello': data['name']}

class HelloWorld2(Resource):
    def get(self, name):
        return {'hello': name}

api.add_resource(HelloWorld1, '/hello')
api.add_resource(HelloWorld2, '/hello/<name>')

if __name__ == "__main__":
    app.run(debug=True)
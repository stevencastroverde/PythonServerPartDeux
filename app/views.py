from flask import jsonify, request
from app import app, db
from .forms import LoginForm
from .models import User
people = [{
    'id': 1,
    'firstname': 'Steven',
    'lastname': 'Castroverde',
    },
    {
    'id': 2,
    'firstname': 'Cass',
    'lastname': 'Wilferd',
    }
]


@app.route('/')
@app.route('/index', methods=['GET'])
def getTheseMofos():
    return jsonify({'mofos':people})
@app.route('/<int:id>', methods =['GET'])
def getMofo(id):
        person = [person for person in people if person['id'] == id]
        return jsonify({'person': person[0]})
@app.route('/add', methods=["POST"])
def create_person():
        person = {
            'id': people[-1]['id'] +1,
            'firstname': request.json['firstname'],
            'lastname': request.json['lastname']

        }
        people.append(person)
        return jsonify({'person':person})
@app.route('/update/<int:id>', methods=["PUT"])
def updatePerson(id):
    person = [person for person in people if person['id'] == id]
    person[0]['firstname'] = request.json.get('firstname', person[0]['firstname'])
    person[0]['lastname'] = request.json.get('lastname', person[0]['lastname'])
    return jsonify({'person': person[0]})
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = [person for person in people if person['id'] == id]
    people.remove(person[0])
    return jsonify({'deleted':True})

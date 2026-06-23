import flask
from flask import request, jsonify
import student_generator_v2 as sg

# create a flask app object
app = flask.Flask(__name__)

# tell the server to reload each time the code changes
app.config["DEBUG"] = True

"""
Function to query the list of student dictionaries based on a search key, and a value
INPUT: search_key - key in the dictionary we want to check the value of
       search_value - the value of the key we need to match
OUTPUT: list of student dictionaries that match the search criteria
"""
def search_dictionary_list(search_key, search_value):
    student_dictionaries = sg.get_student_dictionaries()
    search_critiera_list = []
    for student_dict in student_dictionaries:
        if search_value == student_dictionaries[search_key]:
            search_critiera_list.append(student_dict)

# create a route/view for the home page of the application
@app.route('/', methods=['GET'])
def index():
    return "<h1>Student Data API</h1>"

# create end points for the functions we will create
# create a route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    # get student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

# create a route that returns students in a specific major

# create a route that returns students of a specific class (freshman, sophomore, junior, senior)
# create a route that returns a specific student by ID number

# run the application
app.run(debug=True)
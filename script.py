import numpy as np
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_marks():
	marks = request.get_json()
	#marks = json.loads(str(marks_json))

	response = {}
	users = []
	grades = []

	for mark in marks['users']:
		users.append(mark['user'])
		grades.append(mark['grade'])

	response["grade_point_average"] = np.average(grades)
	response["user_number"] = len(users)
	response["user_alphabetized"] = sorted(users)

	return response
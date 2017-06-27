from flask import Flask, render_template, request, jsonify
from search import search

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	#TODO: Why the hell do these need to be called 'name' and 'email'???
	topic_string = request.form['name']
	query_string = request.form['email']


	if query_string:

		#newName = (str(search(query_string))[19:])[:-1]
		newName = search(query_string)


		print(newName)

		return jsonify({'name' : newName})

	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)
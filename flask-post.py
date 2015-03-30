from flask import Flask, render_template, request, url_for


app =Flask(__name__)

@app.route('/') # default URL that loads form
def form():
	return render_template('form.html')
#define url when submit button is clicked in the form

@app.route('/hello/', methods =['POST'])
def hello():
	name_val =request.form['firstname']
	name_lastname = request.form['lastname']
	print name_val
	print name_lastname
	return render_template('form_action.html', name =name_val)

#Run the app
if __name__ =='__main__' :
	app.run(debug=True)
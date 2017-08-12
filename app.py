from flask import Flask, render_template, request, redirect
from sparkpost import SparkPost

app = Flask(__name__)
sparky = SparkPost('<API KEY HERE>')

@app.route('/')
def index():
	return render_template('index.html', page_classes='home')

@app.route('/contact')
def contact_page():
	return render_template('contact.html', page_classes='contact')

@app.route('/services')
def services_page():
	return render_template('services.html', page_classes='services');

@app.route('/sendmsg', methods=['GET', 'POST'])
def sendmsg():
	if request.method == 'POST':
		name = request.form['nameField']
		email = request.form['emailField']
		msg = request.form['msgField']

		recipients = ['TO_EMAIL']
		reply_to = email
		from_email = 'FROM_EMAIL'
		subject = '[New Message] ' + name + ' - ' + email
		html = msg

		sparky.transmissions.send(
			recipients=recipients,
			from_email=from_email,
			subject=subject,
			reply_to=reply_to,
			html=html
		)
		return redirect('/?send_msg=ok')

	return redirect('/')

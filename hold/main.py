from flask import Flask, request
from caesar import rotate_string

form = web-caesar.html
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return form.format()
	
@app.route('/encrypt', methods=['POST'])

def encrypt():
	rot = ''
	text = ''
	text = rotate_string(text)
	text = <h1>text</h1>
    return form.format(text)

app.run()

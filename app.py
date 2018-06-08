#Import the module flask

from flask import Flask, render_template
app = Flask(__name__)

#define the basic route / and its corresponding request handler
@app.route("/")
def main():
	return render_template("index.html")

#check if the executed file is the main program and run the app
if __name__ == '__main__':
	app.run()
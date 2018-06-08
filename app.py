#Import the module flask
from flask import Flask
app = Flask(_name_)

#define the basic route / and its corresponding request handler
@app.route("/")
def main():
	return "Welcome!"

#check if the executed file is the main program and run the app
if __name__ == '__main__':
	app.run()
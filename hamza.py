from flask import Flask,render_template

hamza = Flask(__name__)

@hamza.route("/")
def haka():
	return "Hamza Ali"


@hamza.route("/about")
def faka():
	return render_template("about.html")


@hamza.route("/index")
def zaka():
	return render_template("index.html")

if __name__ == '__main__':
	hamza.run(debug=True)

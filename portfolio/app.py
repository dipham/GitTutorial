from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')          								#This is the main URL
def default():
    return render_template("index.html", name = "index", title = "Diane Pham | Portfolio")			#The argument should be in templates folder


@app.route('/index')          							#This is the main URL
def index():
    return render_template("index.html", name = "index", title = "Diane Pham | Portfolio")			#The argument should be in templates folder


@app.route('/about')          							#This is the main URL
def about():
    return render_template("about.html", name = "about", title = "Diane Pham | About")

@app.route('/resume')
def resume():
    return render_template("resume.html", name = "resume", title = "Diane Pham | Resume")

@app.route('/contact')
def contact():
    return render_template("contact.html", name = "contact", title = "Diane Pham | Contact")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html'), 404





if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional

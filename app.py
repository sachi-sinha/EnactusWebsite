from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # creating route to index
def index():
    return render_template("index.html")

@app.route("/about") # creating route ABOUT US page
def about():
    return render_template("about.html")

@app.route("/services") # creating route SERVICES page
def services():
    return render_template("services.html")

@app.route("/contact") # creating route to CONTACT US page
def contact():
    return render_template("contact.html")


from flask import Flask,render_template,url_for,send_from_directory
import requests

app = Flask(__name__,template_folder="./templates")

@app.route("/", methods=['GET'])
def index():
    return render_template("home.html") 

@app.route("/projects", methods=['GET'])
def projects():
    uni_meetups_logo = url_for("static",filename="images/uni_meetups_logo.png")
    return render_template("projects.html",uni_meetups_logo=uni_meetups_logo)

@app.route("/about", methods=['GET'])
def about():
    response = requests.get("https://api.thecatapi.com/v1/images/search")

    if response.status_code == 200:
        resp_json = response.json()[0]
        cat_url = resp_json["url"]
        return render_template("about.html",cat_src=cat_url)

    return render_template("about.html") 

    

@app.route("/resume",methods=["GET"])
def resume():
    resume_location = "./static/misc"
    return send_from_directory(resume_location,"resume.pdf")

    
app.run(host="localhost",port=8080,debug=True)
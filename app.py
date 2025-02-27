from flask import Flask,render_template,request
import google.generativeai as genai
from textblob import TextBlob
import os

api = os.getenv("MAKERSUITE_API_TOKEN") 
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_QA", methods=["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/makersuite", methods=["GET","POST"])
def makersuite():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("makersuite.html",r=r.text))

""" @app.route("/prediction", methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html")) """

@app.route("/singapore_joke", methods=["GET","POST"])
def singapore_joke():
    return(render_template("singapore_joke.html"))

@app.route("/text_sentiment", methods=["GET","POST"])
def text_sentiment():
    return(render_template("text_sentiment.html"))

@app.route ("/SA",methods = ["GET","POST"])
def SA():
    return render_template('SA.html')

@app.route ("/SAR",methods = ["GET","POST"])
def SAR():
    q = request.form.get("q")
    r = TextBlob(q).sentiment
    return render_template('SAR.html',r=r)

@app.route ("/TM",methods = ["GET","POST"])
def TM():
    return render_template('TM.html')

if __name__ == "__main__":
    app.run()

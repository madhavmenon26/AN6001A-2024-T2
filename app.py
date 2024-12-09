from flask import Flask
from flask import render_template,request
import textblob
import os
import google.generativeai as genai

api = os.getenv("makersuite")
app = Flask(__name__)

@app.route("/",methods=["GET","POST"]) #send to and recieve from frontend
def index(): 
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"]) #send to and recieve from frontend
def main(): 
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/SA",methods=["GET","POST"]) #send to and recieve from frontend
def SA(): 
    return(render_template("SA.html"))

@app.route("/SA_result",methods=["GET","POST"]) #send to and recieve from frontend
def SA_result(): 
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html",r=r))

@app.route("/GenAI",methods=["GET","POST"]) #send to and recieve from frontend
def GenAI(): 
    return(render_template("GenAI.html"))

@app.route("/GenAI_result",methods=["GET","POST"]) #send to and recieve from frontend
def GenAI_result(): 
    q = request.form.get("q")
    #r = textblob.TextBlob(q).sentiment
    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-1.5-flash")
    r = model.generate_content(q)
    return(render_template("GenAI_result.html",r=r.text))

if __name__ == "__main__":
    app.run()
    #app.run(port=1111) #code to run on a different port
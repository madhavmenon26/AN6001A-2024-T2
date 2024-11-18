from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"]) #send to and recieve from frontend
def index(): 
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"]) #send to and recieve from frontend
def main(): 
    name = request.form.get("q")
    return(render_template("main.html"))

if __name__ == "__main__":
    app.run()
    #app.run(port=1111) #code to run on a different port
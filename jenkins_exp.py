from flask import Flask

app = Flask(_name_)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to Flask app deployement using Jenkins."

@app.route("/aboutus", methods=["GET"])
def about_us():
    return "This is about us page."

@app.route("/contactus", methods=["GET"])
def contact_us():
    return "Here you can find information about how to contact us."

if(_name) == "__main_":
    app.run(debug=True)

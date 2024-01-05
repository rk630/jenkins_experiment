from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "For the sake of assignment,run barry run"

@app.route("/aboutus", methods=["GET"])
def about_us():
    return "This is about us page."
 
@app.route("/contactus", methods=["GET"])
def contact_us():
    return "Here you can find information about how to contact us."

if __name__ == '__main__':
    app.run(port=5010, host='0.0.0.0')

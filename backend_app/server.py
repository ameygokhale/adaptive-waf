
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Application Running Behind WAF"

if __name__ == "__main__":
    app.run(port=9000)

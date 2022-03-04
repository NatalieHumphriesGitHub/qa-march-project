from flask import Flask

app = Flask(__name__)

@app.route('/')  
def home():
    return "Hello Internet!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
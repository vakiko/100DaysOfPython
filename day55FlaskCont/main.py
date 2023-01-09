from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/bye')
def bye():
    return "Bye, world!"
    
    
if __name__ == "__main__":
    app.run()


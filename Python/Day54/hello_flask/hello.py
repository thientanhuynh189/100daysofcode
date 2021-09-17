from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# definition.__name__ : The name of the class, function, method, descriptor, or generator instance


# Run without command
if __name__ == "__main__":
    app.run()

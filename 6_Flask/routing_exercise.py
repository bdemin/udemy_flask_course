from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is a welcome page!</h1>'

@app.route('/<name>') # Fill this in!
def puppylatin(name):
    if name[-1] == 'y':
        new_name = name[:-1] + 'iful'
    else:
        new_name = name + 'y'
    return "The name of the puppy is: {}".format(new_name)

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect')
def redirect():
    upper_flag = False
    lower_flag = False
    num_flag = False

    username = request.args.get('username')

    upper_flag = any(letter.isupper() for letter in username)
    lower_flag = any(letter.islower() for letter in username)
    num_flag = username[-1].isdigit()

    flag = lower_flag and upper_flag and num_flag
    
    return render_template('redirect.html', flag = flag, upper_flag = upper_flag,
                            lower_flag = lower_flag, num_flag = num_flag)

if __name__ == '__main__':
    app.run(debug=True)

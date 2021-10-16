from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Never Bow Down"

num = 1

@app.route('/')
def index():
    session['count'] = session['count'] + 1
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def counter():
    session['count'] = session['count'] + 1
    return redirect('/')

@app.route('/remove', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)
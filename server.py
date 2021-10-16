from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Never Bow Down"

@app.route('/')
def index():
    if 'count' in session:
        session['count'] = session['count'] + 1
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def counter():
    session['count'] = session['count'] + 1
    return redirect('/')

@app.route('/remove', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

@app.route('/destroySession')
def destroySession():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)
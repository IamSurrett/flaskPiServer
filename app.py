from flask import Flask
from Flask import render_template, request, redirect, url_for
from gamemain import doCommand, createWorld

app = Flask(__name__)
hostString = '0.0.0.0'
w = createWorld('ClueHouse')

# @app.route('/')

# def index():
#  return render_template('index.html', action = (hostString + ':5000/start'))
# def login():
#    if request.method == 'POST':
#       user = request.form['name']
#       return redirect(url_for('dashboard',name = user))
#    else:
#       user = request.args.get('name')
#       return render_template('login.html')

@app.route('/game', methods=['POST', 'GET'])
def game():
  if request.method == 'POST':
    return render_template('game.html', message=doCommand(w, request.form['command']))
  else:
    name = request.args.get('name')
    return render_template('game.html', message='welcome to TBAG!')

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
 app.run(debug=True, host=hostString)

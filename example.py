Flask = None
while not Flask:
    impl = input('What Flask implementation should I use?\n[R]eal Flask\n[A]lmost Flask\n>>> ').lower()
    if impl == 'r':
        from flask import Flask, session, request
    elif impl == 'a':
        from almost_flask import Flask, session, request
    else:
        print('Invalid input, try again!')

app = Flask(__name__)

@app.route('/')
def home():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return 'Home, visited %d times' % session['count']

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/hello/<name>', methods=['GET, POST, PUT'])
def hello_to(name):
    return 'Hello to %s (args %s, path %s, method %s)' % (name, request.args, request.path, request.method)

@app.route('/hello/<first_name>/<last_name>')
def hello_to_formal(first_name, last_name):
    return 'Hello to %s %s' % (first_name, last_name)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run()

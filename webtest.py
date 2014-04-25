from bottle import run,Bottle

app = Bottle()

@app.route('/hello')

def hello():
    return "hello world!"

run(app, host='', port=8080)

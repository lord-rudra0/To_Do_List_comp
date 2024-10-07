from flask import Flask
app=Flask(__name__)
@app.route('/hello<name>')

def getName(name):
    return f'Hello {name}! why are you black?'

if __name__ == '__main__':
    app.run(debug=True)

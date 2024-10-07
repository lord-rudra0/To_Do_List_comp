from flask import Flask ,render_template

app = Flask(__name__)
@app.route('/')

def index():
    str="""
<html>
<body>
<h1> Hello World </h1>
<button onclick="alert('Hello World!')">Click Me!</button>
</body>
</html>
"""
    return str

if __name__ == '__main__':
    app.run(debug=True)    
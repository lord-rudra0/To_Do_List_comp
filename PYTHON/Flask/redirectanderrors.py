from flask import Flask, redirect, url_for, abort, request, render_template,redirect

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login' , methods = ['POST', 'GET'])

def login():

   if request.method == 'POST':
       if request.form['username'] == 'admin' :
           return redirect(url_for('success'))
       else:
              return redirect(url_for('error'))
    

@app.route('/success')
def success():
    return 'logged in successfully'




# # @app.route('/user/<name>')
# # def user(name):
# #     if name == 'admin':
# #         return redirect(url_for('login'))
#     else:
#         return 'Hello %s!' % name
    
@app.route('/redirect')
def redirect():
    return redirect(url_for('login'))

@app.route('/error')
def error():
    return 'error in login'
    abort(404)
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('login.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
amm = Flask(__name__)
@amm.route('/')
def hello_world():
    return 'Hello, World make me !'
   
if __name__ == '__main__':
    amm.run(debug=True)
# amm.run(debug=True)
    
    # amm.debug = True
    # amm.run()
    
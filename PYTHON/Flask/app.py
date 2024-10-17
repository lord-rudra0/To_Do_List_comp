import os
import random
import string
from flask import Flask, request, jsonify, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import InMemoryVectorStore
from langchain import LLMChain, PromptTemplate
from pypdf import PdfReader
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from flask_cors import CORS
from sqlalchemy import create_engine

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/SDG EXPOLRER/your_database.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your_default_secret_key'

db = SQLAlchemy(app)

#delete the all data from the database


class User(db.Model):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


with app.app_context():
    db.create_all()


def generate_random_key(length=16):
    characters = string.ascii_letters + string.digits + 'abcdef'
    random_key = ''.join(random.choice(characters) for _ in range(length))
    return random_key

# if User:
#     print(f'User {User.username} hashed password: {User.password}')
#     print(f'Check password: {check_password_hash(User.password, "password")}')
    
# else:
    
#     print('User does not exist')
    

@app.route('/')
def index():
    return render_template('index.html')  
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        phone = data.get('phone')
         
            
            
        if username and email and password and phone:
            existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
            if existing_user:
                return jsonify({'message': 'User with this username or email already exists'}), 409

            hashed_password = generate_password_hash(password)
            user = User(username=username, email=email, password=hashed_password, phone=phone)
            db.session.add(user)
            db.session.commit()

            session['email'] = email  
            return jsonify({'message': 'Signup successful'}), 200
        
        return jsonify({'message': 'All fields are required'}), 400 
    
    return render_template('signup.html'), 200


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password') 
        
        print(email, password)
        if email and password:
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['email'] = email
                return jsonify({'message': 'Login successful'}),200
            else:
                return jsonify({'message': 'Invalid credentials'}), 401
    return render_template('login.html')  

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return jsonify({'message': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function


@app.route('/dashboard', endpoint='dashboard')
@login_required
def dashboard():
    return render_template('indexdash.html')

@app.route('/logout', endpoint='logout')
@login_required
def logout():
    session.pop('email', None)
    return jsonify({'message': 'Logout successful'})

#when i click on btn1 it should redirect to no_poverity.html

@app.route('/no-poverty')

def no_poverity():
    return render_template('goal1.html')

@app.route('/zero-hunger')

def zero_hunger():
    return render_template('goal2.html')

@app.route('/good-health')

def good_health():
    return render_template('goal3.html')

@app.route('/quality-education')

def quality_education():
        return render_template('goal4.html')
    
@app.route('/gender-equality')

def gender_equality():  
    return render_template('goal5.html')
    
@app.route('/clean-water')

def clean_water():  
    return render_template('goal6.html')
    
@app.route('/affordable-energy')

def affordable_energy():  
    return render_template('goal7.html')
    
@app.route('/decent-work')

def decent_work():    
    return render_template('goal8.html')
    
@app.route('/industry-innovation')

def industry_innovation():
    return render_template('goal9.html')
        
@app.route('/reduced-inequalities')

def reduced_inequalities():            
    return render_template('goal10.html')
            
@app.route('/sustainable-cities')

def sustainable_cities():
    return render_template('goal11.html')
                
@app.route('/responsible-consumption')

def responsible_consumption():
    return render_template('goal12.html')

@app.route('/climate-action')

def climate_action():    
    return render_template('goal13.html')

@app.route('/life-below-water')

def life_below_water():
    return render_template('goal14.html')
    
@app.route('/life-on-land')

def life_on_land():
    return render_template('goal15.html')

@app.route('/peace-justice')

def peace_justice():
    return render_template('goal16.html')

@app.route('/partnership')

def partnership():
    return render_template('goal17.html')

@app.route('/games')

def games():
    return render_template('game.html')


@app.route('/quiz1')
def quiz1():
    return render_template('quiz1.html')

@app.route('/quiz2')

def quiz2():
    return render_template('quiz2.html')

@app.route('/quiz3')

def quiz3():
    
    return render_template('quiz3.html')

@app.route('/quiz4')

def quiz4():
    return render_template('quiz4.html')

@app.route('/quiz5')
def quiz5():
    return render_template('quiz5.html')

@app.route('/quiz6')
def quiz6():
    return render_template('quiz6.html')

@app.route('/quiz7')
def quiz7():
    return render_template('quiz7.html')

@app.route('/quiz8')
def quiz8():
    return render_template('quiz8.html')

@app.route('/quiz9')
def quiz9():
    return render_template('quiz9.html')

@app.route('/quiz10')
def quiz10():
    return render_template('quiz10.html')

@app.route('/quiz11')
def quiz11():
    return render_template('quiz11.html')

@app.route('/quiz12')
def quiz12():
    return render_template('quiz12.html')

@app.route('/quiz13')
def quiz13():
    return render_template('quiz13.html')

@app.route('/quiz14')
def quiz14():
    return render_template('quiz14.html')

@app.route('/quiz15')
def quiz15():
    return render_template('quiz15.html')

@app.route('/quiz16')
def quiz16():
    return render_template('quiz16.html')

@app.route('/quiz17')
def quiz17():
    return render_template('quiz17.html')



@app.route('/dashboard-game1')
def dashboard_games():
    return render_template('Game1.html')

@app.route('/dashboard-game2')
def dashboard_games2():
    return render_template('game2.html')




CORS(app)

OPENAI_API_KEY = 'AIzaSyDSFSqcDt43ezHzFW1npREHhQ_E6Lvox2M'  
loader = PyPDFLoader("C:/SDG _EXPOLRER/SDG.pdf")  
pages = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(pages)


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=OPENAI_API_KEY)
docsearch = InMemoryVectorStore.from_documents(texts, embeddings)


template = """You are a teaching assistant:
{context}
Now, based on this information and some of your knowledge about SDG, answer the following question:
{question}
Provide a concise and accurate response based on all the given information, not just below:
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)


retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 2})
llm = ChatGoogleGenerativeAI(google_api_key=OPENAI_API_KEY, model="gemini-1.5-flash", temperature=0)


qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)


def get_text_response(message):
    query = message
    result = qa_chain.invoke(query)
    response = result['result']
    return response


data = {}

@app.route('/dashboard/api', methods=['POST'])
def update_data():
    global data
    key = request.json['key']
    value = request.json['value']
    data[key] = value
    RESULT = get_text_response(data["Quest"])
    return jsonify({'message': RESULT})
    
    return jsonify({'message': 'DataGAY updated successfully'})

@app.route('/dashboard/api', methods=['GET'])
def get_data():
    global data
    value=get_text_response(data["Quest"])
    data['Quest']=value
    RESULT = get_text_response(data["Quest"])
    return RESULT
@app.route('/dashboard/api', methods=['POST'])

def handle_question():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)

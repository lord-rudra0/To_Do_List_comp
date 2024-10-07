from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sdg.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# SDG Model
class SDG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sdg_number = db.Column(db.Integer, nullable=False)
    sdg_title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    earth_data = db.Column(db.Text, nullable=True)
    progress_current = db.Column(db.Float, nullable=False)
    target_2030 = db.Column(db.Float, nullable=False)
    case_study = db.Column(db.Text, nullable=True)

db.create_all()

# Populate SDG Data (if necessary)
@app.route('/populate_sdg_data')
def populate_sdg_data():
    sdg_13 = SDG(
        sdg_number=13,
        sdg_title="Climate Action",
        description="Climate change is one of the most pressing issues...",
        earth_data="NASA’s Earth observation tools provide critical information...",
        progress_current=45.0,
        target_2030=100.0,
        case_study="In areas like the Sahel region of Africa..."
    )
    db.session.add(sdg_13)
    db.session.commit()
    return "SDG data populated successfully"

# API to fetch all SDGs
@app.route('/api/sdgs')
def get_sdgs():
    sdgs = SDG.query.all()
    data = [{
        'sdg_number': sdg.sdg_number,
        'sdg_title': sdg.sdg_title,
        'description': sdg.description,
        'earth_data': sdg.earth_data,
        'case_study': sdg.case_study
    } for sdg in sdgs]
    return jsonify(data)

# API to fetch SDG details by SDG number
@app.route('/api/sdg/<int:sdg_number>')
def get_sdg_details(sdg_number):
    sdg = SDG.query.filter_by(sdg_number=sdg_number).first()
    if sdg:
        data = {
            'sdg_number': sdg.sdg_number,
            'sdg_title': sdg.sdg_title,
            'description': sdg.description,
            'earth_data': sdg.earth_data,
            'case_study': sdg.case_study
        }
        return jsonify(data)
    return jsonify({'error': 'SDG not found'}), 404

# Dashboard Route (Main Page)
@app.route('/')
def index():
    return render_template('index.html')

# SDG Details Route
@app.route('/sdg/<int:sdg_number>')
def sdg_detail(sdg_number):
    sdg = SDG.query.filter_by(sdg_number=sdg_number).first()
    if sdg:
        return render_template('sdg_detail.html', sdg=sdg)
    return "SDG not found", 404

if __name__ == '__main__':
    app.run(debug=True)

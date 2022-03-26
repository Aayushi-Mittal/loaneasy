from flask import Flask,request,jsonify
import numpy as np
import pickle

model1 = pickle.load(open('model1.pk1','rb'))
model2 = pickle.load(open('model2.pk1','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Loan Easy Flask API for predicting loan granted or not"

@app.route('/predict',methods=['POST'])
def predict():
    sector = request.form.get('Sector')
    age = request.form.get('Age')
    tv_bills = request.form.get('Tv Bills')
    water_bills = request.form.get('Water bills')
    e_bills = request.form.get('Electricity Bills')
    family = request.form.get('Family Members')
    isGroup = request.form.get('Group?')
    duration = request.form.get('Duration (year)')
    salary = request.form.get('Salary (yearly)')
    qual = request.form.get('Qualifications')
    district = request.form.get('District')
    state = request.form.get('State')
    loan_history = request.form.get('Loan History')
    loan_category = request.form.get('Loan Category')
    busi_sector = request.form.get('Sector of Business')
    founding_year = request.form.get('Founding Year')
    profit = request.form.get('Profit per anum')
    credit_score = request.form.get('Credit Score')
    
    input_query = np.array([[sector, age, tv_bills, water_bills, e_bills, family, isGroup, duration, salary, qual, district, state, loan_history, loan_category, busi_sector, founding_year, profit, credit_score]])

    result1 = model1.predict(input_query)[0]
    result2 = model2.predict(input_query)[0]

    return jsonify({'loan-granted':str(result1), 'risk-score':str(result2)})

if __name__ == '__main__':
    app.run(debug=True)
    
# 7.16,45,1,0,0,5,0,5.0,900000,5,0,10,-3,5,0.8,2020,400,1
# sector=7.16&age=45&tv_bills=1&water_bills=0&e_bills=0&family=5&isGroup=0duration=5&salary=900000&qual=5&district=0&state=10&loan_history=-3&loan_category=5&busi_sector=0.8&founding_year=2020&profit=400&credit_score=1
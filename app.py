from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        marital_status = request.form['marital_status']
        dependents = request.form['dependents']
        education = request.form['education']
        self_employed = request.form['self_employed']
        applicant_income = float(request.form['applicant_income'])
        coapplicant_income = float(request.form['coapplicant_income'])
        loan_amount = float(request.form['loan_amount'])
        loan_term = float(request.form['loan_term'])
        credit_history = float(request.form['credit_history'])
        property_area = request.form['property_area']

        if(gender == "Male"):
            Male = 1
        else:
            Male = 0

        if(marital_status == "Yes") :
            Married_Yes = 1
        else:
            Married_Yes = 0
        
        if(dependents == "3+"):
            Dependents = 3
        elif(dependents == "2"):
            Dependents = 2
        elif(dependents == "1"):
            Dependents = 1
        else:
            Dependents = 0
        
        if(education == "Graduate"):
            Graduate = 1
        elif(education == "Not Graduate"):
            Graduate = 0
        
        if(self_employed == "Yes"):
            SelfEmployment_Yes = 1
        elif(self_employed == "No"):
            SelfEmployment_Yes = 0
        
        if(property_area == "Rural"):
            Rural = 1
            Semiurban = 0
        elif(property_area == "Semiurban"):
            Rural = 0
            Semiurban = 1
        elif(property_area == "Urban"):
            Rural = 0
            Semiurban = 0

        ApplicantIncome = applicant_income
        CoapplicantIncome = coapplicant_income
        LoanAmount = loan_amount
        Loan_Amount_Term = loan_term
        Credit_History = credit_history
        prediction = model.predict([[Male, Married_Yes, Dependents, Graduate, SelfEmployment_Yes, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Rural, Semiurban]])

        if(prediction == 1):
            prediction = "Yes"
        elif(prediction == 0):
            prediction ="NO"

        return render_template("predict.html", prediction_text = "Loan Status is {}".format(prediction))
        




    else:
        return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)
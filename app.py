from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
preprocessor= pickle.load(open('preprocessor.pkl','rb'))
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Subscription_Length_Months= int(request.form['Subscription_Length_Months'])
        Monthly_Bill = float(request.form['Monthly_Bill'])
        Total_Usage_GB = int(request.form['Total_Usage_GB'])
        log_Subscription_Length_Months = float(request.form['log_Subscription_Length_Months'])
        log_Monthly_Bill = float(request.form['log_Monthly_Bill'])
        log_Total_Usage_GB = float(request.form['log_Total_Usage_GB'])
        interaction_feature = float(request.form['interaction_feature'])
        Location = request.form['Location']
        if(Location == 'Chicago'):
            Location_Chicago = 1
            Location_Houston= 0
            Location_LosAngeles = 0
            Location_Miami = 0
            Location_NewYork = 0

            
                
        elif(Location == 'Houston'):
            Location_Chicago = 0
            Location_Houston= 1
            Location_LosAngeles = 0
            Location_Miami = 0
            Location_NewYork = 0
            Geography_France = 0
            
            
        elif(Location == 'LosAngeles'):
            Location_Chicago = 0
            Location_Houston= 0
            Location_LosAngeles = 1
            Location_Miami = 0
            Location_NewYork = 0
            Geography_France = 0
            
        elif(Location == 'Miami'):
            Location_Chicago = 0
            Location_Houston= 0
            Location_LosAngeles = 0
            Location_Miami = 1
            Location_NewYork = 0
            Geography_France = 0 
            
        elif(Location == 'NewYork'):
            Location_Chicago = 0
            Location_Houston= 0
            Location_LosAngeles = 0
            Location_Miami = 0
            Location_NewYork = 1
            Geography_France = 0           
        
        else:
            Location_Chicago = 0
            Location_Houston= 0
            Location_LosAngeles = 0
            Location_Miami = 0
            Location_NewYork = 0
            Geography_France = 1
        Gender = request.form['Gender']
        if(Gender == 'Male'):
            Gender_Male = 1
            Gender_Female = 0
        else:
            Gender_Male = 0
            Gender_Female = 1
            
            
        input_data = pd.DataFrame({
            'Age': [Age],
            'Subscription_Length_Months': [Subscription_Length_Months],
            'Monthly_Bill': [Monthly_Bill],
            'Total_Usage_GB': [Total_Usage_GB],
            'log_Subscription_Length_Months': [log_Subscription_Length_Months],
            'log_Monthly_Bill': [log_Monthly_Bill],
            'log_Total_Usage_GB': [log_Total_Usage_GB],
            'interaction_feature': [interaction_feature],
            'Location': [Location],
            'Gender':[Gender]
        })    
        new_data = preprocessor.fit_transform(input_data)    
        prediction = model.predict(new_data)
        if prediction==1:
             return render_template('index.html',prediction_text="The Customer will leave the bank")
        else:
             return render_template('index.html',prediction_text="The Customer will not leave the bank")
                
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
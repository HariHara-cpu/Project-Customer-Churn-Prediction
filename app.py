from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model and column names
try:
    model = pickle.load(open('notebooks/model.pkl', 'rb'))
    columns = pickle.load(open('notebooks/columns.pkl', 'rb'))
    print("Model and columns loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    columns = []


def transform_form_data(form_data):
    """
    Transform raw form data into model-compatible feature format.

    The model expects a specific one-hot encoded format with binary columns.
    """
    processed = {}

    # Basic numeric and binary fields (direct mapping)
    processed['gender'] = int(form_data.get('gender', 0))
    processed['SeniorCitizen'] = int(form_data.get('SeniorCitizen', 0))
    processed['Partner'] = int(form_data.get('Partner', 0))
    processed['Dependents'] = int(form_data.get('Dependents', 0))
    processed['tenure'] = float(form_data.get('tenure', 0))
    processed['PhoneService'] = int(form_data.get('PhoneService', 0))
    processed['PaperlessBilling'] = int(form_data.get('PaperlessBilling', 0))
    processed['MonthlyCharges'] = float(form_data.get('MonthlyCharges', 0))
    processed['TotalCharges'] = float(form_data.get('TotalCharges', 0))

    # MultipleLines: 0=No, 1=Yes, 2=No phone service
    multiple_lines = form_data.get('MultipleLines', '0')
    processed['MultipleLines'] = 0 if multiple_lines == '2' else int(multiple_lines)

    # OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies
    # 0=No, 1=Yes, 2=No internet service
    for field in ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                  'StreamingTV', 'StreamingMovies']:
        value = form_data.get(field, '0')
        processed[field] = 0 if value == '2' else int(value)

    # One-hot encoding for InternetService
    # Reference category: DSL (no column created for it)
    internet_service = form_data.get('InternetService', '')
    processed['InternetService_Fiber optic'] = 1 if internet_service == 'Fiber optic' else 0
    processed['InternetService_No'] = 1 if internet_service == 'No' else 0
    # If DSL is selected, both columns remain 0 (reference category)

    # One-hot encoding for Contract
    # Reference category: Month-to-month (no column created)
    contract = form_data.get('Contract', '')
    processed['Contract_One year'] = 1 if contract == 'One year' else 0
    processed['Contract_Two year'] = 1 if contract == 'Two year' else 0
    # If Month-to-month is selected, both columns remain 0

    # One-hot encoding for PaymentMethod
    # Reference category: Bank transfer (automatic) (no column created)
    payment_method = form_data.get('PaymentMethod', '')
    processed['PaymentMethod_Credit card (automatic)'] = 1 if payment_method == 'Credit card (automatic)' else 0
    processed['PaymentMethod_Electronic check'] = 1 if payment_method == 'Electronic check' else 0
    processed['PaymentMethod_Mailed check'] = 1 if payment_method == 'Mailed check' else 0
    # If Bank transfer is selected, all three columns remain 0

    # NOTE: The model was trained with these columns:
    # 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
    # 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    # 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling',
    # 'MonthlyCharges', 'TotalCharges', 'Contract_One year', 'Contract_Two year',
    # 'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check',
    # 'PaymentMethod_Mailed check', 'InternetService_Fiber optic', 'InternetService_No'

    return processed


@app.route('/')
def home():
    """Render the main prediction form."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests."""
    try:
        # Get form data
        data = request.form.to_dict()

        # Transform raw categorical inputs to model features
        processed_data = transform_form_data(data)

        # Create DataFrame with correct column order
        input_df = pd.DataFrame([processed_data], columns=columns)

        # Make prediction
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]

        # Prepare response
        result = {
            'prediction': int(prediction),
            'churn_probability': float(probability[1]),  # Probability of churn
            'no_churn_probability': float(probability[0]),  # Probability of no churn
            'message': 'Customer is likely to churn' if prediction == 1 else 'Customer is likely to stay'
        }

        return render_template('index.html', result=result, form_data=data)

    except Exception as e:
        return render_template('index.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

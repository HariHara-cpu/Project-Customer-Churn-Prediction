#!/usr/bin/env python
"""Test script for Customer Churn Prediction Flask App"""

import requests

# Sample customer data (all features)
sample_data = {
    'gender': '0',
    'SeniorCitizen': '0',
    'Partner': '1',
    'Dependents': '0',
    'tenure': '12',
    'PhoneService': '1',
    'MultipleLines': '0',
    'InternetService': 'DSL',
    'OnlineSecurity': '1',
    'OnlineBackup': '1',
    'DeviceProtection': '0',
    'TechSupport': '0',
    'StreamingTV': '1',
    'StreamingMovies': '1',
    'PaperlessBilling': '1',
    'MonthlyCharges': '75.50',
    'TotalCharges': '906.00',
    'Contract': 'Month-to-month',
    'PaymentMethod': 'Electronic check'
}

def test_prediction():
    """Test the prediction endpoint with sample data"""
    url = 'http://127.0.0.1:5000/predict'

    try:
        response = requests.post(url, data=sample_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")

        if response.status_code == 200:
            print("\nPrediction successful!")
            print(f"HTML response length: {len(response.text)} bytes")

            # Check if success indicators are in the response
            if 'Customer is likely to' in response.text:
                print("[OK] Prediction message rendered")
            if 'Churn Probability' in response.text:
                print("[OK] Probability meter displayed")
            if 'churn-probability' in response.text:
                print("[OK] Result card generated")
        else:
            print(f"\nError response: {response.text[:500]}")

    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not connect to server. Is the Flask app running?")
        print("   Run: python app.py")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")


if __name__ == '__main__':
    print("=== Customer Churn Prediction - Test Script ===\n")
    test_prediction()

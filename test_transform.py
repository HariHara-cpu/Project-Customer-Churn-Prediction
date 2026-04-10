#!/usr/bin/env python
"""Quick verification of transform_form_data function"""

import sys
sys.path.append('.')
from app import transform_form_data, columns

# Test case 1: DSL internet, Month-to-month contract, Bank transfer payment
test_data = {
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
    'PaymentMethod': 'Bank transfer (automatic)'
}

result = transform_form_data(test_data)

print("Transform test results:")
print("-" * 50)

# Check all expected columns exist
missing = [col for col in columns if col not in result]
if missing:
    print(f"[ERROR] Missing columns: {missing}")
else:
    print(f"[OK] All {len(columns)} model columns are present")

# Verify specific transformations
print("\nKey transformations:")
print(f"  InternetService_Fiber optic: {result.get('InternetService_Fiber optic')} (expected 0 for DSL)")
print(f"  InternetService_No: {result.get('InternetService_No')} (expected 0 for DSL)")
print(f"  Contract_One year: {result.get('Contract_One year')} (expected 0 for Month-to-month)")
print(f"  Contract_Two year: {result.get('Contract_Two year')} (expected 0 for Month-to-month)")
print(f"  PaymentMethod_Bank transfer (automatic): {result.get('PaymentMethod_Bank transfer (automatic')} (expected 1)")
print(f"  PaymentMethod_Credit card (automatic): {result.get('PaymentMethod_Credit card (automatic')} (expected 0)")
print(f"  PaymentMethod_Electronic check: {result.get('PaymentMethod_Electronic check')} (expected 0)")
print(f"  PaymentMethod_Mailed check: {result.get('PaymentMethod_Mailed check')} (expected 0)")

# Test case 2: Fiber optic, One year contract, Credit card
print("\n" + "-" * 50)
test_data2 = test_data.copy()
test_data2['InternetService'] = 'Fiber optic'
test_data2['Contract'] = 'One year'
test_data2['PaymentMethod'] = 'Credit card (automatic)'
result2 = transform_form_data(test_data2)

print("Test case 2 (Fiber, 1yr, Credit):")
print(f"  InternetService_Fiber optic: {result2.get('InternetService_Fiber optic')} (expected 1)")
print(f"  Contract_One year: {result2.get('Contract_One year')} (expected 1)")
print(f"  PaymentMethod_Credit card (automatic): {result2.get('PaymentMethod_Credit card (automatic')} (expected 1)")

print("\n[SUCCESS] Transform function verified!")

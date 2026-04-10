# Customer Churn Prediction

A web-based machine learning application for predicting customer churn in the telecom industry using a Random Forest classifier.

## Project Structure

```
customer-churn-prediction/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── notebooks/            # Jupyter notebooks
│   ├── EDA and Feature Engineering.ipynb
│   ├── Model building and training.ipynb
│   ├── model.pkl        # Trained Random Forest model
│   └── columns.pkl      # Feature column names
├── templates/           # HTML templates
│   └── index.html      # Main prediction form
└── static/            # Static files
    └── style.css      # Application styles
```

## Features

- **Interactive Web Interface**: User-friendly HTML form for inputting customer data
- **Real-time Predictions**: Instant churn probability predictions
- **Model Explainability**: Displays both churn and no-churn probabilities
- **Responsive Design**: Works on desktop and mobile devices
- **Validated Model**: Random Forest trained on telecom churn dataset with SMOTE for handling class imbalance

## Model Performance

- **Algorithm**: Random Forest Classifier
- **Best Parameters** (from RandomizedSearchCV):
  - max_depth: 5
  - min_samples_leaf: 1
  - min_samples_split: 5
  - n_estimators: 100
- **Recall**: 73.85% (optimized for churn detection)
- **ROC-AUC**: 83.5%

## Installation

### Prerequisites

- Python 3.9+
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   cd "Customer Churn Prediction"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify model files**
   Ensure the following files exist in the `notebooks/` directory:
   - `model.pkl` - Trained Random Forest model
   - `columns.pkl` - Feature column names

## Running the Application

### Start the Flask server

```bash
python app.py
```

The application will start at: **http://localhost:5000**

### Access the web interface

Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Fill out the customer information form** with details about:
   - Demographics (gender, senior citizen status, partner, dependents)
   - Services (phone, internet, streaming, etc.)
   - Billing information (charges, contract type, payment method)

2. **Click "Predict Churn"** to get instant predictions

3. **View Results**:
   - Churn probability percentage
   - No-churn probability percentage
   - Prediction message: "Customer is likely to churn/stay"

## Form Fields

### Customer Demographics
- Gender
- Senior Citizen (Yes/No)
- Partner (Yes/No)
- Dependents (Yes/No)

### Services
- Tenure (number of months as customer)
- Phone Service (Yes/No)
- Multiple Lines (Yes/No/No phone service)
- Internet Service (DSL/Fiber/None)
- Online Security (Yes/No/No internet)
- Online Backup (Yes/No/No internet)
- Device Protection (Yes/No/No internet)
- Tech Support (Yes/No/No internet)
- Streaming TV (Yes/No/No internet)
- Streaming Movies (Yes/No/No internet)

### Billing
- Monthly Charges
- Total Charges
- Contract Type (Month-to-month/One year/Two year)
- Paperless Billing (Yes/No)
- Payment Method (Electronic check, Mailed check, Credit card, Bank transfer)

## API Endpoints

- `GET /` - Renders prediction form
- `POST /predict` - Processes form and returns prediction

## Development

The application uses:
- **Flask** for the web framework
- **pandas** for data manipulation
- **scikit-learn** for ML model inference
- **pickle** for model serialization

## Output
<img width="799" height="924" alt="image" src="https://github.com/user-attachments/assets/2a165ec7-39c9-4fb2-868d-b96a825d126d" />

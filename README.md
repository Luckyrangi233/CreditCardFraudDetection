💳 Credit Card Fraud Detection
This project predicts whether a credit card transaction is fraudulent or genuine using a trained machine learning model.

Features Used in Prediction
V1, V2, V3, ..., V10: These are anonymized features derived from the original transaction data using mathematical transformations (like PCA) to protect sensitive information. They are numbers that describe the transaction patterns.

Amount: The actual amount of money involved in the transaction.


Note: Some feature values may be negative because of the mathematical transformations applied.


How Prediction Works
You can enter transaction details manually (values for V1 to V10 and Amount) and get a prediction.

Or, you can upload a CSV file containing many transactions to check them all at once.

The model will classify each transaction as:

0 = Genuine transaction

1 = Fraudulent transaction
# Credit Card Fraud Detection - Flask Web App

This is a demo Flask web app for credit card fraud detection. It uses a Logistic Regression model trained on a synthetic dataset for demonstration purposes.

## Features
- Manual single-transaction prediction (enter V1..V10 and Amount)
- Batch prediction via CSV upload (CSV must contain columns: V1..V10, Amount)
- Results for batch predictions are saved in `uploads/` as `results_<originalfilename>.csv`

## Run locally
1. Create a Python virtual environment and activate it:
```bash
python -m venv venv
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# or Git Bash / cmd
.\venv\Scripts\activate
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Flask app:
```bash
python app.py
```
4. Open your browser at: http://127.0.0.1:5000/

## Files in this package
- `app.py` - Flask backend
- `model/` - contains `model.pkl` and `scaler.pkl`
- `dataset/creditcard_sample.csv` - sample CSV with V1..V10 and Amount columns
- `templates/` - HTML templates
- `static/` - styles
- `requirements.txt` - dependencies

## Notes
- Replace the model with one trained on the real `creditcard.csv` dataset for production.
"# CreditCardFraudDetection" 
<img width="1635" height="910" alt="image" src="https://github.com/user-attachments/assets/c343b6ab-12e3-4f9f-9b7b-c7816e1477d1" />

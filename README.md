
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

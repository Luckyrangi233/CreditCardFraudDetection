
from flask import Flask, render_template, request, redirect, url_for, flash
import joblib, os, pandas as pd, numpy as np
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"csv"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "replace-with-a-secure-key"

# Load model and scaler
model = joblib.load(os.path.join("model", "model.pkl"))
scaler = joblib.load(os.path.join("model", "scaler.pkl"))

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Two modes: manual form or CSV upload
        if "predict_single" in request.form:
            try:
                # Read inputs from form
                features = []
                for i in range(1, 11):
                    features.append(float(request.form.get(f"V{i}", 0)))
                amount = float(request.form.get("Amount", 0))
                features.append(amount)
                X = np.array([features])
                Xs = scaler.transform(X)
                pred = model.predict(Xs)[0]
                proba = model.predict_proba(Xs)[0][1]
                result = {"prediction": int(pred), "probability": float(proba)}
                return render_template("result.html", single=True, result=result, inputs=features)
            except Exception as e:
                flash("Error predicting: " + str(e))
                return redirect(url_for("index"))
        elif "upload_csv" in request.form:
            # CSV upload handling
            if "file" not in request.files:
                flash("No file part")
                return redirect(request.url)
            file = request.files["file"]
            if file.filename == "":
                flash("No selected file")
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)
                try:
                    df = pd.read_csv(path)
                    # expect dataframe to contain the same features V1..V10 and Amount, or try to use available columns
                    expected = [f"V{i}" for i in range(1,11)] + ["Amount"]
                    missing = [c for c in expected if c not in df.columns]
                    if missing:
                        flash("Uploaded CSV is missing columns: " + ", ".join(missing))
                        return redirect(url_for("index"))
                    X = df[expected].values
                    Xs = scaler.transform(X)
                    preds = model.predict(Xs)
                    probs = model.predict_proba(Xs)[:,1]
                    df["Prediction"] = ["Fraud" if p==1 else "Not Fraud" for p in preds]
                    df["Fraud_Probability"] = probs
                    # Save results to uploads/results_*.csv
                    out_path = os.path.join(app.config['UPLOAD_FOLDER'], "results_" + filename)
                    df.to_csv(out_path, index=False)
                    return render_template("result.html", single=False, table_html=df.head(200).to_html(classes='table table-striped', index=False), out_file=out_path)
                except Exception as e:
                    flash("Error processing CSV: " + str(e))
                    return redirect(url_for("index"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

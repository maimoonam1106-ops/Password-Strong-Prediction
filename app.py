from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model and vectorizer
with open("password_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    password = request.form["password"]

    # Convert password to vector
    vector = vectorizer.transform([password])

    # Predict password strength
    result = int(model.predict(vector)[0])

    # -------- Password Strength --------
    if result == 0:
        prediction = "Weak"
        color = "danger"
        progress = 30
        score = 30

    elif result == 1:
        prediction = "Medium"
        color = "warning"
        progress = 65
        score = 65

    elif result == 2:
        prediction = "Strong"
        color = "success"
        progress = 100
        score = 100

    else:
        prediction = "Unknown"
        color = "secondary"
        progress = 0
        score = 0

    # -------- Suggestions --------
    suggestions = []

    if len(password) < 8:
        suggestions.append("❌ Password should contain at least 8 characters.")
    else:
        suggestions.append("✅ Good password length.")

    if any(c.isupper() for c in password):
        suggestions.append("✅ Contains uppercase letters.")
    else:
        suggestions.append("❌ Add uppercase letters.")

    if any(c.islower() for c in password):
        suggestions.append("✅ Contains lowercase letters.")
    else:
        suggestions.append("❌ Add lowercase letters.")

    if any(c.isdigit() for c in password):
        suggestions.append("✅ Contains numbers.")
    else:
        suggestions.append("❌ Add numbers.")

    if any(not c.isalnum() for c in password):
        suggestions.append("✅ Contains special characters.")
    else:
        suggestions.append("❌ Add special characters.")

    # -------- Password Statistics --------
    length = len(password)
    uppercase = sum(1 for c in password if c.isupper())
    lowercase = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    special = sum(1 for c in password if not c.isalnum())

    return render_template(
        "index.html",
        prediction=prediction,
        color=color,
        progress=progress,
        score=score,
        suggestions=suggestions,
        length=length,
        uppercase=uppercase,
        lowercase=lowercase,
        digits=digits,
        special=special,
        password=password
    )


if __name__ == "__main__":
    app.run(debug=True)
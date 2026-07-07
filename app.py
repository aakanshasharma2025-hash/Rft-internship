from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions


@app.route("/", methods=["GET", "POST"])
def home():
    strength = None
    suggestions = []

    if request.method == "POST":
        password = request.form["password"]
        strength, suggestions = check_password_strength(password)

    return render_template(
        "index.html",
        strength=strength,
        suggestions=suggestions
    )


if __name__ == "__main__":
    app.run(debug=True)

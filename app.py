from flask import Flask, request, render_template, jsonify, session
import os
from main import (
    agent,
    format_prompt,
    execute_query,
    horoscope_qe,
    zodiac_qe,
    risk_of_death_qe,
    traffic_accidents_qe,
    life_expectancy_qe,
    life_and_death_qe,
    income_qe,
    marriage_qe,
)

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Setzt einen geheimen Schlüssel für die Sitzungen

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile.html")
def profile():
    description = session.get("user_description", "")  # Holt die Beschreibung aus der Sitzung
    return render_template("profile.html", description=description)


@app.route("/save_description", methods=["POST"])
def save_description():
    session["user_description"] = request.form["description"]  # Speichert die Beschreibung in der Sitzung
    return jsonify(result="Beschreibung gespeichert")


@app.route("/query", methods=["POST"])
def query():
    prompt = request.form["prompt"]
    user_description = session.get("user_description", "")
    full_prompt = format_prompt(prompt, user_description)
    result = agent.query(full_prompt)
    formatted_result = f"{result}"
    return jsonify(result=formatted_result)


@app.route("/execute_query", methods=["POST"])
def query_execution():
    query = request.json["query"]
    result = execute_query(
        horoscope_qe,
        zodiac_qe,
        risk_of_death_qe,
        traffic_accidents_qe,
        life_expectancy_qe,
        life_and_death_qe,
        income_qe,
        marriage_qe,
        query,
    )
    return jsonify(result=result.tolist() if hasattr(result, "tolist") else result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify
import json
import os
from services.scoring import score_places, build_pros_and_cons
from services.summary import generate_summary

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

with open(os.path.join(DATA_DIR, "towns.json"), "r", encoding="utf-8") as f:
    towns = json.load(f)

with open(os.path.join(DATA_DIR, "preferences.json"), "r", encoding="utf-8") as f:
    preferences = json.load(f)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Wonder Journey backend is running.",
        "endpoints": ["/town-summary"]
    })

@app.route("/town-summary", methods=["POST"])
def town_summary():
    data = request.get_json(silent=True) or {}
    town_name = data.get("town")

    if not town_name:
        return jsonify({"error": "Missing required field: town"}), 400

    if town_name not in towns:
        return jsonify({"error": f"Town '{town_name}' not found"}), 404

    town_data = towns[town_name]
    places = town_data["places"]
    category_weights = preferences["categoryWeights"]

    scored_places = score_places(places, category_weights)
    pros, cons = build_pros_and_cons(scored_places)
    spoken_summary = generate_summary(town_name, pros, cons)

    return jsonify({
        "town": town_name,
        "state": town_data["state"],
        "coordinates": {
            "latitude": town_data["latitude"],
            "longitude": town_data["longitude"]
        },
        "pros": pros,
        "cons": cons,
        "topPicks": scored_places[:3],
        "spokenSummary": spoken_summary
    })

if __name__ == "__main__":
    app.run(debug=True)

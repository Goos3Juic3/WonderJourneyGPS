# Wonder Journey Backend Prototype

# Files
- `app.py` - Flask API entry point
- `data/towns.json` - mock town/place data
- `data/preferences.json` - mock user preference profile
- `services/scoring.py` - scoring and pros/cons logic
- `services/summary.py` - spoken summary generation

# Setup
```bash
pip install -r requirements.txt
python app.py
```

# Test request
Send a POST request to `/town-summary` with JSON like:
```json
{
  "town": "Dallas"
}
```
OR
```json
{
  "town": "Texarkana"
}
```

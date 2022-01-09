import datetime
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def fetch_data():
  # --- Call KaaS REST endpoint ---
  req = requests.get('https://api.kanye.rest/')
  resp = req.content
  return resp
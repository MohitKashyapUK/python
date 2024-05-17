# Framework
from flask import Flask, request, jsonify

# Libraries
import os
from pytube import YouTube
from urllib.parse import unquote

# Initializing the app
app = Flask(__name__)

# Home page
@app.route("/")
def index():
  return "<h1>Hello, this is a home page!</h1>"

@app.get("/api/youtube")
def api_youtube():
  URL = request.args.get("url")

  if URL == None: return jsonify({ "error": "Please provide the URL." })
  
  URL = unquote(URL)

  yt = YouTube(URL)
  # desc = yt.description
  # return jsonify({ "desc": desc })
  print(yt.description)
  return ""

  """try:
  except:
    return jsonify({ "error": "Something went wrong." })"""
#! /usr/bin/env python
from flask import Flask, url_for, jsonify, request
import lib.features as Features
import json, pymongo
import lib.repo as Repo
from flask.ext.cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)

# Serve the static index.html file
@app.route('/')
def root():
  return app.send_static_file('index.html')

# Return a list of repos from the mongo database
@app.route('/repos', methods=['GET'])
def get_repos():
  repos = Repo.find()
  return repos

# Handle the user's search
@app.route('/search', methods=['POST'])
def features_search():
  data = json.loads(request.data)
  query = str(data["query"])
  repos = list(data["repos"])

  def get_full_name(r): return str(r["full_name"])
  full_names = map(get_full_name, repos)

  return json.dumps({"query": query, "repos": repos })

app.run(debug=True)

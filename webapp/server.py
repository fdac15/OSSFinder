#! /usr/bin/env python
from flask import Flask, url_for, jsonify, request
import lib.features as Features
import lib.relationships as Relationships
import json, pymongo
import lib.repo as Repo
from flask.ext.cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)

# Setup feature search
search_service = Features.service_initialization('./feature-search-model', './feature-search-readmes')

# Define routes

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
  feature_query = str(data["query"])
  user_repos = list(data["repos"])

  def get_full_name(r): return str(r["full_name"])
  full_names = map(get_full_name, user_repos)

  feature_repos = Features.search(feature_query, search_service, min_score=0.25, max_results=100)
  matched_repos = Relationships.match_repos(feature_repos, user_repos)
  
  return json.dumps(matched_repos)

app.run(debug=True)

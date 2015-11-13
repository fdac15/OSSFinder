#! /usr/bin/env python
from flask import Flask, url_for, jsonify
#import lib.features as Features
import json
import lib.repo as Repo
import pymongo

app = Flask(__name__, static_url_path='')

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
@app.route('/features/search', methods=['POST'])
def features_search():
  return 'features search'

app.run()

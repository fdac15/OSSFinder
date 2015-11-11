from flask import Flask, url_for
import lib.features as features

app = Flask(__name__, static_url_path='')

# Serve the static index.html file
@app.route('/')
def root():
  return app.send_static_file('index.html')

# Return a list of repos from the mongo database
@app.route('/repos', methods=['GET'])
def get_repos():
  return 'get repos'

# Handle the user's search
@app.route('/features/search', methods=['POST'])
def features_search():
  return 'features search'

app.run()

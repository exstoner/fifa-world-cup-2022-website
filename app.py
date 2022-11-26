from flask import *
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    def get_standings():
            uri = 'https://api.football-data.org/v4/competitions/2000/standings'
            headers = { 'X-Auth-Token': '95b24a1ff13c4ad1af05c04a8434b95f' }
            response = requests.get(uri, headers=headers)
            standings = response.json()["standings"]
            return standings
    def get_matches():
            uri = 'https://api.football-data.org/v4/competitions/2000/matches'
            headers = { 'X-Auth-Token': '95b24a1ff13c4ad1af05c04a8434b95f' }
            response = requests.get(uri, headers=headers)
            matches = response.json()["matches"]
            return matches
    return render_template('test.html', standings=get_standings(), matches=get_matches())

if __name__ == '__main__':
    app.run(debug=True)
  
## Data Pipe
The code pull data from google sheet and push it on an Elastic Search Cluster. All hosts/adresses are set in config.json.

###  Run
source inside your virtual environnement then:
```bash
pip install -r requirements.txt
python server.py
```
In config.json replace #ServerAdress by the ES server's address.
You'll need to set google API credentials (see [Using OAuth2 for Authentication](https://gspread.readthedocs.io/en/latest/oauth2.html)).

import urllib
import json
import xml
import pandas as pd
from elasticsearch import Elasticsearch
from google.oauth2.service_account import Credentials
import gspread


def read_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


def load_gsheet(name, credentials):
    gc = connect_gs(credentials=credentials)
    gsheet = gc.open(name).sheet1  # Sheet Selection option may be required
    return pd.DataFrame(gsheet.get_all_records())


def connect_gs(credentials=''):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file(
        credentials, scopes=scope)

    return gspread.authorize(credentials)


def es_write_dataframe(dataframe, host, index):
    es = es_connect(host)
    responses = []
    for identifier, data in enumerate(dataframe.to_dict(orient='records')):
        responses.append(es.index(index=index, id=identifier, body=data))

    return responses


def es_connect(host):
    return Elasticsearch([host])


def fetch_arxiv_article(query, entry):
    arxiv_prefix = '{http://www.w3.org/2005/Atom}'
    parsed_query = urllib.parse.quote(query)
    url = 'http://export.arxiv.org/api/query?search_query=all:{}&start=0&max_results=1'.format(
        parsed_query)
    data = urllib.request.urlopen(url).read().decode()
    root = ET.fromstring(data)
    xml_entry = root.findall('./{prefix}entry/'.format(prefix=arxiv_prefix))
    print()
    infos = root.findall(
        './{prefix}entry/{prefix}{entry}'.format(prefix=arxiv_prefix, entry=entry))[0]
    return infos, xml_entry

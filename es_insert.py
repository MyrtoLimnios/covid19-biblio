import pandas as pd
from utils import read_json, connect_gs, es_write_dataframe, load_gsheet

config = read_json("config.json")
gsheet_name = config["gsheet_name"]
elasticsearchServer = config["elasticsearchServer"]


def clean(dataframe):
    dataframe['Date of publication'] = pd.to_datetime(
        dataframe['Date of publication'] + '/2020', format="%m/%d/%Y", errors='coerce')

    code_available_mask = ((dataframe['Code available'] != 'no') & (
        dataframe['Code available'] != ''))
    dataframe.loc[code_available_mask, 'bool_code_available'] = True
    dataframe['bool_code_available'] = dataframe['bool_code_available'].fillna(
        False)
    dataframe.loc[code_available_mask, 'str_code_available'] = 'Yes'
    dataframe['str_code_available'] = dataframe['str_code_available'].fillna(
        'No')
    return dataframe


if __name__ == '__main__':

    dataframe = load_gsheet(name=gsheet_name,
                            credentials='credentials.json')
    dataframe = clean(dataframe)
    print(dataframe.head(5))
    responses = es_write_dataframe(
        dataframe, host=elasticsearchServer, index='catalog')

    if False:
        print(responses)

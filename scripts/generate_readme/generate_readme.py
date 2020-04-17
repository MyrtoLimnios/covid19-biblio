# -*- coding: UTF-8
import pandas as pd
# import sys
# sys.path.append('../utils/')


GG_SPREADSHEET = "https://docs.google.com/spreadsheets/d/1WWIOWnuJuOKKNQA71qgxs7IVHtYL7ROKm7m7LwGY3gU"
GG_SPREADSHEET_NAME = GG_SPREADSHEET + "/export?format=csv&id=KEY&gid=0"
KIBANA = "http://54.72.238.242/app/kibana#/dashboard/f3a4f480-80a3-11ea-b4c0-d1a4270d43fe"

def load_gsheet(path):
    return pd.read_csv(path).fillna('null')


def add_h2_title(fd, text):
    print(text.encode('utf-8'))
    fd.write(u' '.join(('##', text, '\n')))


def add_h1_title(fd, text):
    print(text.encode('utf-8'))
    fd.write(u' '.join(('#', text, '\n')))


def add_general_information(fd):
    fd.write(u''.join(('###', ' General information', '\n')))


def add_technical_information(fd):
    fd.write(u''.join(('###', ' Technical information', '\n')))


def add_model_information(fd):
    fd.write(u''.join(('####', ' Model information', '\n')))


def add_estimation_information(fd):
    fd.write(u''.join(('####', ' Estimation information', '\n')))


def add_additional_information(fd):
    fd.write(u''.join(('####', ' Additional information', '\n')))


def add_authors(fd, text):
    #print(text.encode('utf-8'))
    fd.write(u''.join(('**Authors** : ', text.encode('utf-8').decode('utf-8'), '</br>', '\n')))


def add_publication_date(fd, text):
    #print(text.encode('utf-8'))
    fd.write(u''.join(('**Publication date** : ', text.encode('utf-8').decode('utf-8'), '</br>', '\n')))


def add_paper_link(fd, text):
    #print(text.encode('utf-8'))
    fd.write(u''.join(('**Paper** : Available [here](', text.encode('utf-8').decode('utf-8'), ')</br>', '\n')))


def add_code_available(fd, text):
    #print(text.encode('utf-8'))
    fd.write(u''.join(('**Code available** : ', text.encode('utf-8').decode('utf-8'), '</br>', '\n')))


def add_category_of_model(fd, text):
    #print(text.encode('utf-8'))
    fd.write(u''.join(('**Model category** : ', text.encode('utf-8').decode('utf-8'), '</br>', '\n')))


def add_sub_category_of_model(fd, text):
    form = '''<details>
	<summary> <b>Model sub-category</b> </summary>''' + text.encode('utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_data_used_for_the_model(fd, text):
    form = '''<details><summary> <b>Data used for the model</b> </summary>''' + text.encode('utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))

def add_global_approach(fd, text):
    form = '''<details><summary> <b>Global approach</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_outputs(fd, text):
    form = '''<details><summary> <b>Outputs</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_intervention_strategies(fd, text):
    form = '''<details><summary> <b>How intervention strategies are modelled</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_objective_function(fd, text):
    form = '''<details><summary> <b>Objective function</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_algo_type(fd, text):
    form = '''<details><summary> <b>Type of algorithm or method</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_epidemio_parameters(fd, text):
    form = '''<details><summary> <b>Epidemio parameters</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_other_parameters(fd, text):
    form = '''<details><summary> <b>Other parameters</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_input_estimation(fd, text):
    form = '''<details><summary> <b>How input parameters are estimated</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_additional_assumptions(fd, text):
    form = '''<details><summary> <b>Additional Assumptions</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_comments(fd, text):
    form = '''<details><summary> <b>Comment/issues</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details></br>'''
    fd.write(u''.join((form, '\n', '\n')))


def get_href(title):
    return '#' + title.lower().replace('(', '').replace(')', '').replace(':', '').replace(',', '').replace("'", '').replace(' ', '-')

# def add_table(fd, titles, authors):
#     fd.write(u''.join(('| <div style="width:400px">Title<div> | Author(s) |', '\n')))
#     fd.write(u'| --- | --- |\n')
#     for i in range(len(titles)):
#         fd.write(u''.join(('| <a href=', get_href(titles[i]) + '>' + titles[i] + '</a> | ' +  authors[i] + ' |', '\n')))


def add_table(fd, titles):
    fd.write(u''.join(('| Title | Description |', '\n')))
    fd.write(u'| --- | --- |\n')
    for i in range(len(titles)):
        fd.write(u''.join(('| ' + titles[i] + ' | [here](' + get_href(titles[i]) + ') |', '\n')))


if __name__ == '__main__':

    # Load data
    df = load_gsheet(GG_SPREADSHEET_NAME)

    # Open target file
    myfile = open("../../README.md", "w")

    add_h1_title(myfile, 'What is it ?')
    myfile.write(u'We host here a bibliography of papers related to COVID19 outbreak.\n')

    add_h1_title(myfile, 'Who are we ?')
    myfile.write(u'We are a group a researchers working with [Centre Borelli](https://ens-paris-saclay.fr/recherche/laboratoires-et-instituts/centre-borelli) at ENS Paris Saclay.\n')

    add_h1_title(myfile, 'Raw data')
    myfile.write(u'The raw data displayed here is available [here](' + GG_SPREADSHEET + ')\n')

    add_h1_title(myfile, 'How to contribute')
    myfile.write(u'In order to add an entry to this bibliography please comment on the [spreadsheet](' + GG_SPREADSHEET + ') and we will process it ! \n')

    add_h1_title(myfile, 'Also available with Kibana')
    myfile.write(u'If you wish to browse all the information embedded into the bibliography with a more powerful search engine and some nice dashboard, please use our [Kibana](' + KIBANA + ')\n\n')

    add_h1_title(myfile, 'The bibliography')

    # add_table(myfile, df['Paper(s)'], df['Authors'])
    add_table(myfile, df['Paper(s)'])

    for index, row in df.iterrows():
        if row['Paper(s)'].encode('utf-8') != b'null':
            add_h2_title(myfile, row['Paper(s)'])
            # General info
            add_general_information(myfile)
            add_authors(myfile, row['Authors'])
            add_publication_date(myfile, row['Date of publication'])
            add_paper_link(myfile, row['Link/source'])
            add_code_available(myfile, row['Code available'])
            # technical information
            add_technical_information(myfile)
            # Model information
            add_model_information(myfile)
            add_category_of_model(myfile, row['Category of model'])
            add_sub_category_of_model(myfile, row['Subcategory of model'])
            if row['Data used for the model (e.g. historical or simulated)'] != 'null':
                add_data_used_for_the_model(myfile, row['Data used for the model (e.g. historical or simulated)'])
            if row['Global approach'] != 'null':
                add_global_approach(myfile, row['Global approach'])
            if row['Outputs'] != 'null':
                add_outputs(myfile, row['Outputs'])
            if row['How intervention strategies are modelled'] != 'null':
                add_intervention_strategies(myfile, row['How intervention strategies are modelled'])
            if row['Additional Assumptions'] != 'null':
                add_additional_assumptions(myfile, row['Additional Assumptions'])
            # Estimation
            add_estimation_information(myfile)
            if (row["Objective function (write 'not explained' if the case)"] != 'null' and row["Objective function (write 'not explained' if the case)"] != 'not explained' ):
                add_objective_function(myfile, row["Objective function (write 'not explained' if the case)"])
            if (row["Type of algorithm or method used (write 'not explained' if the case)"] != 'null' and row["Type of algorithm or method used (write 'not explained' if the case)"] != 'not explained'):
                add_algo_type(myfile, row["Type of algorithm or method used (write 'not explained' if the case)"])
            if row['Epidemio parameters (induced by the model and/or inherent of the virus: infection,reco,death rates)'] != 'null':
                add_epidemio_parameters(myfile, row['Epidemio parameters (induced by the model and/or inherent of the virus: infection,reco,death rates)'])
            if row['Other parameters'] != 'null':
                add_other_parameters(myfile, row['Other parameters'])
            if row['How input parameters are estimated (data-driven or from litterature)'] != 'null':
                add_input_estimation(myfile, row['How input parameters are estimated (data-driven or from litterature)'])
            # Additional
            add_additional_information(myfile)
            if row['Comment/issues'] != 'null':
                add_comments(myfile, row['Comment/issues'])

    myfile.close()



# https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20#9942822
# https://medium.com/better-programming/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686

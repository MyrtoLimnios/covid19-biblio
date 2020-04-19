# -*- coding: UTF-8
import pandas as pd
# import sys
# sys.path.append('../utils/')


GG_SPREADSHEET = "https://docs.google.com/spreadsheets/d/1WWIOWnuJuOKKNQA71qgxs7IVHtYL7ROKm7m7LwGY3gU"
GG_SPREADSHEET_NAME = GG_SPREADSHEET + "/export?format=csv&id=KEY&gid=0"
GG_SPREADSHEET_COLUMNS = '/edit#gid=348695068'
GG_SPREADSHEET_GLOSSARY = '/edit#gid=1452418079'
KIBANA = "http://orvet.pppcmla.ens-cachan.fr:443/app/kibana#/dashboard/66e9a680-8229-11ea-b3e0-13021bdba55f"

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
    form = '''<details><summary> <b>Model sub-category</b> </summary>''' + text.encode('utf-8').decode('utf-8') + '''</details>'''
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


def add_problem_formulation(fd, text):
    form = '''<details><summary> <b>Problem Formulation</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_solving_method(fd, text):
    form = '''<details><summary> <b>Solving Method</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_epidemiological_parameters(fd, text):
    form = '''<details><summary> <b>Epidemiological parameters</b> </summary>''' + text.encode(
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


def get_author(authors):
    authors_list = authors.split(',')[0]
    if len(authors_list) > 1:
        return authors.split(',')[0] + ' et al.'
    else:
        return authors.split(',')[0]

def add_table(fd, titles, authors):
    fd.write(u''.join(('| Title | Authors | Description |', '\n')))
    fd.write(u'| --- | --- | --- |\n')
    for i in range(len(titles)):
        fd.write(u''.join(('| ' + titles[i] + ' | ' + get_author(authors[i]) + ' | [here](' + get_href(titles[i]) + ') |', '\n')))


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
    myfile.write(u'\nThe meaning for each column can be found [here](' + GG_SPREADSHEET + GG_SPREADSHEET_COLUMNS + ')\n')
    myfile.write(u'\nA glossary can be found [here](' + GG_SPREADSHEET + GG_SPREADSHEET_GLOSSARY + ')\n')

    add_h1_title(myfile, 'How to contribute')
    myfile.write(u'In order to add an entry to this bibliography please comment on the [spreadsheet](' + GG_SPREADSHEET + ') and we will process it ! \n')

    add_h1_title(myfile, 'Also available with Kibana')
    myfile.write(u'If you wish to browse all the information embedded into the bibliography with a more powerful search engine and some nice dashboard, please use our [Kibana](' + KIBANA + ')\n\n')

    add_h1_title(myfile, 'The bibliography')

    add_table(myfile, df['Paper(s)'], df['Authors'])

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
            if (row["Problem Formulation (e.g. numerical scheme, objective function, etc.)"] != 'null' and row["Problem Formulation (e.g. numerical scheme, objective function, etc.)"] != 'not explained' ):
                add_problem_formulation(myfile, row["Problem Formulation (e.g. numerical scheme, objective function, etc.)"])
            if (row["Solving Method"] != 'null' and row["Solving Method"] != 'not explained'):
                add_solving_method(myfile, row["Solving Method"])
            if row['Epidemiological parameters (e.g. inherent of the virus: infection, recovery, death rates)'] != 'null':
                add_epidemiological_parameters(myfile, row['Epidemiological parameters (e.g. inherent of the virus: infection, recovery, death rates)'])
            if row['Other parameters'] != 'null':
                add_other_parameters(myfile, row['Other parameters'])
            if row['How input parameters are estimated (data-driven or from litterature)'] != 'null':
                add_input_estimation(myfile, row['How input parameters are estimated (data-driven or from litterature)'])
            # Additional
            add_additional_information(myfile)
            if row['Comment/issues'] != 'null':
                add_comments(myfile, row['Comment/issues'])

    myfile.close()



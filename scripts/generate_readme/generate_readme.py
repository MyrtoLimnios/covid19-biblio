# -*- coding: UTF-8
import pandas as pd
# import sys
# sys.path.append('../utils/')


GG_SPREADSHEET = "https://docs.google.com/spreadsheets/d/1WWIOWnuJuOKKNQA71qgxs7IVHtYL7ROKm7m7LwGY3gU"
GG_SPREADSHEET_NAME = GG_SPREADSHEET + "/export?format=csv&id=KEY&gid=0"
GG_SPREADSHEET_COLUMNS = '/edit#gid=1061863733'
GG_SPREADSHEET_GLOSSARY = '/edit#gid=693948220'
KIBANA = "http://covidreview.org/kibana"

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

def add_model_num(fd, num):
    text_num = "" + "First"*(num==1) + "Second"*(num==2) + "Third"*(num==3) + "Fourth"*(num==4)
    fd.write(u''.join(('###', ' '+text_num+' model', '\n')))


def add_model_information(fd):
    fd.write(u''.join(('####', ' Model information', '\n')))


def add_estimation_information(fd):
    fd.write(u''.join(('####', ' Estimation information', '\n')))

def add_parameters_information(fd):
    fd.write(u''.join(('####', ' Model parameters information', '\n')))

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


def add_stochastic_deterministic(fd, text):
    #print(text.encode('utf-8'))
    fd.write(u''.join(('**Deterministic or stochastic model** : ', text.encode('utf-8').decode('utf-8'), '</br>', '\n')))

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

def add_details_approach(fd, text):
    form = '''<details><summary> <b>Details of approach</b> </summary>''' + text.encode(
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
    form = '''<details><summary> <b>How parameters are estimated</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))
    
def add_details_input_estimation(fd, text):
    form = '''<details><summary> <b>Details on parameters estimation</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))
    
    
def add_additional_assumptions(fd, text):
    form = '''<details><summary> <b>Additional Assumptions</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))


def add_comments(fd, text):
    form = '''<details><summary> <b>Comment/issues</b> </summary>''' + text.encode(
        'utf-8').decode('utf-8') + '''</details>'''
    fd.write(u''.join((form, '\n', '\n')))

def add_space(fd):
    fd.write(u'</br>\n\n')

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

    add_h1_title(myfile, 'Repository of a selection of papers related to COVID-19 outbreak operated by Centre Borelli (ENS Paris-Saclay, CNRS, Université de Paris, SSA)')
    myfile.write(u'The repository prioritizes papers presenting mathematical models with practical impact, use of empirical data, strategy of containment policy, open and reproducible implementation of the model.\n\n')
    myfile.write(u'The repository compiles the key elements of each paper such as: type of model, main assumptions, input parameters, output of the model, open source implementation, etc. The complete table can be found under three different formats:\n\n')
    myfile.write(u"* Interactive dashboard-like table under [Kibana](https://covidreview.org/kibana)\n" +
                  "* A [spreadsheet](" + GG_SPREADSHEET + ") --> Comments are allowed \n" +
                  "* List with clickable entries below.\n\n")

    add_h1_title(myfile, 'Additional information')
    myfile.write(u'List of characteristics is provided for each paper : see [characteristics](' + GG_SPREADSHEET + GG_SPREADSHEET_COLUMNS + ') description\n\n')
    myfile.write(u'A [glossary](' + GG_SPREADSHEET + GG_SPREADSHEET_GLOSSARY + ') of technical terms is available. \n')

    add_h1_title(myfile, 'Provided by Centre Borelli (ENS Paris-Saclay, CNRS, Université de Paris, SSA)')
    myfile.write(u'Authors: Marie Garin, Myrto Limnios, Alice Nicolaï, Nicolas Vayatis\n\n')
    myfile.write(u'Contributors: Stephen Chick, Theodoros Evgeniou, Mathilde Fekom, Anton Ovchinnikov, Raphaël Porcher, Camille Pouchol\n\n')
    myfile.write(u'Credits for technical support: Olivier Boulant, Amir Dib, Christophe Labourdette.\n\n')

    add_h1_title(myfile, 'Contribution')
    myfile.write(u'If you wish to suggest an article to be added to the review, please contact us via email at <A href="mailto:centreborelli.repository@gmail.com">centreborelli.repository@gmail.com</A> and we will proceed with the new entry after an internal assessment.\n')

    add_h1_title(myfile, 'Contact us')
    myfile.write(u'Email: <A href="mailto:centreborelli.repository@gmail.com">centreborelli.repository@gmail.com</A>\n')

    add_h1_title(myfile, 'Terms of Use')
    myfile.write(u'This GitHub repository and its contents herein, copyright 2020 ENS Paris-Scalay, all rights reserved, is provided to the public strictly for educational and academic research purposes. The Website relies upon publicly available data from multiple sources, that do not always agree. The ENS Paris-Saclay hereby disclaims any and all representations and warranties with respect to the Website, including accuracy, fitness for use, and merchantability. Reliance on the Website for medical guidance or use of the Website in commerce is strictly prohibited.\n')


    models_dic = {}
    for unique_title in df["Paper(s)"].unique():
        models_dic[unique_title] = sorted(df[(df["Paper(s)"]==unique_title)].index)
        
    unique_index = [v[0] for k,v in models_dic.items()]
    df_unique = df.loc[unique_index].reset_index()

        

    add_h1_title(myfile, 'The review (%d articles in total)' %(df_unique.shape[0]))

    add_table(myfile, df_unique['Paper(s)'], df_unique['Authors'])

    for index, row in df.iterrows():

        is_alone = (len(models_dic[row["Paper(s)"]])==1)
        is_first_of_serie = not is_alone and (index==models_dic[row["Paper(s)"]][0])
        is_last_of_serie = not is_alone and (index==models_dic[row["Paper(s)"]][-1])

        if is_alone or is_first_of_serie:  
            
            if row['Paper(s)'].encode('utf-8') != b'null':
                add_h2_title(myfile, row['Paper(s)'])
                # General info
                add_general_information(myfile)
                add_authors(myfile, row['Authors'])
                add_publication_date(myfile, row['Date of publication'])
                add_paper_link(myfile, row['Link/source'])
    
        if is_first_of_serie:
            model_num = 1
            add_model_num(myfile, model_num)
                
        if not is_alone and not is_first_of_serie:
            
            model_num+=1
            add_model_num(myfile, model_num)


        add_code_available(myfile, row['Code available'])
        # technical information
        add_technical_information(myfile)
        # Model information
        add_model_information(myfile)

        if row['Stochastic vs. Deterministic'] != 'null':
            add_stochastic_deterministic(myfile, row['Stochastic vs. Deterministic'])
        if row['Category of model'] != 'null':
            add_category_of_model(myfile, row['Category of model'])
        
        if row['Subcategory of model'] != 'null':
            add_sub_category_of_model(myfile, row['Subcategory of model'])
        if row['Data used for the model (e.g. historical or simulated)'] != 'null':
            add_data_used_for_the_model(myfile, row['Data used for the model (e.g. historical or simulated)'])
        if row['Global approach'] != 'null':
            add_global_approach(myfile, row['Global approach'])            
        if row['Details of approach'] != 'null':
            add_details_approach(myfile, row['Details of approach'])
        if row['Outputs'] != 'null':
            add_outputs(myfile, row['Outputs'])
        if row['How intervention strategies are modelled'] != 'null':
            add_intervention_strategies(myfile, row['How intervention strategies are modelled'])
        if row['Additional Assumptions'] != 'null':
            add_additional_assumptions(myfile, row['Additional Assumptions'])

        if (row["Problem Formulation (eg numerical scheme, objective function, etc.)"] != 'null' and row["Problem Formulation (eg numerical scheme, objective function, etc.)"] != 'not explained' ):
            add_problem_formulation(myfile, row["Problem Formulation (eg numerical scheme, objective function, etc.)"])
        if (row["Solving Method"] != 'null' and row["Solving Method"] != 'not explained'):
            add_solving_method(myfile, row["Solving Method"])
            
        # Estimation
        add_parameters_information(myfile)

        if row['Epidemiological parameters (eg inherent of the virus: infection, recovery, death rates)'] != 'null':
            add_epidemiological_parameters(myfile, row['Epidemiological parameters (eg inherent of the virus: infection, recovery, death rates)'])
        if row['Other parameters'] != 'null':
            add_other_parameters(myfile, row['Other parameters'])

        if row['How input parameters are estimated (data-driven or from literature)'] != 'null':
            add_input_estimation(myfile, row['How input parameters are estimated (data-driven or from literature)'])
        if row['Details on parameters estimation'] != 'null':
            add_details_input_estimation(myfile, row['Details on parameters estimation'])
        # Additional
        if row['Comment/issues'] != 'null':
            add_additional_information(myfile)
        if row['Comment/issues'] != 'null':
            add_comments(myfile, row['Comment/issues'])
            
        if is_alone or is_last_of_serie:
            add_space(myfile)

    myfile.close()

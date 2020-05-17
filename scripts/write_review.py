import pandas

from stats import count_occurrences

import scholarly

def maths_formatting(string, list_maths_terms):
    
    for term in list_maths_terms:
        string = string.replace(term, '& '+ term + ' &')

    return string

if __name__=="__main__":


        
    GG_SPREADSHEET = "https://docs.google.com/spreadsheets/d/1WWIOWnuJuOKKNQA71qgxs7IVHtYL7ROKm7m7LwGY3gU"
    GG_SPREADSHEET_NAME = GG_SPREADSHEET + "/export?format=csv&id=KEY&gid=0"
    table = pandas.read_csv(GG_SPREADSHEET_NAME).fillna('')

    categories = count_occurrences(table, 'Category of model')
    
    list_categories = ['compartmental','agent-based']
    
    list_maths_terms = ['\sim']


    for i, categ in enumerate(list_categories):
        
        rows_categ = (table['Category of model']==categ)
        table_categ = table[rows_categ]
        
        columns = ['Authors', 'Paper(s)', 'Stochastic vs. Deterministic', 'Category of model', 'Subcategory of model']
        headers = ['Author', 'Article', 'Stochastic or deterministic', 'Model category', 'Model']
        col_width = [5,5,3,3,3]
        column_format = ["p{"+str(col_width[i])+"cm}" for i in range(len(columns))]

        
        with open('table_'+categ+'.tex','w') as f:
            
            f.write("\\begin{landscape}\n\n")

            f.write("\\begin{tabular}{|"+"|".join(column_format)+"|}\n\n")

            f.write("\\toprule\n\n")

            f.write(" & ".join([str(x) for x in headers]) + " \\\\\n")
            for i, row in table_categ[columns].iterrows():
                f.write("\\midrule\n")
                f.write(" & ".join([maths_formatting(str(x), list_maths_terms) for x in row.values]) + " \\\\\n")

            f.write("\\bottomrule \n\n")


            f.write("\\end{tabular}\n\n")

            f.write("\\end{landscape}")
        

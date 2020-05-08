

import numpy as np
import pandas
from collections import Counter




def count_occurrences(gsheet, name_col, separator=';', delete_empty=True, count_filled=False, date=False, percent=True, combination=False, not_filled_value=''):
    
    # Clean rows not filled yet
    if delete_empty:
        gsheet = clean_empty(gsheet)
    
    rows = clean_col(gsheet, name_col, separator, count_filled, date, not_filled_value)
    
    if combination==True:
        rows = rows.apply(lambda s: sorted(s))
        rows = rows.apply(lambda s: [';'.join(s)])
    
    # Concatenate all values
    all_values = sum(rows, [])

    counts = Counter(all_values)
    
    # Nb filled lines
    n = len(gsheet)
    
    if percent:
        counts = {k:100*(v/n) for k, v in counts.items()}
    
    return counts


def clean_col(gsheet, name_col, separator=';', count_filled=False, date=False, not_filled_value=''):

    rows = gsheet[name_col]
    
    # If column of date, keep only month
    if date:
        rows = rows.apply(lambda s: s.split("/")[0])
        
    # Check only if filled cell
    if count_filled:
        rows = rows.apply(lambda s: 'not filled' if s==not_filled_value else 'filled')

    # Split with separator
    rows = rows.str.split(separator)

    # Remove blank spaces after separator"
    rows = rows.apply(lambda x: [s.lstrip() for s in x])
    
    return rows

def clean_empty(gsheet):
    to_keep = (gsheet.apply(lambda x: sum([1 for s in list(x[5:]) if s!='']), axis = 1)>=2)
    gsheet = gsheet[to_keep]
    return gsheet


if __name__=="__main__":
    
        
    GG_SPREADSHEET = "https://docs.google.com/spreadsheets/d/1WWIOWnuJuOKKNQA71qgxs7IVHtYL7ROKm7m7LwGY3gU"
    GG_SPREADSHEET_NAME = GG_SPREADSHEET + "/export?format=csv&id=KEY&gid=0"
    
    gsheet = pandas.read_csv(GG_SPREADSHEET_NAME).fillna('')

    approach = count_occurrences(gsheet, 'Global approach')
    deterministic_sto = count_occurrences(gsheet, 'Stochastic vs. Deterministic')
    categories = count_occurrences(gsheet, 'Category of model')
    subcategories = count_occurrences(gsheet, 'Subcategory of model')
    code = count_occurrences(gsheet, 'Code available', count_filled=True, not_filled_value='No')

    strategies = count_occurrences(gsheet, 'Subcategory of model', count_filled=True)

    parameters_estimation = count_occurrences(gsheet, 'How input parameters are estimated (data-driven or from litterature)',
                                              combination=True)

    dates = count_occurrences(gsheet, 'Date of publication', date=True)

    data = count_occurrences(gsheet, 'Data used for the model (e.g. historical or simulated)')


"""
Simple script to pull a table from a webpage. Will require some tweaking depending on how the webpage is set up.
Perhaps in the future I will work to make a more generalized version that will auto-identify headers and rows and such
no matter how the table is set up.

Author: Ethan Purnell
Date: 12/19/22
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Insert url of page containing desired table and desired output excel sheet name
url = ''
fname = ''


def extract_html_table(url, fname):
    """
    Function to extract HTML tables from websites. Print statements are included (but commented out) at points where
    you may want to check the code output as it goes.
    :param url:
    :param fname:
    :return:
    """
    # Create page object
    page = requests.get(url)

    # Read with beautiful soup
    soup = bs(page.text, 'lxml')

    # Extract table
    table = soup.find('table')
    # print(table)

    # Get column headers
    cols = []
    for i in table.find_all('td'):
        colname = i.text
        cols.append(colname)

    # Nothing unique to headers, grab them from list, won't always be the case
    cols = cols[:3]
    # print(cols)

    # Create dataframe
    df = pd.DataFrame(columns=cols)

    # Populate with data
    for i in table.find_all('tr')[1:]:
        row_data = i.find_all('td')
        row = [i.text for i in row_data]
        # print(row)
        length = len(df)
        df.loc[length] = row

    # Insert desired file name to save as Excel sheet
    df.to_excel(fname, index=False)

    return df


data = extract_html_table(url, fname)

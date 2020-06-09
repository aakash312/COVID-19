'''
The purpose of this code is to pull data from COVID tracking project APIs, cleaning and processing it and finally exporting into
a csv file for visualization purposes.
'''

from urllib.request import urlopen
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



api_urls = {'key1':'https://covidtracking.com/api/v1/us/daily.json','key2':'https://covidtracking.com/api/v1/states/current.json'}
df1= pd.read_json("D:\Python Outputs\data.v.1.json")
df2= pd.read_json("D:\Python Outputs\data.v.2.json")

def apiData(api_urls,df1,df2):
    try:
            for val1,val2 in api_urls.items():
                    if val1 == 'key1':
                         print('The json file generated will have the data from this URL: {}' .format(val2))
                         json_obj1= urlopen(val2)
                         data1= json.load(json_obj1)
                         json_object1 = json.dumps(data1, indent = 4)
                         with open("D:\Python Outputs\data.v.1.json" , "w") as outfile1:
                                outfile1.write(json_object1)
                         df1.to_csv("D:\Python Outputs\API_us_daily.csv")
                    else:
                        print('The json file generated will have the data from this URL: {}' .format(val2))
                        json_obj2= urlopen(val2)
                        data2= json.load(json_obj2)
                        json_object2 = json.dumps(data2, indent = 4)
                        with open("D:\Python Outputs\data.v.2.json" , "w") as outfile2:
                            outfile2.write(json_object2)
                        df2.to_csv("D:\Python Outputs\API_state_current.csv")
                        print("\n")
            print("Function Excecuted Successfully, JSON files and CSV file for US daily and State Current have been generated\n")
    except:
      print("Error in apiData Function")

def dataExploration(df1,df2):
        print('The information about the daily US cases dataset is as follows:')
        print(df1.info())
        print('The information about the daily state cases dataset is as follows:')
        print(df2.info())

def stateData(df2):
    try:
           print("State Current Testing Data- \n")
           total_positive_state = df2['positive'].sum()
           print('Total positive cases in all the states currently are :{} '.format(total_positive_state))
           total_negative_state = df2['negative'].sum()
           print('Total negative cases in all the states currently are :{} '.format(total_negative_state))
           total_pending_state = df2['pending'].sum()
           print('Total pending cases in all the states currently are :{} \n'.format(total_pending_state))

           print("State Current Outcome Data- \n")
           total_recovered_state = df2['recovered'].sum()
           print('Total recovered cases in all the states currently are :{} '.format(total_recovered_state))
           total_death_state = df2['death'].sum()
           print('Total death cases in all the states currently are :{} '.format(total_death_state))

           print("State Total Test Results Data- \n")
           total_tests_state = total_positive_state+ total_negative_state
           print('Total tests done in all the states are : {} '.format(total_tests_state))
    except:
        print('Error in stateData Function')

def stateViz(df2):
    x = df2.loc[:,'state'].values
    y = df2.loc[:,'total'].values
    plt.bar(x, y, label = 'Total Cases/ State', align='center')
    plt.xticks(x, rotation=90)
    plt.show()
if __name__ =="__main__":
    apiData(api_urls,df1,df2)
    # dataExploration(df1,df2)
    stateData(df2)
    stateViz(df2)

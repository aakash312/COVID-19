'''
The purpose of this code is to pull data from COVID tracking project APIs, cleaning and processing it and finally exporting into
a csv file for visualization purposes.
'''

from urllib.request import urlopen
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

date_current = date.today()
api_urls = {'key1':'https://covidtracking.com/api/v1/us/daily.json','key2':'https://covidtracking.com/api/v1/states/current.json'}
df1= pd.read_json("D:\Python Outputs\data.v.1.json")
df2= pd.read_json("D:\Python Outputs\data.v.2.json")

def apiData(api_urls,df1,df2):
    '''
    This function will take the api_urls dictionary as a input and generate a json file with all the API data and later convert
    the json file into csv format which can is more readable as compared to json file
    '''
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
                        # print("\n")
            print("Function Excecuted Successfully, JSON files and CSV file for US daily and State Current have been generated\n")
    except:
             print("Error in apiData Function")

def dataExploration(df1,df2):
        '''
        This function will take the df1 and df2 as input and provide some basic information about the data type of different columns
        and also top 5 rows of both the dataframes
        '''
        print('The information about the daily US cases dataset is as follows:')
        print(df1.info())
        print(df1.head())
        print('The information about the daily state cases dataset is as follows:')
        print(df2.info())
        print(df2.head())

def stateData(df2,date_current):
    '''
    This function will take in the df2 i.e. the dataframe with the state daily data and also date_current variable which will
    be use to print out the date in the output. The goal of this function is to do some aggregation of values and show the total positive, negative, recovered and
    death cases
    '''
    try:
           print("State Current Testing Data- \n")
           total_positive_state = df2['positive'].sum()
           print('Total positive cases in all the states on {} are :{} ' .format(date_current,total_positive_state))
           total_negative_state = df2['negative'].sum()
           print('Total negative cases in all the states on {} are :{} '.format(date_current, total_negative_state))
           total_pending_state = df2['pending'].sum()
           print('Total pending cases in all the states on {} are :{} \n'.format(date_current,total_pending_state))
            ##
           print("State Current Outcome Data- ")
           total_recovered_state = df2['recovered'].sum()
           print('Total recovered cases in all the states on {} are :{} '.format(date_current,total_recovered_state))
           total_death_state = df2['death'].sum()
           print('Total death cases in all the states on {} are :{} \n'.format(date_current,total_death_state))
            ##
           print("State Total Test Results Data- ")
           total_tests_state = total_positive_state+ total_negative_state
           print('Total tests done in all the states are : {} '.format(total_tests_state))
    except:
        print('Error in stateData Function')

def usDate(df1):
    '''

    '''
    try:
        pass
    except:
        pass

def usViz(df1):
    '''

    '''
    try:
        pass
    except:
        pass



def stateViz(df2,date_current):
    '''
    This function is used for visualization purposes
    '''
    try:
            x1=df2.nlargest(10, ['positive'])
            x = x1.loc[:,'positive'].values
            y = x1.loc[:,'state'].values
            plt.pie(x,labels=y,autopct='%1.1f%%')
            # plt.legend(y, loc="right")
            plt.title("Top 10 states that are most affected by COVID-19 are ")
            plt.savefig('D:\Python Outputs\Top10most.pdf')
            # plt.show()

            x3=df2.nsmallest(5, ['positive'])
            a = x3.loc[:,'positive'].values
            b = x3.loc[:,'state'].values
            plt.pie(a,labels=b,autopct='%1.1f%%')
            # plt.legend(b, loc="right")
            plt.title("Top 10 states that are least affected by COVID-19 are ")
            plt.savefig('D:\Python Outputs\Top10least.pdf')
            # plt.show()

            font = {'size': 65}
            plt.rc('font', **font)
            plt.rcParams["figure.figsize"]=60,40
            df2.plot(kind = 'bar', x = 'state', y = 'positive', color = 'blue')
            plt.title("State wise positive cases on {}" .format(date_current))
            plt.savefig('D:\Python Outputs\positive.pdf')
            # plt.show()

            df2.plot(kind = 'bar', x = 'state', y = 'negative', color = 'red')
            plt.title("State wise negative cases on {}" .format(date_current))
            plt.savefig('D:\Python Outputs\ negative.pdf')
            # plt.show()

            df2.plot(kind = 'bar', x = 'state', y = 'death', color = 'black')
            plt.title("State wise deaths cases on {}" .format(date_current))
            plt.savefig('D:\Python Outputs\deaths.pdf')
            # plt.show()

    except:
        print('stateViz function failed to execute')


if __name__ =="__main__":
    # apiData(api_urls,df1,df2)
    # # dataExploration(df1,df2)
    # stateData(df2,date_current)
    stateViz(df2,date_current)

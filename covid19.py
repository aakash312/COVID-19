'''
The purpose of this python script is to pull data from COVID tracking project APIs then exploring, processing the data and finally creating
visualizations to be saved in form of PDF files so that the daily state wise and country wise progress can be tracked.
'''

from urllib.request import urlopen
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

class covid19:

    date_current = date.today()

    def __init__(self,df1,df2,api_urls):
        self.df1= df1
        self.df2=df2
        self.api_urls= api_urls

    def apiData(self):
        '''
            This function will take the api_urls dictionary as a input and generate a json file with all the API data and later convert
            the json file into csv format which can is more readable as compared to json file
        '''
        try:
            for val1, val2 in self.api_urls.items():
                if val1 == 'key1':
                    # print('The json file generated will have the data from this URL: {}'.format(val2))
                    json_obj1 = urlopen(val2)
                    data1 = json.load(json_obj1)
                    json_object1 = json.dumps(data1, indent=4)
                    with open("D:\Python Outputs\API_US_Data.json",'w') as outfile1:
                        outfile1.write(json_object1)

                    self.df1.to_csv("D:\Python Outputs\ {}_API_US_Daily.csv".format(covid19.date_current))
                else:
                    # print('The json file generated will have the data from this URL: {}\n'.format(val2))
                    json_obj2 = urlopen(val2)
                    data2 = json.load(json_obj2)
                    json_object2 = json.dumps(data2, indent=4)
                    with open("D:\Python Outputs\API_State_Data.json", "w") as outfile2:
                        outfile2.write(json_object2)

                    self.df2.to_csv("D:\Python Outputs\ {}_API_State_Current.csv".format(covid19.date_current))
            print("apiData Function Executed Successfully\n")
        except:
            print("Error in apiData Function")

    def dataExploration(self):
        '''
            This function will take the df1 and df2 as input and provide some basic information about the data type of different columns
            and also top 5 rows of both the dataframes
        '''
        try:
            print('The information about the daily US cases dataset is as follows:')
            # print(self.df1.info())
            print(self.df1.head())
            print('The information about the daily state cases dataset is as follows:')
            # print(self.df2.info())
            print(self.df2.head())
            print('dataExploration Function Executed Successfully')
        except:
            print("Error in dataExploration Function")

    def stateData(self):
        '''
            This function will take in the df2 i.e. the dataframe with the state daily data and also date_current variable which will
            be use to print out the date in the output. The goal of this function is to do some aggregation of values and show the total positive, negative, recovered and
            death cases
        '''
        try:
            print("State Current Testing Data- \n")
            total_positive_state = self.df2['positive'].sum()
            print('Total positive cases in all the states on {} are :{} '.format(covid19.date_current, total_positive_state))
            total_negative_state = self.df2['negative'].sum()
            print('Total negative cases in all the states on {} are :{} '.format(covid19.date_current, total_negative_state))
            total_pending_state = self.df2['pending'].sum()
            print('Total pending cases in all the states on {} are :{} \n'.format(covid19.date_current, total_pending_state))
            ##
            print("State Current Outcome Data- ")
            total_recovered_state = self.df2['recovered'].sum()
            print('Total recovered cases in all the states on {} are :{} '.format(covid19.date_current, total_recovered_state))
            total_death_state = self.df2['death'].sum()
            print('Total death cases in all the states on {} are :{} \n'.format(covid19.date_current, total_death_state))
            ##
            print("State Total Test Results Data- ")
            total_tests_state = total_positive_state + total_negative_state
            print('Total tests done in all the states on {} are : {}'.format(covid19.date_current,total_tests_state))
            print('stateData Function Executed Successfully\n')
        except:
            print('Error in stateData Function')

    def usData(self):
        '''
            This function will take in the df1 i.e. the dataframe with the US daily data and also date_current variable which will
            be use to print out the date in the output. The goal of this function is to do some aggregation of values and show the total test related stats
        '''
        try:
            print("US Current Testing Data- \n")
            total_death_us = self.df1['death'].max()
            print('Total death cases in all the states on {} are :{} '.format(covid19.date_current, total_death_us))
            total_positive_us = self.df1['positive'].max()
            print('Total positive cases in all the states on {} are :{} '.format(covid19.date_current, total_positive_us))
            total_negative_us = self.df1['negative'].max()
            print('Total negative cases in all the states on {} are :{} '.format(covid19.date_current, total_negative_us))
            total_tests_us = total_negative_us + total_positive_us
            print('Total tests in all the states on {} are :{} \n'.format(covid19.date_current, total_tests_us))
            print('usData Function Executed Successfully\n')
        except:
            print('Error in usData Function')

    def stateViz(self):
        '''
            This function takes df2 i.e. the current state data as input along with current date and generates PDF files with related visualizations
        '''
        try:
            x1 = self.df2.nlargest(10, ['positive'])
            x = x1.loc[:, 'positive'].values
            y = x1.loc[:, 'state'].values
            plt.pie(x, labels=y, autopct='%1.1f%%')
            # plt.legend(y, loc="right")
            plt.title("Top 10 states that are most affected by COVID-19 are ")
            plt.savefig('D:\Python Outputs\{}_Top_Most_Affected_State.pdf'.format(covid19.date_current))
            # plt.show()

            x3 = self.df2.nsmallest(5, ['positive'])
            a = x3.loc[:, 'positive'].values
            b = x3.loc[:, 'state'].values
            plt.pie(a, labels=b, autopct='%1.1f%%')
            # plt.legend(b, loc="right")
            plt.title("Top 10 states that are least affected by COVID-19 are ")
            plt.savefig('D:\Python Outputs\{}_Top_Least_Affected_State.pdf'.format(covid19.date_current))
            # plt.show()

            font = {'size': 65}
            plt.rc('font', **font)
            plt.rcParams["figure.figsize"] = 60, 40
            self.df2.plot(kind='bar', x='state', y='positive', color='blue')
            plt.title("State wise positive cases on {}".format(covid19.date_current))
            plt.savefig('D:\Python Outputs\{}_Positive_State.pdf'.format(covid19.date_current))
            # plt.show()

            self.df2.plot(kind='bar', x='state', y='negative', color='red')
            plt.title("State wise negative cases on {}".format(covid19.date_current))
            plt.savefig('D:\Python Outputs\{}_Negative_State.pdf'.format(covid19.date_current))
            # plt.show()

            self.df2.plot(kind='bar', x='state', y='death', color='black')
            plt.title("State wise deaths cases on {}".format(covid19.date_current))
            plt.savefig('D:\Python Outputs\{}_Deaths_State.pdf'.format(covid19.date_current))
            # plt.show()
            print('stateViz Function Executed Successfully\n')

        except:
            print('Error in stateViz Function')

    def usViz(self):
        '''
        This function takes df1 i.e. the currrent US data as input along with current date and generates PDF files with related visualizations
        '''
        try:
            print('usViz Function Executed Successfully\n')
        except:
            print('Error in usViz Function')


if __name__ == "__main__":
    __covidViz__= covid19( df1 = pd.read_json("D:\Python Outputs\API_US_Data.json"),
                  df2 = pd.read_json("D:\Python Outputs\API_State_Data.json"),
                  api_urls = {'key1': 'https://covidtracking.com/api/v1/us/daily.json',
                              'key2': 'https://covidtracking.com/api/v1/states/current.json'})

    __covidViz__.apiData()
    __covidViz__.dataExploration()
    __covidViz__.stateData()
    __covidViz__.usData()
    __covidViz__.stateViz()
    __covidViz__.usViz()

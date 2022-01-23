from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.worldometers.info/coronavirus/#main_table'
req=requests.get(url)
content=req.text
soup=BeautifulSoup(content, "html.parser")
rows = soup.find_all('tr')
list = []
for row in rows:
    cols=row.find_all('td')
    row = [row.text for row in cols]
    list.append(row)
df=pd.DataFrame(list,columns=["Sr.no","Country","Total Cases","New Cases","Total Deaths","New Deaths","Total Recovered","New Recovered","Active Cases","Serious Cases","Total Cases/1M Pop","Death Cases/1M Pop","Total Tests","Tests/ 1M Pop","Population","16","17","18","19","20","21","22"])
df=df[["Sr.no","Country","Total Cases","New Cases","Total Deaths","New Deaths","Total Recovered","New Recovered","Active Cases","Serious Cases","Total Cases/1M Pop","Death Cases/1M Pop","Total Tests","Tests/ 1M Pop","Population"]]
df=df.drop_duplicates()
df= df.iloc[9:233]
col_name=['New Cases','New Deaths',"New Recovered"]
for val in col_name:
    df['{}'.format(val)] = df['{}'.format(val)].str.replace('+','', regex=True)
df.to_excel('test.xlsx', index=False)

#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[4]:


#input"03-19-2020"
#output"03-19-2020.csv"
#import requests
import pandas as pd

def get_covid_daily_data(input_date):
    csv_name = input_date + ".csv"
    github_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}".format(csv_name)
    #response = requests.get(github_url)
    df = pd.read_csv(github_url)
    # df.head()
    # df.tail()
    df.to_csv(csv_name, index=False)

user_input = input("Please input a date(mm-dd-yyyy):")
get_covid_daily_data(user_input)


# In[5]:


from datetime import date, timedelta

start_date = date(2020, 1, 22)
#time_delta = timedelta(57)
#end_date = start_date + time_delta
date_period = [start_date + timedelta(i) for i in range(58)]
data_dates = [i.strftime('%m-%d-%Y') for i in date_period]
for dt in data_dates:
    print("Downloading {}.csv...".format(dt))
    get_covid_daily_data(dt)


# In[6]:


56_cannot_die = '五六不能亡'


# In[8]:


cannot_56_die = '五六不能亡'
print(cannot_56_die)


# In[9]:


cannot_die_56 = '五六不能亡'
print(cannot_die_56)


# In[10]:


56_cannot_die = '五六不能亡'
print(56_cannot_die)


# In[ ]:





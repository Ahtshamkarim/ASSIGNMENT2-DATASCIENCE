#!/usr/bin/env python
# coding: utf-8

# In[55]:


# libraries that we use in whole analysi.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[56]:


# part1 to read file via pandas builtin function
df = pd.read_csv("data2.csv")


# In[57]:


# data frame of country
cn_df = df["Country Name"]


# In[69]:


# this is abstraction of countries we only make list of countries name without repitition

# list
countries = [ ]

# loop to check repitition of names 
for i in cn_df:
    if i not in countries:

#append in list
        countries.append(i)


# In[59]:


# this is method that use in whole file if we want to make list of dataset for more preicse analysis. 

def MakeList(args):
    lst = list()
    for i in args:
        lst.append(int(i))
    return lst

# dataset of years 
years_df = df.iloc[0:0,5:-1]

# converted to list
years = MakeList(years_df)


# In[60]:


# CO2 emissions from solid fuel consumption (% of total) in china
def co2EmissionChina():
                                    #only record of china extracted here with indicator co2 emission and fuel consumption
    
    df_china = df.loc[(df['Country Name'] == "China") & (df['Indicator Name'] == "CO2 emissions from solid fuel consumption (% of total)")]

                                    # extracting values and make array via builtin function of pandas     
    df_china_data = df_china.iloc[:,5:-1].values
    
                                    #removing nan spaces from array only use clean dataset
    df_china_data=df_china_data[np.logical_not(np.isnan(df_china_data))] 

    
                                    #converting to list for more precise analysis
    datalist = list(df_china_data)

                                    #setting of graphs or figure using matplotlib
    plt.figure(figsize=(8,6))
    plt.ylabel("increase in CO2 emission")
    plt.title("CO2 EMISSION IN CHINA")
    
                                    # use seaborn library for analysis on dataset using histogram   
    sb.histplot(datalist, bins=13, kde=True, color = "y")


# In[61]:


# CO2 emissions from solid fuel consumption (% of total) in spain
def co2EmissionSpain():
                                    #only record of china extracted here with indicator co2 emission and fuel consumption
    df_Spain = df.loc[(df['Country Name'] == "Spain") & (df['Indicator Name'] == "CO2 emissions from solid fuel consumption (% of total)")]

                                    # extracting values and make array via builtin function of pandas   
    df_Spain_data = df_Spain.iloc[:,5:-1].values
    
                                    #removing nan spaces from array only use clean dataset    
    df_Spain_data=df_Spain_data[np.logical_not(np.isnan(df_Spain_data))] 
    
                                    #converting to list for more precise analysis
    datalist = list(df_Spain_data)

                                    #setting of graphs or figure using matplotlib
    plt.figure(figsize=(8,6))
    plt.ylabel("increase in CO2 emission")
    plt.title("CO2 EMISSION IN SPAIN")

                                    #use seaborn library for analysis on dataset using histogram   
    sb.histplot(datalist, bins=11, kde=True, color = "r")


# In[62]:


# CO2 emissions from solid fuel consumption (% of total) in france
def co2EmissionFrance():
                                    #only record of china extracted here with indicator co2 emission and fuel consumption
    df_France = df.loc[(df['Country Name'] == "France") & (df['Indicator Name'] == "CO2 emissions from solid fuel consumption (% of total)")]

                                    # extracting values and make array via builtin function of pandas   
    df_France_data = df_France.iloc[:,5:-1].values
   
                                    # removing nan spaces from array only use clean dataset   
    df_France_data=df_France_data[np.logical_not(np.isnan(df_France_data))] 
    
                                    #converting to list for more precise analysis
    datalist = list(df_France_data)

                                    #SETTINGS OF GRAPHS
    plt.figure(figsize=(8,6))
    plt.ylabel("increase in CO2 emission")
    plt.title("CO2 EMISSION IN FRANCE")
    
    sb.histplot(datalist,bins=13 ,kde=True, color = "g")


# In[63]:


# comparison of all
def indicatorComparison():
                                #only record of france extracted here with indicator electricity from hydro and coal production
    df_France_coal = df.loc[(df['Country Name'] == "France") & (df['Indicator Name'] == "Electricity production from coal sources (% of total)")]

                                # extracting values and make array via builtin function of pandas   
    df_France_coal_data = df_France_coal.iloc[:,5:-1].values
    
                                #removing nan spaces from array only use clean dataset 
    df_France_coal_data=df_France_coal_data[np.logical_not(np.isnan(df_France_coal_data))] 
    
                                #converting to list for more precise analysis
    dlist_france_coal = list(df_France_coal_data)

    
    
                                #only record of france extracted here with indicator electricity from hydro and coal production
    df_France_hydro = df.loc[(df['Country Name'] == "France") & (df['Indicator Name'] == "Electricity production from hydroelectric sources (% of total)")]

                                # extracting values and make array via builtin function of pandas  
    df_France_hydro_data = df_France_hydro.iloc[:,5:-1].values
    
                                #removing nan spaces from array only use clean dataset 
    df_France_hydro_data=df_France_hydro_data[np.logical_not(np.isnan(df_France_hydro_data))] 

                                #converting to list for more precise analysis
    dlist_france_hydor = list(df_France_hydro_data)

    
                                #setting of graphs or figure using matplotlib
    plt.figure(figsize=(10,8))
    plt.ylabel("increase in electircity production")
    plt.title("ELECTRICITY PRODUCTION FROM COAL & HYDRO IN FRANCE")
    tick = np.arange(10,55,5)
    plt.yticks(tick)

                                #plotting on distplot
    sb.distplot(dlist_france_hydor, bins=20, kde = True)
    sb.distplot(dlist_france_coal,bins=8, kde = True)
    
    
    



# In[67]:


# main method
def main():
    
    co2EmissionChina()
    co2EmissionSpain()
    co2EmissionFrance()

    indicatorComparison()


# In[68]:


main()


# In[ ]:





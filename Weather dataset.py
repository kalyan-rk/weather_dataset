#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[8]:


data = pd.read_csv(r"C:\Users\ramavath kalyan\Downloads\1. Weather Data.csv")


# In[9]:


data 


# In[2]:


get_ipython().system('pip install nbconvert')


# In[10]:


data.head()


# In[11]:


data.shape


# In[12]:


data.index


# In[13]:


data.columns


# In[14]:


data.dtypes


# In[19]:


data['Weather'].unique()


# In[21]:


data.nunique()


# In[23]:


data.count()


# In[24]:


data['Weather'].value_counts()


# In[25]:


data.info()


# # 1)Find all the unique wind speed values in the data

# In[26]:


data.head(2)


# In[27]:


data.nunique()


# In[28]:


data['Wind Speed_km/h'].nunique()


# All unique values present in this colomn

# In[29]:


data['Wind Speed_km/h'].unique()


# # 2)Find the number of times when the Weather is exactly clear

# In[30]:


data.head(2)


# In[32]:


#value_counts()
data.Weather.value_counts()


# In[38]:


#filtering
#data.head(2)
#data.Weather == 'Clear' --> it shows boolean form
data[data.Weather == 'Clear']


# In[40]:


#groupby()
data.groupby('Weather').get_group('Clear')


# # 3) Find the number of times when the Wind speed was exactly 4kmph

# In[44]:


data.head(2)


# In[46]:


data[data['Wind Speed_km/h']==4]


# # 4) Find out the Null values in the data

# In[48]:


data.isnull().sum()


# In[49]:


data.notnull().sum()


# # 5) Rename the column name Weather of the dataframe to Weather condition

# In[50]:


data.head(2)


# In[53]:


data.rename(columns={'Weather': 'Weather condition'})
#only for temporary


# In[54]:


data.head(2)


# In[55]:


data.rename(columns={'Weather': 'Weather condition'}, inplace=True)
#permanent name change


# In[56]:


data.head(2)


# # 6) What is mean visibility?

# In[57]:


data.head(2)


# In[58]:


data.Visibility_km.mean()


# # 7) What is standard deviation of pressure in this data?

# In[59]:


data.Press_kPa.std()


# # What is the varience of Relative humidity?

# In[61]:


#we use [] if we have space in the naming
data['Rel Hum_%'].var()


# # 9) Find all the instances when snow was recorded

# In[64]:


#value_counts
#data.head(2)
data['Weather condition'].value_counts()


# In[65]:


#filtering
data[data['Weather condition']=='Snow']


# In[66]:


#str.contains
data[data['Weather condition'].str.contains('Snow')]


# # 10) Find all the instances when Widnd speed is above 24 and visibility is 25

# In[67]:


data.head(2)


# In[70]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)]


# # 11) What is the mean value of each colomn against each Weather condition?

# In[71]:


data.head(2)


# In[72]:


data.groupby('Weather condition').mean()


# # 12) What is the Min & Max value of each column against each Weather condition

# In[73]:


data.head(2)


# In[74]:


data.groupby('Weather condition').min()


# In[75]:


data.groupby('Weather condition').max()


# # 13) Show all the records where weather condition is fog

# In[78]:


data[data['Weather condition']=='Fog']


# # 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'

# In[83]:


data[(data['Weather condition']=='Clear') | (data['Visibility_km']>40)]


# # 15) Find all the instances when:

# Weather is clear and relative humidity >50
# or
# Visibility >40

# In[88]:


data[(data['Weather condition']=='Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)]


# In[ ]:





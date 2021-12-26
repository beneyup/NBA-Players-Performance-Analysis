#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[3]:


os.getcwd()


# In[17]:


#changing the working directory to read the csv file
os.chdir('/Users/e.agtepe/Desktop/data science')


# In[5]:


movies = pd.read_csv('P4-Dataset.csv')


# In[6]:


len(movies)


# In[7]:


movies.head()


# In[8]:


movies.columns


# In[18]:


#changing column names
movies.columns = ['DayofWeek', 'Director', 'Genre', 'MovieTitle', 'ReleaseDate', 'Studio', 'AdjustedGross(mill)',  
                  'Budget(mill)','Gross(mill)','IMDbRating','MovieLensRating','Overseas(mill)','Overseas(perc)',
                  'Profit(mill)','Profit(perc)','Runtime(min)', 'US(mill)','GrossUS(perc)']






# In[10]:


movies.head()


# In[11]:


movies.info()


# In[19]:


#changing the type of the columns to categoric variable
#if you get an attribute error you can change the types in excel.  
movies.DayofWeek = movies.DayofWeek.astype('category')
movies.Director  = movies.Director.astype('category')
movies.Genre     = movies.Genre.astype('category')
movies.MovieTitle = movies.MovieTitle.astype('category')
movies.ReleaseDate = movies.ReleaseDate.astype('category')
movies.Studio = movies.Studio.astype('category')


# In[13]:


#filtering the genre data 
genre_filters= ['action','comedy','adventure','animation','drama']
movies_2 = movies[movies.Genre.isin(genre_filters)]
print(movies_2)


# In[20]:


#filtering the studio data
studio_filters=['Buena Vista Studios','Sony','Universal','WB','Paramount Pictures','Fox']
movies_3 = movies_2[movies_2['Studio'].isin(studio_filters)]
print(movies_3)


# In[15]:


#rearranging the graph's size.
plt.rcParams['figure.figsize'] =19,10


# In[16]:


get_ipython().run_cell_magic('time', '', 'sns.set(style=\'darkgrid\', palette=\'muted\', color_codes= True)\n\nax = sns.boxplot(data=movies_3, x=\'Genre\', y=\'GrossUS(perc)\', orient = \'v\', color =\'lightgray\', showfliers = False)\nplt.setp(ax.artists, alpha=0.5)\n\nsns.stripplot(x="Genre", y="GrossUS(perc)", data=movies_3, jitter = True, hue=\'Studio\', size=6, linewidth = 0, alpha =0.7)\n\nax.axes.set_title(\'Domestic Gross % by Genre\',fontsize=30)\nax.set_xlabel(\'Genre\', fontsize = 30)\nax.set_ylabel(\'Gross % US\', fontsize = 20)\nax.legend(bbox_to_anchor = (1.05, 1), loc =2)\n')


# From the boxplot graph above, we only see the data from action, adventure, animation, comedy and drama genres. Also,  we only see dots that are representing Buena Vista Studios, Sony, Universal , WB, Paramount Pictures , Fox. We're able to change it by filtering the data from those columns.  

# The insights that we can draw from the graph are:
# 
# * Most studios have released movies of the action genre. This might be because the audience likes action movies more.
# 
# * Comedy movies' median, max. and min. points are higher than the others, which can be interpreted as comedy movies making more money.  
# 
# * Drama movies do not have that much attention from the 6 Studios that we filtered the data with. 
# 
# * Animation movies are doing better compared to adventure and drama movies.
# 
# * Adventure movies may be the least beneficial genre in financial terms in this group of genres, and its median and the min point are lower than the others. 
# 
# 
# 
# 
# 
# 

# In[ ]:





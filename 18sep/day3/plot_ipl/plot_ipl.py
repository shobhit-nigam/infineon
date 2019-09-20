#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt


# In[2]:


lista = [1, 2, 3]
listb = [4, 5, 2]


# In[3]:


plt.plot(lista, listb)
plt.show()


# In[4]:


lista = [1, 2, 3]
listb = [4, 5, 2]
plt.plot(lista, listb)
plt.title('survived third day')
plt.ylabel('energy')
plt.xlabel('copmlexity')
plt.show()


# In[6]:


lista = [1, 2, 3]
listb = [4, 5, 2]
listc = [2, 3, 6]
listd = [4, 6, 4]

plt.plot(lista, listb)
plt.plot(listc, listd)
plt.title('survived third day')
plt.ylabel('energy')
plt.xlabel('copmlexity')
plt.show()


# In[7]:


lista = [1, 2, 3]
listb = [4, 5, 2]
listc = [2, 3, 6]
listd = [4, 6, 4]

plt.plot(lista, listb, linewidth=4)
plt.plot(listc, listd)
plt.title('survived third day')
plt.ylabel('energy')
plt.xlabel('copmlexity')
plt.show()


# In[8]:


from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

lista = [1, 2, 3]
listb = [4, 5, 2]
listc = [2, 3, 6]
listd = [4, 6, 4]

plt.plot(lista, listb, linewidth=4)
plt.plot(listc, listd)
plt.title('survived third day')
plt.ylabel('energy')
plt.xlabel('copmlexity')
plt.show()


# In[11]:


from matplotlib import pyplot as plt
from matplotlib import style

lista = [1, 2, 3]
listb = [4, 5, 2]
listc = [2, 3, 6]
listd = [4, 6, 4]

plt.plot(lista, listb, color = 'green', label = 'line one', linewidth=4)
plt.plot(listc, listd, color = 'pink', label = 'line two', linewidth=5)
plt.title('survived third day')
plt.ylabel('energy')
plt.xlabel('copmlexity')
plt.legend()
plt.show()


# In[12]:


help(plt.plot)


# In[14]:


from matplotlib import pyplot as plt
from matplotlib import style

lista = [1, 2, 3]
listb = [4, 5, 2]
listc = [2, 3, 6]
listd = [4, 6, 4]

plt.plot(lista, listb, "go")
plt.plot(listc, listd, "r^")
plt.title('survived third day')
plt.ylabel('energy')
plt.xlabel('copmlexity')
plt.show()


# In[20]:


activity = ['movie', 'travel', 'housecleaning', 'sleep', 'shopping']
share = [4, 3, 3, 7, 5]
Explode = [0, 0, 0, 0.1, 0]
plt.pie(share, explode=Explode,labels=activity)
plt.show()


# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


matches = pd.read_csv('matches.csv')


# In[23]:


matches.shape


# In[24]:


matches


# In[25]:


matches.head(10)


# In[26]:


matches.info()


# In[27]:


matches


# In[28]:


matches.shape[0]


# In[29]:


matches['id'].max()


# In[30]:


#matches['season'] == 2017
matches_2017 = matches[matches['season'] == 2017]


# In[31]:


type(matches)


# In[32]:


type(matches_2017)


# In[33]:


matches_2017.shape[0]


# In[35]:


len(matches['season'].unique())


# In[36]:


matches_2017


# In[37]:


dfa = matches[matches['season'] == 2017]


# In[38]:


#dfa['winner']== dfa['toss_winner']
winner_dfa = dfa[dfa['winner']== dfa['toss_winner']]


# In[40]:


perc = (winner_dfa.shape[0]/dfa.shape[0])*100


# In[41]:


print(perc)


# In[42]:


last_match = dfa.tail(1)


# In[43]:


last_match['winner']


# In[46]:


last_match[['team1', 'team2']]


# In[47]:


matches


# In[48]:


#matches['dl_applied'] == 1
dl_used = matches[matches['dl_applied'] == 1]


# In[49]:


dl_used


# In[50]:


dl_used.shape[0]


# In[51]:


dl_used['city']


# In[53]:


dl_used['city'].value_counts()


# In[54]:


type(dl_used)


# In[55]:


dl_used_city = dl_used['city'].value_counts()


# In[56]:


type(dl_used_city)


# In[57]:


dl_used


# In[59]:


sns.countplot(y='city', data=dl_used)
plt.show()


# In[60]:


matches


# In[62]:


#matches['win_by_runs'].idmax()
matches.iloc[matches['win_by_runs'].idxmax()]


# In[63]:


matches.iloc[matches['win_by_runs'].idxmax()]['winner']


# In[64]:


matches


# In[65]:


matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner']


# In[66]:


matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmin()]


# In[67]:


sns.countplot(x='winner', data=matches)
plt.show()


# In[68]:


sns.countplot(y='winner', data=matches)
plt.show()


# In[70]:


data = matches.winner.value_counts()
sns.barplot(y= data.index, x = data)


# In[71]:


matches


# In[72]:


sns.countplot(y='player_of_match', data=matches)
plt.show()


# In[73]:


top_players = matches.player_of_match.value_counts()[:10]


# In[75]:


sns.barplot(y=top_players.index, x = top_players)
plt.show()


# In[ ]:





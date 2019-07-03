#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from datetime import timedelta


# In[2]:


pd.read_csv('filmdata.csv',delimiter=';')


# In[3]:


data=pd.read_csv('filmdata.csv',delimiter=';' )


# In[4]:


data.columns=['ID', 'title', 'year', 'rating', 'votes', 'duration', 'genres']


# In[5]:


data.info()


# In[6]:


data1=pd.DataFrame(data,columns=['ID'])


# In[7]:


data1


# In[8]:


data.head()


# In[9]:


data.tail(11)


# In[10]:


data.info(verbose=True)


# In[11]:


data.info(verbose=False)


# In[12]:


data.info()


# In[13]:


data.info(verbose='True',null_counts='False')


# In[14]:


data.info(memory_usage='deep')


# In[15]:


#data.drop([],axis=0,inplace=True)


# In[16]:


checkrow=data.dropna(axis=0)


# In[17]:


checkrow.shape


# In[18]:


data.shape


# In[19]:


checkrow.isna()


# In[20]:


#df['title'].str.lstrip('+-').str.rstrip('aAbBcC')


# In[21]:


#data['title'] = data['title'].map(lambda x: str(x)[:-1])


# In[22]:


data


# In[ ]:





# In[23]:


data['title']=data['title'].str.slice(0, -6)


# In[24]:


data


# In[25]:


data['duration']=data['duration'].str.slice(0, -5)


# In[26]:


data


# In[27]:


#data['duration'] = data['duration'] * 60 


# In[28]:


df1 = data['duration'].str.split('.', expand=True).astype(int)
data['duration'] =df1*60


# In[29]:


data


# In[30]:


#Concatination


# In[31]:


import pandas as pd


# In[32]:


movie_crew_df=pd.read_csv('crew_data.tsv.gz', sep='\t')


# In[33]:


movie_crew_df.head()


# In[34]:


movie_crew_df=movie_crew_df.rename(columns={'tconst':'ID','directors':'director_ids'})


# In[35]:


movie_crew_df.head()


# In[36]:


#movie_crew_df = movie_crew_df.rename_axis('ID')


# In[37]:


movie_crew_df.set_index('ID',inplace = True)


# In[38]:


del movie_crew_df['writers']


# In[39]:


movie_crew_df


# In[40]:


person_df=pd.read_csv('name_data.tsv.gz', sep='\t')


# In[41]:


person_df.head()


# In[42]:


person_df=person_df.rename(columns={'nconst':'person_ID','primaryName':'name'})


# In[43]:


person_df.head()


# In[44]:


person_df.drop(['birthYear','deathYear','primaryProfession','knownForTitles'],axis=1,inplace=True)


# In[45]:


person_df


# In[46]:


df_1=pd.merge(data,movie_crew_df, how='outer',on='ID')


# In[47]:


df_1.drop(['title','year','rating','votes','duration','genres'],axis=1,inplace=True)


# In[48]:


df_1.head()


# In[49]:


df_1.dropna()


# In[50]:


dropping=df_1[(df_1['director_ids'].str.len()>9)].index
df_1.drop(dropping,inplace=True)


# In[51]:


df_1.head()


# In[52]:



df_1=df_1.rename(columns={'director_ids':'director_id'})


# In[53]:


df_1.head()


# In[54]:


df_2=pd.merge(df_1,person_df, how='outer',left_on='director_id',right_on='person_ID')


# In[55]:


df_2.head()


# In[56]:


df_2.drop(['director_id','person_ID'],axis=1,inplace=True)


# In[57]:


df_2.head()


# In[58]:


df_2=df_2.rename(columns={'name':'Director'})


# In[59]:


print(df_2)


# In[60]:


#Exploration


# In[61]:


import numpy as np
import pandas as pd


# In[62]:


data.head()


# In[63]:


#data[data['duration']==data['duration'].max()].head(10)


# In[64]:


data.nlargest(10, ['duration'])


# In[65]:


data.groupby(['rating']).max()


# In[66]:


data.sort_values(['rating', 'title'], ascending = [False, True])


# In[67]:


data.head()


# In[68]:


min=data['duration']/60


# In[69]:


min.mean()


# In[71]:


df_2.head()


# In[79]:


data.head()


# In[80]:


df_2.head()


# In[81]:


prod = pd.merge(df_2, data, on = 'ID', how = 'outer' )


# In[82]:


prod.head()


# In[84]:


prod.sort_values(['rating', 'votes'], ascending = [False, False])


# In[87]:


prod


# In[89]:


movies_20000=(prod['year']>1999)&(prod['year']<2010)


# In[92]:


prod[movies_20000]


# In[100]:


akira=prod[prod['Director']=='Akira Kurosawa']


# In[99]:


#prod[akira]
#sorting_year=prod[['Title','year','director']].sort_values(['year'], ascending=[False])


# In[103]:


akira.head()


# In[105]:


akira.sort_values(['year'],ascending=[True])


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#  importing libaries
# 

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn


# ## 2.loading the data

# In[12]:



data =pd.read_csv ( r"C:\Users\User\Downloads\VEDHA\Churn_Modelling.csv" )


# In[13]:


data.head()


# In[14]:


data.tail()


# In[15]:


data.shape


# In[61]:


data.describe()


# In[62]:


data.info()


# ## 4.statistical analysis

# In[63]:


data.head()


# In[64]:


data.columns


# In[65]:


data.nunique()


# In[66]:


data.mean()


# In[67]:


data.describe()


# In[68]:


data['Age'].unique()


# In[69]:


data['Gender'].unique()


# In[70]:


data['Age'].value_counts()


# ## 3. Data Visualizations
# 

# In[44]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn


# In[45]:


#univariate analysis
sns.distplot ( data ['Age'] )


# In[46]:


sns.histplot ( data ['Age'] )


# In[47]:


sns.boxplot ( data ['Age'] )


# In[48]:


# bi variate analysis


# In[49]:


sns.barplot ( data ['Age'] , data ['CreditScore'] )


# In[50]:


sns.scatterplot ( data ['Age'] , data ['CreditScore'] )


# In[51]:


#Multi-Variate Analysis


# In[52]:


sns.pairplot( data )


# In[53]:


data.corr()


# In[20]:


sns.heatmap(data.corr())


# In[ ]:


sns.heatmap(data.corr(),annot=True)


# ## 5. handling the missing values

# In[ ]:


data. isnull().any()


# In[ ]:




data.isnull().sum()


# In[ ]:


data['Age'].mean()


# In[ ]:


data['Age'].median()


# In[ ]:


data['Age'].mode()


# In[ ]:


data['Age'].unique()


# In[ ]:


data['Age'].value_counts()


# In[ ]:


data['Age'] = data['Age'].fillna(data['Age'].mean())


# In[ ]:


#replacing the null values


# In[ ]:


data.replace(to_replace='Johnstone',value='john')


# ## 6. OUTLIERS

# In[ ]:


sns.boxplot(data['Age'])


# In[ ]:


q = data.quantile ( [ 0.75,0.25 ] )


# In[ ]:


q


# In[ ]:


iqr = q.iloc[ 0 ]- q.iloc [ 1 ]


# In[ ]:


iqr


# In[ ]:


u = q.iloc[0] + (1.5*iqr)


# In[ ]:


u


# In[ ]:


l= q.iloc [ 1 ] - ( 1.5*iqr ) 


# In[ ]:


l


# In[ ]:


data['Age'] = np.where(data['Age']>62,40,data['Age'])


# In[ ]:


sns.boxplot(data['Age'])


# ## 7.Encoding

# In[ ]:


from sklearn.preprocessing import LabelEncoder , OneHotEncoder
le = LabelEncoder()
oneh = OneHotEncoder( )
data['Gender'] = le.fit_transform(data['Gender'])


# In[ ]:


data.head()


# ## 8.split data into dependent and independent

# In[ ]:


x = data.iloc[:,1:10]


# In[ ]:


x


# In[ ]:


y=data['Geography']


# In[ ]:


y


# ## 9.scaling

# In[ ]:


from sklearn import preprocessing

 
# separate the independent and dependent variables
X_data = data.Age

 
# standardization of dependent variables
standard = preprocessing.scale(X_data)
print(standard)


# ## 10.split into train and test

# In[ ]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X = data.iloc[:, :-1]
y = data.iloc[:, -1]


X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.05, random_state=0)


# In[ ]:


X_train


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





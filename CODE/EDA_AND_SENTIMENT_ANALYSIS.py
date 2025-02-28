#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install textblob


# In[2]:


import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# In[3]:


df = pd.read_csv(r"C:\Users\patel\Downloads\IMDB_MOVIE_SENTIMENT_PROJECT\Updated_Movies.csv")


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


# checking null valus
df.isna().sum()


# In[61]:


df.nunique()


# In[7]:


# Converting Movie_name in proper format
df['Movie_name'] = df['Movie_name'].str.replace(r'^\d+\.\s*', '', regex=True)


# In[8]:


df


# In[9]:


# Converting Duration in Minutes
df['Duration'] = df['Duration'].apply(lambda x: int(re.findall(r'(\d+)h', x)[0]) * 60 if isinstance(x, str) and 'h' in x else 0) + \
                   df['Duration'].apply(lambda x: int(re.findall(r'(\d+)m', x)[0]) if isinstance(x, str) and 'm' in x else 0)


# In[10]:


# Filling missing values in Duration using Median
df["Duration"].fillna(df["Duration"].median(), inplace=True)


# In[11]:


df


# In[12]:


# Converting num_Reviews in properformat
df['Num_Reviews'] = df['Num_Reviews'].astype(str).str.strip(" ()").apply(lambda x: int(float(x.replace('K', '')) * 1_000) if 'K' in x else 
                                                                            int(float(x.replace('M', '')) * 1_000_000) if 'M' in x else int(x) if x.isdigit() else None)


# In[13]:


df


# In[14]:


# Filling null values in matascore
df["Metascore"].fillna(df["Metascore"].median(), inplace=True)


# In[15]:


df["Summary"].fillna("", inplace=True)


# In[16]:


df.isnull().sum()


# In[17]:


# Changing Data Types
df = df.astype({
    "Duration": "int64",
    "Num_Reviews": "int64",
    "Metascore": "int64"
})


# In[18]:


df.describe()


# # EDA

# In[19]:


# Average IMDB Rating
Ave_Rating = df["Rating"].mean()


# In[20]:


Ave_Rating


# In[21]:


# Highest Rated Movie
Highest_rated = df.loc[df["Rating"].idxmax(), "Movie_name"]


# In[22]:


Highest_rated


# In[23]:


# Highest Reviewed Movie
Highest_Reviewd = df.loc[df["Num_Reviews"].idxmax(), "Movie_name"]


# In[24]:


Highest_Reviewd


# In[25]:


# Average Movie Duration
Avg_Duration  = df["Duration"].mean()


# In[26]:


Avg_Duration


# In[27]:


# Top 10 Movies with Highest Metascore
top_10 = df.nlargest(10, 'Metascore')[['Movie_name', 'Metascore', 'Rating']]


# In[28]:


top_10


# In[29]:


# Movies with Rating >= 8.5
top_movies = df[df["Rating"] >= 8.5][['Movie_name', 'Rating', 'Num_Reviews']]


# In[30]:


top_movies


# In[31]:


# Average Rating by Genre
avg_rating_genre = df.groupby('Genre')["Rating"].mean().sort_values(ascending=False)


# In[32]:


avg_rating_genre


# In[33]:


# Most reviewed by Genre
most_reviewed_genre = df.groupby('Genre')["Num_Reviews"].sum().sort_values(ascending=False)


# In[34]:


most_reviewed_genre


# In[35]:


# Average Metascore by Genre
avg_metascore_genre = df.groupby('Genre')["Metascore"].mean().sort_values(ascending=False)


# In[36]:


avg_metascore_genre


# In[37]:


plt.figure(figsize=(8, 5))
sns.histplot(df['Rating'], bins=20, kde=True, color='blue')
plt.title("Distribution of IMDB Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()


# In[38]:


plt.figure(figsize=(8, 5))
sns.histplot(df['Duration'], bins=20, kde=True, color='green')
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Frequency")
plt.show()


# In[39]:


plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Num_Reviews'], y=df['Rating'], alpha=0.5, color='red')
plt.title("IMDB Rating vs. Number of Reviews")
plt.xlabel("Number of Reviews")
plt.ylabel("Rating")
plt.show()


# In[40]:


sns.boxplot(x=df['Rating'])
plt.title("Box Plot of IMDB Ratings")
plt.xlabel("Rating")
plt.show()


# In[41]:


sns.boxplot(x=df['Genre'], y=df['Rating'])
plt.xticks(rotation=45)
plt.title("Genre-wise Distribution of IMDB Ratings")
plt.xlabel("Genre")
plt.ylabel("Rating")
plt.show()


#  # Sentiment Analysis

# In[42]:


df["Sentiment_Score"] = df["Summary"].apply(lambda x: TextBlob(x).sentiment.polarity if isinstance(x, str) else None)


# In[43]:


df


# In[44]:


plt.figure(figsize=(8, 5))
sns.histplot(df["Sentiment_Score"].dropna(), bins=20, kde=True, color='purple')
plt.title("Distribution of Sentiment Scores")
plt.xlabel("Sentiment Score")
plt.ylabel("Frequency")
plt.show()


# In[45]:


plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Sentiment_Score"], y=df["Rating"], alpha=0.5, color='orange')
plt.title("Sentiment Score vs. IMDb Rating")
plt.xlabel("Sentiment Score")
plt.ylabel("IMDb Rating")
plt.show()


# In[46]:


# Movies with Highest Sentiment Scores
top_10_sentiment = df.nlargest(10, "Sentiment_Score")[['Movie_name', 'Sentiment_Score', 'Rating']]


# In[47]:


top_10_sentiment


# # Machine Learning - Predicting IMDb Ratings

# In[48]:


features = ["Sentiment_Score", "Num_Reviews", "Duration", "Metascore"]
X = df[features]
y = df["Rating"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[49]:


model = LinearRegression()
model.fit(X_train, y_train)


# In[50]:


y_pred = model.predict(X_test)


# In[51]:


y_pred


# In[52]:


mse = mean_squared_error(y_test, y_pred)


# In[53]:


mse


# In[54]:


r2 = r2_score(y_test, y_pred)


# In[55]:


r2


# In[56]:


df.to_csv('Cleaned_Updated_Movies.csv',index = False)


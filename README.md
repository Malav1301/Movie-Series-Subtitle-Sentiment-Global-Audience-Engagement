# IMDb Sentiment Analysis & Power BI Dashboard

## 📌 Project Overview
This project analyzes IMDb movie data to extract insights using sentiment analysis, statistical tests, and machine learning. The final step involves creating a **Power BI dashboard** to visualize key trends in ratings, sentiment, and audience engagement.

---

## 📂 Dataset Used
- **Scraped IMDb Data** using Python (Selenium).  
- IMDb movie details with features like **Rating, Metascore, Genre, Duration, Reviews, and Summary**.  
- Sentiment scores generated from movie summaries.

---

## 🛠️ Data Processing Steps

### **1️⃣ Web Scraping (Python)** [**View Web Scraping Code**](https://github.com/Malav1301/Movie-Series-Subtitle-Sentiment-Global-Audience-Engagement/blob/main/CODE/Web_Scrapping_IMDB.ipynb)
- Used **BeautifulSoup & Selenium** to extract IMDb movie data.  
- Scraped movie details including **title, rating, metascore, genre, duration, reviews, and summary**.  
- Stored scraped data in a structured **CSV file** for further processing.

### **2️⃣ Data Cleaning & Preprocessing (Python)** [**View EDA Code**](https://github.com/Malav1301/Movie-Series-Subtitle-Sentiment-Global-Audience-Engagement/blob/main/CODE/EDA_AND_SENTIMENT_ANALYSIS.ipynb)
- Removed unnecessary characters from **Movie Names**.  
- Converted **Duration** to numerical values (minutes).  
- Cleaned and converted **Num_Reviews** (K/M notation to integer).  
- Handled **missing values** using median imputation.  
- Converted **Metascore, Duration, Num_Reviews** to appropriate data types.

### **3️⃣ Exploratory Data Analysis (EDA)** 
- Plotted **Distribution of IMDb Ratings** (Histogram).  
- Analyzed **Distribution of Movie Durations** (Histogram).  
- Visualized **IMDB Rating vs. Number of Reviews** (Scatter Plot).  
- Visualized **Genre-wise Distribution of IMDB Ratings** (Boxplots).  
- Visualized a **Distribution of Sentiment Scores** (Boxplots).

### **4️⃣ Sentiment Analysis** 
- Used **TextBlob** to assign sentiment polarity to each movie summary.  
- Plotted **Sentiment Score Distribution** and analyzed its relationship with **IMDb Ratings**.

### **5️⃣ Statistical Testing & Machine Learning**
- **Hypothesis:** Positive sentiment leads to higher IMDb ratings.  
- **Correlation Analysis:** Checked the relationship between **Sentiment Score & IMDb Rating**.  
- **Regression Model:** Built a **Linear Regression Model** to predict IMDb ratings based on Sentiment Score, Metascore, Duration, and Reviews.

---

## 📌 Recommendations for Streaming Platforms
✔️ **Optimize Content Sequencing:** Balance dramatic and comedic scenes to maintain engagement.  
✔️ **Use Sentiment-Based Recommendations:** Promote movies with higher sentiment scores in targeted regions.  
✔️ **Improve Movie Marketing:** Highlight key sentiment-driven insights in trailers and promotions.  
✔️ **Reduce Viewer Drop-off:** Identify high-exit scenes and introduce engaging elements to retain viewers.  
✔️ **Cultural Adaptation:** Adjust **content recommendations** based on sentiment trends in different regions.

---

## 🚀 Future Work
- **Enhancing Sentiment Analysis:** Use **advanced NLP models (BERT, GPT)** for better accuracy.  
- **Real-Time Viewer Drop-off Prediction:** Apply **deep learning models** to predict engagement.  
- **Streaming Optimization:** Implement personalized content curation based on sentiment impact.

---

## 📊 Power BI Dashboard Insights

![IMDb Sentiment Analysis Dashboard](https://github.com/Malav1301/Movie-Series-Subtitle-Sentiment-Global-Audience-Engagement/blob/main/Dashboard/Screenshot%202025-03-03%20212728.png)

---

## 🔗 Contributors
👤 **Malav Menpara**  
📧 **malavmenpara2001@gmail.com**  
💼 **[GitHub](https://github.com/Malav1301)**

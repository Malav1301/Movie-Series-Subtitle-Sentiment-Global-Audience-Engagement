# IMDb Sentiment Analysis & Power BI Dashboard

## 📌 Project Overview
This project analyzes IMDb movie data to extract insights using sentiment analysis, statistical tests, and machine learning. The final step involves creating a **Power BI dashboard** to visualize key trends in ratings, sentiment, and audience engagement.

---

## 📂 Dataset Used
- **Scraped IMDb Data** using Python (BeautifulSoup, Selenium) 
- IMDb movie details with features like **Rating, Metascore, Genre, Duration, Reviews, and Summary**.
- Sentiment scores generated from movie summaries.

---

## 🛠️ Data Processing Steps

### **1️⃣ Web Scraping (Python)**
- Used **BeautifulSoup & Selenium** to extract IMDb movie data.
- Scraped movie details including **title, rating, metascore, genre, duration, reviews, and summary**.
- Stored scraped data in a structured **CSV file** for further processing.

### **2️⃣ Data Cleaning & Preprocessing (Python)**
- Removed unnecessary characters from **Movie Names**.
- Converted **Duration** to numerical values (minutes).
- Cleaned and converted **Num_Reviews** (K/M notation to integer).
- Handled **missing values** using median imputation.
- Converted **Metascore, Duration, Num_Reviews** to appropriate data types.

### **3️⃣ Exploratory Data Analysis (EDA)**
- **Distribution of IMDb Ratings** (Histogram)
- **Duration vs. Ratings Relationship** (Scatter Plot)
- **Top 10 Highest Rated Movies** (Bar Chart)
- **Genre-based insights** (Boxplots & Aggregated Averages)
- **Correlation Matrix** to find key relationships

### **4️⃣ Sentiment Analysis**
- Used **TextBlob** to assign sentiment polarity to each movie summary.
- Plotted **Sentiment Score Distribution** and its relationship with **IMDb Ratings**.

### **5️⃣ Statistical Testing & Machine Learning**
- **Hypothesis:** Positive sentiment leads to higher IMDb ratings.
- **Correlation Analysis:** Checked relationship between **Sentiment Score & IMDb Rating**.
- **Regression Model:** Built a **Linear Regression Model** to predict IMDb ratings based on Sentiment Score, Metascore, Duration, and Reviews.

---

## 📊 Power BI Dashboard Insights

### **🔹 Visualizations in Power BI**
- **IMDb Ratings Distribution (Histogram)**
- **Sentiment Score vs IMDb Ratings (Scatter Plot)**
- **Top 10 Movies by Rating (Bar Chart)**
- **Genre-wise Rating Comparison (Stacked Bar Chart)**
- **Duration vs. Ratings Impact (Box Plot)**
- **Drop-off Rate Analysis (Funnel Chart)**
- **Sentiment Trends by Region (Map Visualization)**

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

## 🔗 Contributors
👤 **Your Name**  
📧 **your.email@example.com**  
💼 **LinkedIn/GitHub Profile**


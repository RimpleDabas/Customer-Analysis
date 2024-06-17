# Churn Analysis
## Requirements
To conduct a churn analysis using the provided data, focusing on factors such as demographics, gender, and credit scores, and to provide insights for improving customer retention.

## Tools Used
- Azure data studio
- SQL Server
- SQL Alchemy
- Pandas
- Numpy
- Matplotlib
- pyodoc

# Steps 
- Created Database
- Loaded data into the database
- Made connection with the database using SQL Alchemy 
- Did analysis writing Sql queries 
- Created visualizations
- Analysed results

# Dataset
The dataset have 12 columns and 10000 rows
- customer_id           int64
- credit_score          int64
- country              object
- gender               object
- age                   int64
- tenure                int64
- balance             float64
- products_number       int64
- credit_card            bool
- active_member          bool
- estimated_salary    float64
- churn                  bool

Here are the few analysis and insights. For more detailed code and analysis
please refer [here](Customer-Analysis\Analysis.ipynb)
### Analysis based on demography and gender 
 Overall Churn Rate by Country:

- Germany: Higher churn rates, especially among females (37.55%) compared to males (27.81%)

- Spain: Lower churn rates overall, with males (13.11%) and females (21.21%) having the least churn compared to other countries

- France: Lowest churn rates for males (12.71%) but a significant increase for females (20.34%)

 Insights 
 - In all countries, female customers exhibit higher churn rates compared to male customers
- The disparity is most pronounced in Germany, where the churn rate for females is about 10% higher than for males
- Spain has the smallest gender disparity in churn rates, with a difference of about 8%.

### Analysis based on age 
- 51-70: This age group has the highest churn rate at 48.94%. Despite having fewer total customers compared to the 31-50 age group, the churn rate is significantly higher
- 31-50: This is the largest customer group with 6771 total customers and a moderate churn rate of 19.58%
- 70 and above: This group has the lowest churn rate at 8.27%, though the total number of customers is quite small 
- 18-30: This age group has the second-lowest churn rate at 7.52%, with 1968 total customers.

Insights

- The 51-70 age group is experiencing almost half of its customers churning, which is a critical issue
- Younger customers (18-30) and those over 70 have the lowest churn rates, suggesting higher satisfaction or engagement within these age brackets
- The 31-50 age group, despite having the most customers, maintains a relatively moderate churn rate.

### Analysis based on Credit score 

- Customers with bad credit have the highest churn rate of 22.22% , indicating they might be facing more challenges in maintaining their services or satisfaction
- The churn rates for customers with fair, excellent, and very good credit are quite close, all around the 20% mark
- Customers with good credit have the lowest churn rate of 19%, suggesting they are the most satisfied or the most stable in their service usage.

## Recommendations
- **Investigate High Female Churn**: Conduct surveys or focus groups to understand why female customers are churning at a higher rate. Possible areas of improvement might include customer service, product offerings, or pricing strategies targeted specifically towards female customers
- **Enhance Customer Engagement**: Implement loyalty programs, personalized marketing campaigns, and targeted promotions to increase customer retention, focusing more on female customers and specific age groups
- **Feedback Mechanisms**: Implement robust feedback mechanisms to continually gather insights from customers across all age groups. Use this data to make informed decisions about product development and service improvements. Regularly collect and analyze feedback from customers across all credit criteria to identify pain points and areas for improvement
- **Personalized Marketing and customer experience**: Tailor marketing strategies to address the specific needs and preferences of each age group.Understand the unique needs and challenges of each group and address them with specific strategies
- **Segmentation**: Segment customers and apply targeted marketing and retention strategies that are most likely to resonate with each group.












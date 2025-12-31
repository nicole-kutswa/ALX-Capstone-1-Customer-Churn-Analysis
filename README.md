<div align="right">
  
[![github](https://raw.githubusercontent.com/nicole-kutswa/Telecom-customer-churn-analysis/main/icons/git.svg)][1]
[![linkedin](https://raw.githubusercontent.com/nicole-kutswa/Telecom-customer-churn-analysis/main/icons/iconmonstr-linkedin-5.svg)][2]

[1]: https://github.com/nicole-kutswa
[2]: https://www.linkedin.com/in/nicole-kutswa/ 

</div>

# <div align="center">Telecom Customer Churn Analysis (ALX Capstone Project)</div>

![Intro](https://github.com/nicole-kutswa/ALX-Capstone-1-Customer-Churn-Analysis/blob/main/output/churn.webp?raw=true)

## What is Customer Churn?
Customer churn occurs when subscribers discontinue their service. In the highly competitive telecom industry, annual churn rates range from 15-25%. Retaining existing customers is significantly more cost-effective than acquiring new ones, making churn prediction a high-value business priority.

## Objectives:
- **Visualizing Risk:** Identify the "Profile" of a churning customer using distribution plots.
- **Feature Correlation:** Determine which variables (Tenure, Charges, Service Type) are the strongest drivers of attrition.
- **Actionable Insights:** Provide data-driven recommendations to the business to reduce churn.

## Dataset:
[Telco Customer Churn (Kaggle)](https://www.kaggle.com/bhartiprasad17/customer-churn-prediction/data)

## Implementation & Tools:
* **Python (Pandas/NumPy):** For data cleaning and handling the `TotalCharges` numeric conversion.
* **Seaborn & Matplotlib:** Used for advanced statistical visualizations like Box Plots and Heatmaps.
* **Modular Code:** Custom functions stored in `data_analysis.py` for reusable plotting logic.

---

##  Key Findings from EDA:
### 1. Churn Rate Distribution (Pie chart)
> ![Monthly Charges Boxplot](https://github.com/nicole-kutswa/ALX-Capstone-1-Customer-Churn-Analysis/blob/main/output/distribution.PNG?raw=true)
> **Insight:** Our analysis shows a 26.6% churn rate. This means that more than 1 in 4 customers are leaving the service. To maintain a healthy growth rate, we must focus on retention strategies that address the specific needs of this segment.
### 2. Monthly Charges Distribution (Box Plot)
> ![Monthly Charges Boxplot](https://github.com/nicole-kutswa/ALX-Capstone-1-Customer-Churn-Analysis/blob/main/output/charges_boxplot.png?raw=true)
> **Insight:** Our Box Plot analysis confirms that Churned customers have a significantly higher median monthly charge (approx. $80) compared to Retained customers (approx. $65). Higher price points are a direct driver of attrition.

### 3. Internet Service & Tech Support
> ![Internet Service Analysis](https://github.com/nicole-kutswa/ALX-Capstone-1-Customer-Churn-Analysis/blob/main/output/internet_services.png?raw=true)
> **Insight:** **Fiber Optic** users exhibit a massive churn rate (over 40%) despite it being a premium service. Additionally, customers with **No Tech Support** are the most likely to migrate to competitors.

### 4. Tenure vs. Churn
> ![Tenure Distribution](https://github.com/nicole-kutswa/ALX-Capstone-1-Customer-Churn-Analysis/blob/main/output/churn-by-tenure.PNG?raw=true)
> **Insight:** Churn is highest in the **first 12 months**. New customers are at the highest risk, suggesting a need for better onboarding or "first-year" loyalty incentives.

### 5. Correlation Heatmap
> ![Correlation Heatmap](https://github.com/nicole-kutswa/ALX-Capstone-1-Customer-Churn-Analysis/blob/main/output/correlation_heatmap.png?raw=true)
> **Insight:** The heatmap shows a strong negative correlation between **Tenure** and **Churn**, confirming that the longer a customer stays, the less likely they are to leave.

---
**Executive Summary: Customer Churn Analysis**
The objective of this analysis was to identify the primary drivers of customer attrition (churn) and provide actionable strategies to improve retention. Our analysis of **7,043** customers revealed three critical "risk zones" where the company is losing the most revenue.

###  Key Findings & Risk Drivers

| Risk Factor | Observation | Business Impact |
| :--- | :--- | :--- |
| **Early Tenure** | A significant spike in churn occurs within the first 12 months. | High acquisition costs are not recovered before customers leave. |
| **Contract Type** | Month-to-Month users are significantly more likely to churn. | Lack of "stickiness" makes it too easy for customers to switch. |
| **High Billing** | Churners have higher Monthly Charges (median ~$80 vs ~$65). | High costs without perceived value are driving exits. |
| **Internet Type** | Fiber Optic customers exhibit the highest churn rates. | Fast speed is not enough to maintain loyalty; price is the issue. |

##  Business Recommendations:
1. **The "First 90 Days" Program:** Focus retention efforts on new customers during their first 3 months.
2. **Fiber Optic Quality Audit:** Investigate why premium Fiber users are leaving at such high rates—potential issues with price vs. reliability.
3. **Incentivize Contracts:** Since Month-to-Month users churn the most, offer small discounts to transition them to 1-Year or 2-Year plans.

## About Me
#### Hi, I'm Nicole!
I am a Data science ML practitioner, and an aspiring Data Engineer.

[![github](https://raw.githubusercontent.com/nicole-kutswa/ALX-Capstone-1-Customer-Churn-Analysis/main/icons/git.svg)][1]
[![linkedin](https://raw.githubusercontent.com/nicole-kutswa/ALX-Capstone-1-Customer-Churn-Analysis/main/icons/iconmonstr-linkedin-5.svg)][2]

[1]: https://github.com/nicole-kutswa
[2]: https://www.linkedin.com/in/nicole-kutswa/

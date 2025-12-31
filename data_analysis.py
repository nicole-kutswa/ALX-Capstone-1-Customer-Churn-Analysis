import matplotlib.pyplot as plt  # <--- Added this
import pandas as pd
import numpy as np

def analyze_churn_rate(df):
    """Calculate and analyse overall churn rate"""
    
    # 1. Calculations
    churn_rate = df['Churn'].mean() * 100
    churned = df['Churn'].sum()
    retained = len(df) - churned
    
    # 2. Printing results (Fixed \n)
    print(f"\nOverall churn rate: {churn_rate:.2f}%")
    print(f"Churned customers: {churned}") # Removed \n here for tighter text
    print(f"Retained customers: {retained}")
    
    # 3. Visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    colors = ['#ff6b6b', '#4ecdc4']
    labels = ['Churned', 'Retained']
    sizes = [churned, retained]
    
    # Pie chart
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Customer Churn Distribution', fontsize=14, fontweight='bold')
    
    # Bar chart
    ax2.bar(['Churned', 'Retained'], sizes, color=colors)
    ax2.set_ylabel('Number of Customers')
    ax2.set_title('Customer Count by Status', fontsize=14, fontweight='bold')
    
    # Adding text labels on top of bars
    for i, v in enumerate(sizes):
        ax2.text(i, v + 50, str(v), ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    return churn_rate

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def analyze_by_tenure(df):
    """
    Analyze churn rate by customer tenure
    """
    # 1. Grouping and aggregation (Note the capital 'G' in TenureGroup)
    # observed=True is used for categorical data to avoid errors in newer pandas versions
    tenure_churn = df.groupby('TenureGroup', observed=True)['Churn'].agg(['mean', 'count'])
    tenure_churn['mean'] = tenure_churn['mean'] * 100
    
    print("\nChurn rate by tenure group:")
    print(tenure_churn)
    
    # 2. Setup the visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Bar Chart (Left)
    tenure_churn['mean'].plot(kind='bar', ax=ax1, color='#ff6b6b')
    ax1.set_xlabel('Tenure Group')
    ax1.set_ylabel('Churn Rate (%)')
    ax1.set_title('Churn Rate by Customer Tenure', fontsize=14, fontweight='bold')
    # Corrected the 'sex_' and double 'b' typos here:
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    
    # Histogram (Right)
    df[df['Churn']==1]['tenure'].hist(bins=30, ax=ax2, alpha=0.7, color='#ff6b6b', label='Churned')
    df[df['Churn']==0]['tenure'].hist(bins=30, ax=ax2, alpha=0.7, color='#4ecdc4', label='Retained')
    ax2.set_xlabel('Tenure (months)')
    ax2.set_ylabel('Number of Customers')
    ax2.set_title('Tenure Distribution by Churn Status', fontsize=14, fontweight='bold')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

def analyze_by_charges(df):
    """Analyze how monthly billing amounts impact churn"""
    
    # 1. Grouping analysis
    charges_churn = df.groupby('ChargesGroup', observed=True)['Churn'].agg(['mean', 'count'])
    charges_churn['mean'] = charges_churn['mean'] * 100
    
    # 2. Visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Bar Plot (Left)
    charges_churn['mean'].plot(kind='bar', ax=ax1, color='#ff6b6b')
    ax1.set_title('Churn Rate by Monthly Charges Group', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Churn Rate (%)')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    
    # Box Plot (Right) - Using Seaborn for a cleaner look
    sns.boxplot(x='Churn', y='MonthlyCharges', data=df, ax=ax2, palette=['#4ecdc4', '#ff6b6b'])
    ax2.set_title('Monthly Charges Distribution by Churn', fontsize=12, fontweight='bold')
    ax2.set_xticklabels(['Retained', 'Churned'])
    
    plt.tight_layout()
    plt.savefig('output/charges_boxplot.png', dpi=300, bbox_inches='tight') # This saves the file
    plt.show()
    
    return charges_churn
    
def analyze_internet_churn(df):
    """
    Analyze how different internet technologies affect churn
    """
    # 1. Calculate churn rate per service type
    internet_churn = df.groupby('InternetService')['Churn'].mean() * 100
    
    # 2. Create a temporary copy to map 0/1 to text for the legend
    # This prevents the AttributeError by giving the legend strings instead of numbers
    temp_df = df.copy()
    temp_df['Churn_Status'] = temp_df['Churn'].map({0: 'Retained', 1: 'Churned'})
    
    # 3. Setup the visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Left Plot: Churn Rate %
    sns.barplot(x=internet_churn.index, y=internet_churn.values, ax=ax1, palette='magma')
    ax1.set_title('Churn Rate % by Internet Service', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Churn Rate (%)')
    
    # Right Plot: Total Customer Count (Using the new Churn_Status text column)
    sns.countplot(x='InternetService', hue='Churn_Status', data=temp_df, ax=ax2, palette=['#4ecdc4', '#ff6b6b'])
    ax2.set_title('Total Customers by Service & Churn', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Number of Customers')
    
    plt.tight_layout()
    plt.savefig('output/internet_services.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_correlation_heatmap(df):
    """
    Generate a heatmap to show relationships between numeric features
    """
    # 1. Select only numeric columns
    # We include Churn because it's 0 and 1
    numeric_df = df.select_dtypes(include=['number'])
    
    # 2. Calculate the correlation matrix
    # Values will range from -1 (opposite) to +1 (perfect match)
    corr_matrix = numeric_df.corr()
    
    # 3. Setup the visualization
    plt.figure(figsize=(10, 8))
    
    # sns.heatmap does the heavy lifting
    # annot=True puts the numbers inside the squares
    # cmap='RdBu_r' uses Red for negative and Blue for positive correlation
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0)
    
    plt.title('Correlation Heatmap of Numeric Features', fontsize=14, fontweight='bold')
    plt.savefig('output/correlation_heatmap.png', dpi=300, bbox_inches='tight') # This saves the file
    plt.show()
    
    return corr_matrix





















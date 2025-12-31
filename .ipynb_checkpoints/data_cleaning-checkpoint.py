import numpy as np
import pandas as pd

def clean_data(df):
    """
    Clean and prepare data for analysis, including feature engineering.
    """    
    # Create a copy to avoid modifying original dataframe
    df_clean = df.copy()
    
    # --- 1. TotalCharges Cleaning and Imputation ---
    
    # Identify missing values by converting ' ' to NaN
    # The result is stored in df_clean to ensure all subsequent steps operate on the same frame.
    df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')
    
    missing_charges = df_clean['TotalCharges'].isnull().sum()
    print(f"Found {missing_charges} missing TotalCharges values.")
    
    # Impute missing TotalCharges with 0 (as these are new customers with tenure = 0)
    df_clean['TotalCharges'].fillna(0, inplace=True)
    print(f"   -> Filled {missing_charges} missing TotalCharges with 0.")
    
    # --- 2. Binary Feature Encoding (Yes/No to 1/0) ---
    print(" Converting binary columns to 1/0...")
    binary_columns = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
    for col in binary_columns:
        df_clean[col] = df_clean[col].map({'Yes': 1, 'No': 0})
    
    # --- 3. Feature Engineering ---
    print(" Creating new features...")
    
    # A. Average Monthly Charges (Corrected Syntax)
    # Use 'tenure' instead of 'Tenure' for consistency and robustness
    # The +1 prevents division by zero for customers with tenure=0
    df_clean['AVGMonthlyCharges'] = df_clean['TotalCharges'] / (df_clean['tenure'] + 1) 
    
    # B. Tenure Groups (Binning)
    df_clean['TenureGroup'] = pd.cut(df_clean['tenure'], 
                                     bins=[-1, 12, 24, 48, 72], 
                                     labels=['0-1 year', '1-2 years', '2-4 years', '4+ years'],
                                     right=True) # right=True is the default but good for clarity
                                     
    # C. Monthly Charges Groups (Binning)
    df_clean['ChargesGroup'] = pd.cut(df_clean['MonthlyCharges'], 
                                      bins=[0, 35, 65, 100, 150], 
                                      labels=['Low', 'Medium', 'High', 'Very High'],
                                      right=True)
                                      
    # D. Customer Value Score (Estimated Revenue)
    df_clean['CustomerValue'] = df_clean['tenure'] * df_clean['MonthlyCharges']
    
    print(f"\n✓ Data cleaning and feature engineering complete!")
    print(f"  Final shape: {df_clean.shape}")
    print(f"  New features added: AVGMonthlyCharges, TenureGroup, ChargesGroup, CustomerValue")
    print("="*60)
    
    return df_clean
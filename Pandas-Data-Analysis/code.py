# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)

print(bank.info())

categorical_var = bank.select_dtypes(include='object')
print(categorical_var.head())
print("##############################################")
numerical_var = bank.select_dtypes(include='number')
print(numerical_var.head())



# code ends here


# --------------
# code starts here


banks = bank.drop(["Loan_ID"],axis=1)
print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
print(bank_mode)

banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here


avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values="LoanAmount", aggfunc=np.mean)

print(avg_loan_amount)
# code ends here



# --------------
# code starts here
loan_approved_se = banks.where((banks["Self_Employed"] == "Yes") & 
                    (banks["Loan_Status"] == "Y"))["Loan_Status"].count()

loan_approved_nse = banks.where((banks["Self_Employed"] == "No") & 
                    (banks["Loan_Status"] == "Y"))["Loan_Status"].count()

print(loan_approved_se)
print(loan_approved_nse)

percentage_se = (loan_approved_se / 614 ) *100
percentage_nse = (loan_approved_nse / 614 ) *100

# code ends here


# --------------
# code starts here

loan_term = banks["Loan_Amount_Term"].apply(lambda x: x/12)

# print(loan_term)

big_loan_term = loan_term[loan_term >= 25].count()

print(big_loan_term)
# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby("Loan_Status")

loan_groupby = loan_groupby[["ApplicantIncome", "Credit_History"]]

print(loan_groupby.head())

mean_values = loan_groupby.mean()
print(mean_values)
# code ends here



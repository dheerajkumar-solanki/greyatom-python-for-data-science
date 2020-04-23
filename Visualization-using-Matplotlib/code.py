# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)

loan_status = data["Loan_Status"].value_counts()

loan_status.plot(kind="bar")
plt.xticks(rotation=0)
plt.show()
#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(["Property_Area", "Loan_Status"]).size().unstack()

property_and_loan.plot(kind="bar",stacked=False)

plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

education_and_loan = data.groupby(["Education", "Loan_Status"]).size().unstack()

education_and_loan.plot(kind="bar", stacked=True)

plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = data[data["Education"] == "Graduate"]
not_graduate = data[data["Education"] == "Not Graduate"]
graduate["LoanAmount"].plot(kind="density", label="Graduate")
not_graduate["LoanAmount"].plot(kind="density", label="Not Graduate")

#For automatic legend display
plt.legend()
plt.xlabel("Loan Amount")
plt.show()







#Code ends here





# --------------
#Code starts here

fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=3, ncols=1, figsize=(7,18))
data["TotalIncome"] = data["ApplicantIncome"] + data["CoapplicantIncome"]
data.plot.scatter(y="ApplicantIncome", x="LoanAmount", ax=ax_1)
data.plot.scatter(y="CoapplicantIncome", x="LoanAmount", ax=ax_2)
data.plot.scatter(y="TotalIncome", x="LoanAmount", ax=ax_3)

ax_1.set_title("Applicant Income")
ax_2.set_title("Coapplicant Income")
ax_3.set_title("Total Income")
plt.show()



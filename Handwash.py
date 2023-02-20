import pandas as pd
# Read datasets/yearly_deaths_by_clinic.csv into yearly
yearly = pd.read_csv('datasets/yearly_deaths_by_clinic.csv')
yearly['proportion_deaths']=yearly['deaths']/yearly['births']
# Extract Clinic 1 data into clinic_1 and Clinic 2 data into clinic_2
clinic_1 = yearly[yearly['clinic']=='clinic 1']
clinic_2 = yearly[yearly['clinic']=='clinic 2']
import matplotlib.pyplot as plt
ax=clinic_1.plot(y='proportion_deaths',x='year',label='Clinic_1',ylabel='Proportion deaths')
clinic_2.plot(y='proportion_deaths',x='year',ax=ax,label='Clinic_2',xlabel='year',ylabel='Proportion deaths')
monthly = pd.read_csv('datasets/monthly_deaths.csv',parse_dates=['date'])

# Calculate proportion of deaths per no. births
monthly["proportion_deaths"]=monthly['deaths']/monthly['births']
ax=monthly.plot(y='proportion_deaths',x='date',ylabel='Proportion deaths')
handwashing_start = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly[monthly['date']<handwashing_start]
after_washing = monthly[monthly['date']>=handwashing_start]

# Plot monthly proportion of deaths before and after handwashing
ax=before_washing.plot(y='proportion_deaths',x='date',label='before_wash',ylabel='Proportion deaths')
after_washing.plot(y='proportion_deaths',x='date',ax=ax,label='after_wash',xlabel='year',ylabel='Proportion deaths')
before_proportion = before_washing['proportion_deaths']
after_proportion = after_washing['proportion_deaths']
mean_diff = after_proportion.mean()-before_proportion.mean()
# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1,replace=True)
    boot_after = after_proportion.sample(frac=1,replace=True)
    boot_mean_diff.append( boot_after.mean()-boot_before.mean() )

# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025,0.975])
print(confidence_interval)
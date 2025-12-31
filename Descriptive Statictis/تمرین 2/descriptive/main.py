from extractions import *
from transformers import *
from loads import *
import pandas as pd
import matplotlib.pyplot as plt



def display_data(data):
    print(data)
    
# data=extract_csv('./data.csv')
# display_data(data)

# data_fixed = fix_weight_gender(data)
# display_data(data_fixed)

# save_clean_data_csv(data_fixed, './clean_data.csv')

#----------------------------------------------------------------
clean_data=extract_csv('./clean_data.csv')
# display_data(clean_data)

data_filled = fillna(clean_data)
# display_data(data_filled)

data_noisy= fix_number_of_children(data_filled)
# display_data(data_noisy)

#----------------------------------------------------------------
# income_cols = [
#     'January income', 'February income', 'March income',
#     'April income', 'May income', 'June income',
#     'July income', 'August income', 'September income',
#     'October income', 'November income', 'December income'
# ]

# data_noisy['Average Income'] = data_noisy[income_cols].mean(axis=1)

# plt.figure()
# plt.bar(data_noisy['Name'], data_noisy['Average Income'])
# plt.xlabel('Name')
# plt.ylabel('Average Income')
# plt.title('Average Monthly Income per Person')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#----------------------------------------------------------------import matplotlib.pyplot as plt

# months = [
#     'January income', 'February income', 'March income',
#     'April income', 'May income', 'June income',
#     'July income', 'August income', 'September income',
#     'October income', 'November income', 'December income'
# ]

# plt.figure()

# for index, row in data_noisy.iterrows():
#     plt.plot(months, row[months], marker='o', label=row['Name'])

# plt.xlabel('Month')
# plt.ylabel('Income')
# plt.title('Income Trend of Each Person Over 12 Months')
# plt.xticks(rotation=45)
# plt.legend()
# plt.tight_layout()
# plt.show()

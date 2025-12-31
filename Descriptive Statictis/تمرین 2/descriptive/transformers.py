import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt

def fix_weight_gender(df):
    df = df.copy()
    df.columns = df.columns.str.strip()

    for i in range(len(df)):
        weight = str(df.loc[i, "Weight"]).strip()
        
        if not weight.isdigit():
            match = re.match(r"(\d+)(Male|Female)", weight)

            if match:
                number = int(match.group(1))
                gender = match.group(2)

                df.loc[i, "MaritalStatus"] = df.loc[i, "Education"]
                df.loc[i, "Education"] = df.loc[i, "City"]
                df.loc[i, "City"] = df.loc[i, "Hobby"]
                df.loc[i, "Hobby"] = df.loc[i, "Gender"]
                df.loc[i, "Weight"] = number
                df.loc[i, "Gender"] = gender
    return df

#=========================================================================
def save_clean_data_csv(df, path):
    df.to_csv(path, index=False)
#=========================================================================

'''Name,Age,Height,Weight,Gender,Hobby,City,Education,MaritalStatus,Number of children,
January income,February income,March income,April income,May income,June income,
July income,August income,September income,October income,November income,December income'''
#=========================================================================
def fillna(data):
    data.fillna(value={
        "Name":data.Name.mode()[0],
        "Age":data.Age.mean(),
        "Height":data.Height.mean(),
        "Weight":data.Weight.mean(),
        "Gender":data.Gender.mode()[0],
        "Hobby":data.Hobby.mode()[0],
        "City":data.City.mode()[0],
        "Education":data.Education.mode()[0],
        "MaritalStatus":data.MaritalStatus.mode()[0],
        "Number of children":data["Number of children"].mode()[0],
        "January income":data["January income"].mean(),
        "February income":data["February income"].mean(),
        "March income":data["March income"].mean(),
        "April income":data["April income"].mean(),
        "May income":data["May income"].mean(),
        "June income":data["June income"].mean(),
        "July income":data["July income"].mean(),
        "August income":data["August income"].mean(),
        "September income":data["September income"].mean(),
        "October income":data["October income"].mean(),
        "November income":data["November income"].mean(),
        "December income":data["December income"].mean()
    },inplace=True)
    return data
#=========================================================================
def fix_number_of_children(df, max_children=5):
    df = df.copy()
    col = "Number of children"
    numeric = pd.to_numeric(df[col], errors="coerce")
    valid_mask = (numeric >= 0) & (numeric <= max_children)
    mode_value = numeric[valid_mask].mode()
    if mode_value.empty:
        return df
    mode_value = mode_value.iloc[0]
    df.loc[~valid_mask, col] = mode_value
    return df
#=========================================================================

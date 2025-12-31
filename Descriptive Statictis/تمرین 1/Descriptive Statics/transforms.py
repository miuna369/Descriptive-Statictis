import pandas as pd
import re
import numpy as np

def clean_numeric_spaces(df):
    for col in df.select_dtypes(include="object").columns:
        df[col]=df[col].apply(lambda x: clean_value(x))
    return df  


def clean_value(val):
    if pd.isnull(val):
        return val
    val_string=str(val)
    cleaned=re.sub(r"(?<=\d)\s+(?=\d)", "", val_string)
    if cleaned.isdigit():
        return int(cleaned)
    return cleaned

#=========================================================================
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
def calculate_stats(df, columns):
    stats = {}

    for col in columns:
        values = df[col].astype(float)

        stats[col] = {
            "mean": np.mean(values),
            "median": np.median(values)
        }

    return stats
#=========================================================================
def calculate_mode(df, columns):
    modes = {}

    for col in columns:
        mode_series = df[col].mode()
        if not mode_series.empty:
            modes[col] = mode_series.iloc[0]
        else:
            modes[col] = None

    return modes
#=========================================================================
def calculate_range(df, columns):
    result = {}
    for col in columns:
        try:
            numeric_col = df[col].astype(float)
            result[col] = numeric_col.max() - numeric_col.min()
        except Exception as e:
            result[col] = None
            print(f"خطا در ستون {col}: {e}")
    return result
#=========================================================================
def calculate_variance_sqrt(df, columns):
    result = {}
    for col in columns:
        try:
            numeric_col = df[col].astype(float)
            variance = np.var(numeric_col, ddof=1)
            result[col] = np.sqrt(variance)
        except Exception as e:
            result[col] = None
            print(f"خطا در ستون {col}: {e}")
    return result
#=========================================================================
def calculate_percentiles(df, columns, percentiles):
    result = {}
    for col in columns:
        try:
            numeric_col = df[col].astype(float)
            result[col] = {p: np.percentile(numeric_col, p) for p in percentiles}
        except Exception as e:
            result[col] = None
            print(f"خطا در ستون {col}: {e}")
    return result
#=========================================================================
def calculate_IQR(df, columns):
    result = {}
    for col in columns:
        try:
            numeric_col = df[col].astype(float)
            Q1 = np.percentile(numeric_col, 25)
            Q3 = np.percentile(numeric_col, 75)
            result[col] = Q3 - Q1
        except Exception as e:
            result[col] = None
            print(f"خطا در ستون {col}: {e}")
    return result
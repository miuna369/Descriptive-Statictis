from extractions import *
from transforms import *
from loads import *


def display(data):
    print(data)
    print(100*"-")
    

# data=extract_csv("./students.csv")
# display(data)


# data=clean_numeric_spaces(data)
# display(data)


# clean_data=fix_weight_gender(data)
# display(clean_data)

# save_clean_data_csv(clean_data, "./clean_students.csv")

#-------------------------------------------------------------------------
data=extract_csv("./clean_students.csv")
# display(data)

stats=calculate_stats(data, ["Age", "Weight"])
# display(stats)

mode=calculate_mode(data, ["Height", "Gender","Education"])
# display(mode)

range_stats=calculate_range(data, ["Age","Height","Weight"])
# display(range_stats)

variance_sqrt=calculate_variance_sqrt(data, ["Age","Height","Weight"])
# display(variance_sqrt)

percentiles=calculate_percentiles(data, ["Age","Height","Weight"], [25,50,75])
# display(percentiles)

IQR=calculate_IQR(data, ["Age","Height","Weight"])
display(IQR)
import pandas as pd
import datetime


# Function to get the current date in the format "ddMonYYYY"
def current_date():
    return datetime.datetime.now().strftime("%d%b%Y")


# Print the type and current date
print(type(current_date()), current_date())

# Read data from a CSV file (assuming it's tab-separated)
df = pd.read_csv(r"C:\Users\Thippeswamy U-3061\PycharmProjects\pythonProject\ramp_up_python\employee_details.csv", sep="\t")

# Get the column names and split them into a list
columns = list(df.columns)

split_column = columns[0].split(",")


# Convert DataFrame values to a list of lists
values = df.values.tolist()
list_of_values=[]
for value in values:
    list_of_values.append(value[0].split(","))

# Function to count how many employees are marked as "WFH" or "WFO" today
def how_many_marked_wfo_and_wfh_on_current_date(data):
    current_day = current_date()
    wfo_and_wfh_count = 0
    current_day_index = split_column.index(current_day)

    for i in range(len(values)):
        if list_of_values[i][current_day_index] == "WFH" or list_of_values[i][current_day_index] == "WFO":
            wfo_and_wfh_count += 1

    return f"marked_wfo_and_wfh_on_current_date of count is: {wfo_and_wfh_count}"


# Print the count of employees marked as "WFH" or "WFO" today
print(how_many_marked_wfo_and_wfh_on_current_date(split_column))
print()


# Function to count how many times "WFH" or "WFO" was marked in the previous 5 days
def marked_data_wfo_wfh_from_previous_5_days():
    index_of_current_date = split_column.index(current_date())
    previous_5_days_marked_wfo_and_wfh = 0

    for value in list_of_values:
        len_of_list=[col for col in value[index_of_current_date-1:index_of_current_date-6:-1] if col=="WFH" or col=="WFO"]
        previous_5_days_marked_wfo_and_wfh += len(len_of_list)

    return f"marked wfo and wfh count of previous 5 days of current date of count is: {previous_5_days_marked_wfo_and_wfh}"


# Print the count of "WFH" or "WFO" marked in the previous 5 days
print(marked_data_wfo_wfh_from_previous_5_days())
print()

# Function to get employees who have not filled in their status for the current day
def get_employee_who_not_filled_on_current_day():
    index_of_current_date = split_column.index(current_date())

    employess = []

    for value in list_of_values:

        if value[index_of_current_date] =='""':
            employess.append(value[0])

    return f"details of employess who are not filled attendance given in list format {employess}"




# Print the list of employees who have not filled in their status for the current day
print(get_employee_who_not_filled_on_current_day())
print()
def employee_who_not_filled_on_previous_5_days():
    index_of_current_date = split_column.index(current_date())



    print("employees who not filled attendance from previous 5 days of current date"+"\n"+"********************************************")

    for value in list_of_values:
        l1=[]

        for index in range(index_of_current_date-1,index_of_current_date-6,-1):
            if value[index]=='""':
                l1.append(split_column[index])




        if len(l1)>=1:
            print(f"from previous 5 days  who employee not filled attendance dates are  {value[0]}:{l1}" )




employee_who_not_filled_on_previous_5_days()

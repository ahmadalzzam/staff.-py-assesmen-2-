# importing csv module
import csv

# Open file in read mode
file = open('employees.csv','r')

# reading csv file and storing the values in list
csv_reader = list(csv.reader(file))


line = 0 # stores the line number
total_salary = 0    # stores total salary
count = 0   # count the managers

# Let's assume first employee in the file has the lowest salary.
lowest_salary = float(csv_reader[1][2])


# for loop to iterate through each line in csv file
for row in csv_reader:
    # if condition to ignore the first line of csv file
    if line != 0:
        # if condition to find the lowest salry
        if float(row[2]) < lowest_salary:
            lowest_salary = float(row[2])
            # storing the name of the person with lowest salary
            first_name = row[0]
            last_name = row[1]

        # if condition to find average saalry of the managers
        if row[3] == 'Manager':
            # calculaing the total salary
            total_salary += float(row[2])
            # calculating the total managers
            count += 1
    line += 1

# calculating the average salary
avg_salary = total_salary / count


# printing the results
print(f"The average salary of managers is {avg_salary} dollers.")
print(f"{first_name} {last_name} has Lowest salary ({lowest_salary}).")
# closing the file
file.close()
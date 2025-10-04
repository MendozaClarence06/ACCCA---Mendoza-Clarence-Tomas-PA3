# ACCCA---Mendoza-Clarence-Tomas-PA3
This repository is for use of academics purposes and are needed. This is also for PA3 with pandas as focus in the problems.

## DESCRIPTIONS ABOUT THE ORDER OF CODES USED:

#### First code (Mendoza_Pandas-P1): FIRST FIVE ROWS AND LAST FIVE ROWS:
Display the first five and last five rows of the resulting cars. The data used to display these program data are from the instruction manual with the file named: "cars.csv"

#### Second code (Mendoza_Pandas-P2): 4 PART PROBLEM:
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.


## DESCRIPTION OF FUNCTIONS USED IN MY CODE:

#### FIRST FIVE ROWS AND LAST FIVE ROWS PROBLEM:
```
import pandas as pd
```
To use the functions in the library: pandas, import is needed.
```
cars = pd.read_csv('cars.csv')
```
sets the string "cars" as the values for the file cars.csv. This code syntax gains access to the data for the file and for use in code.
```
first = cars.head(5)
```
Head function calls the first 5 functions, further specified with parameter 5 (this is not needed as .head does this already but I just wanted to try and make sure).
```
last = cars.tail(5)
```
".tail" function has the same use as the ".head" function but now gets the last 5 rows. I also did the same thing with this function.

####  4 PART PROBLEM:
```
odd = cars.iloc[:5, ::2] = With iloc instead of loc, this includes the row 0 instead of skipping it.
```
This code syntax gets the data from the file directed with the string "cars" with the use of the function iloc instead of loc, which includes row 0 instead of skipping it. For easier explanation, the function iloc or loc is formed with ".iloc[rows, columns]" and the use of ":" is for inclusion of 0-4 rows and "::" means that there is a skip of 2 every column.

```
mazda = cars.loc[cars['Model'] == 'Mazda RX4']
```
This function is the same form as used in class. Gets the rows based on the condition, which is Models that are of the specific type stated as "Mazda RX4", included in the bracket.
```
camaro = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
```
Same as used in class, and the previous code syntax, just with added conditions of "cyl".Here, we used values[0] to not include multiple rows.
```
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
```
In order to set a multiple condition line in python, we need to equate them into one list thus explaining it is needed since loc uses the brackets data as conditions.
```
group = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
```
With multiple models, they will counteract the conditions of the loc function set, thus, we have to group them instead and use isin thus proving the use of the code line that we did earlier.

## HOW TO USE THE CODE:
For this set of codes, input is actually not required and is only to be ran. No need to change the code unless want to remove the print code in the lines and remove them to show data. The use of print is just to show cleaner or better use for the user.

Note: These descriptions are all copied and or formulated from the instructions in PA2 assignment in ACCA UST.

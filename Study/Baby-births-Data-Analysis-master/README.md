# Baby-births-Data-Analysis
This assessment uses data from the United States Social Security Administration (SSA) which contains names of babies born between 1991 and 2010

In particular, we are provided with yearly files, from “yob1991.csv’ all the way to “yob2010.csv”. Each of these files contains information such as name, sex, total number and the year of births.

### The objectives of this assessment are as follows: 
1. Data handling by combining multiple datasets
2. Visualize the total male and female babies over time
3. Tabulate the most and least popular baby names
4. Analyze trends in names. 


## Task 1: 
Write a loop to concatenate (vertically) each of these files to form one big file. Call this big file as ‘full_data’. Using the data, compute the following statistics and report them as
Table 1:
(a) total number of observations,
(b) total unique names,
(c) total births, and
(d) average births per unique name.

## Task 2: 
Create a pivot table of total births by sex and year and then plot them as Figure 1.

## Task 3: 
Calculate the total births over the sample period by grouping the data by name and sex. Subset the group into male and female. Using these subsets, select the top and bottom 3 male and female names. In total, you should have 12 names in total. Report them as Table 2.

## Task 4: 
Using the top male and female names (two names in total), check their trends over time, i.e. plot the total births with these names from 1991 to 2010 as Figure 2. In order to do this, you would first need to create a pivot table

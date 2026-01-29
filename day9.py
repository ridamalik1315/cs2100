
'''
CS2100
Spring 2026
Starter code for lecture on 1/29/26
The starter code is just comments! We're working with the file
all_games.csv, which is a dataset containing PWHL games from 2023-2025
We'll be using Pandas today, which is a Python library that is super handy
for working with files, especially files that are messy, have mixed data types,
etc.
Pandas Documentation: https://pandas.pydata.org/docs/
Instructions:
- each comment below describes a task we want to accomplish using pandas
- with a teammate, look up in the pandas documentation how it should work
- then we'll put it into the real code below
'''

import pandas as pd

GAMEFILE = "all_games.csv"
#######################################################
#
# PART ONE
#
#######################################################
# 1. read all_games.csv into a dataframe
df = pd.read_csv(GAMEFILE, sep = "," , engine = "python")
# 2. what's in the dataframe?
print("print the data frame....")
print(df)
print("Print the first 10 rows of the data frame")
print(df.head(10))

# 3. how big is the dataframe? how many rows/columns?
print("Print out df.shape (rows first, columns second!")
print(df.shape)
# 4. what are the names of the columns in the dataframe?
print("what columns do I have?")
print(df.columns)
# 5. what are the datatypes of the columns?
print("what is the data type of my column")
print(df["game_number"].dtype)
#######################################################
#
# PART TWO
#
#######################################################
# 6. ask the user for a column name and tell them if it's there col = input("What column are you looking for?\n")
col = input("what column are you looking for ?")
if col in df.columns:
    print("found your columnm here it is...")
    print(df[col])
else:
    print(f"{col} does not exist")
# 7. make a copy of the dataframe. (bonus question: why??)
df_copy = df.copy()
# 8. add a new column that has total goals (instead of home goals, visit goals)
df_copy["total_goals"]  = df_copy["home_goal_count"] + df_copy["visiting_goal_count"]
print("printing out just the columns i like from my data frame")
print(df_copy[["total_goals", "home_goal_count", "vising_goal_count"]])

# 9. how many games went into overtime?
overtimes = len(df_copy[df_copy["overtime"] > 0])
print("these are the amount of games that went overtime,,, {overtimes}")
# 10. how many times were there 0 total goals in a game? 1? 2? 3? ...
# 11. can we sort the dataframe by date?
#######################################################
#

# PART THREE
#
#######################################################
# 12. filter the dataframe so we just see the rows where total goals were 0
# 13. filter the dataframe so we just see boston vs new york
# (either could be home/visiting)
# (boston team is 1, NY is 4)
# 14. Print out boston vs new york, but only some of the columns, so we see
# who was the home team, how many goals the home team had, how many goals them isiting
# team had.
# 15. How many games had boston vs new york?
# 16. how many of those games did boston win?

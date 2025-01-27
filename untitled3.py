# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QBvSwpckdAM3H3qM0JUax-JsjNqWJ8Kv
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('matches.csv')

for column in df.columns:
    unique_values = df[column].unique()
    print(f"Unique values in '{column}':\n{unique_values}\n")

df.isnull().sum()

# Step 1: Standardize city names (e.g., 'Bangalore' to 'Bengaluru', 'Mohali' to 'Chandigarh', 'Navi Mumbai' to 'Mumbai')
city_replacements = {
    'Bangalore': 'Bengaluru',
    'Mohali': 'Chandigarh',
    'Navi Mumbai': 'Mumbai'
}

df['city'] = df['city'].replace(city_replacements)

# Step 2: Handle missing values (replace nan with 'Unknown' or any other placeholder)
df['city'].fillna('Unknown', inplace=True)

# Step 3: Get unique city values after standardization
unique_cities = df['city'].unique()
print(unique_cities)

# Dictionary of player name replacements
player_name_replacements = {
    'AB de Villiers': 'AB de Villiers',
    'A.B. de Villiers': 'AB de Villiers',
    'MS Dhoni': 'MS Dhoni',
    'M.S. Dhoni': 'MS Dhoni',
    'SR Tendulkar': 'Sachin Tendulkar',
    'S.R. Tendulkar': 'Sachin Tendulkar',
    'SP Narine': 'Sunil Narine',
    'S.P. Narine': 'Sunil Narine',
    'V Sehwag': 'Virender Sehwag',
    'V. Sehwag': 'Virender Sehwag',
    'YK Pathan': 'Yusuf Pathan',
    'Y.K. Pathan': 'Yusuf Pathan',
    'BB McCullum': 'Brendon McCullum',
    'B.B. McCullum': 'Brendon McCullum',
    'SE Marsh': 'Shaun Marsh',
    'S.E. Marsh': 'Shaun Marsh',
    'KP Pietersen': 'Kevin Pietersen',
    'K.P. Pietersen': 'Kevin Pietersen',
    'A Mishra': 'Amit Mishra',
    'A. Mishra': 'Amit Mishra',
    'RG Sharma': 'Rohit Sharma',
    'R.G. Sharma': 'Rohit Sharma',
    'DJ Bravo': 'Dwayne Bravo',
    'D.J. Bravo': 'Dwayne Bravo',
    'Sohail Tanvir': 'Sohail Tanvir',
    'CH Gayle': 'Chris Gayle',
    'C.H. Gayle': 'Chris Gayle',
    'AD Russell': 'Andre Russell',
    'A.D. Russell': 'Andre Russell',
    'ST Jayasuriya': 'Sanath Jayasuriya',
    'S.T. Jayasuriya': 'Sanath Jayasuriya',
    'R Dravid': 'Rahul Dravid',
    'R. Dravid': 'Rahul Dravid',
    'M Vijay': 'Murali Vijay',
    'M. Vijay': 'Murali Vijay',
    'MM Sharma': 'Mohit Sharma',
    'M.M. Sharma': 'Mohit Sharma',
    'SL Malinga': 'Lasith Malinga',
    'S.L. Malinga': 'Lasith Malinga',
    'KD Karthik': 'Dinesh Karthik',
    'K.D. Karthik': 'Dinesh Karthik'
}

# Replace player names in the 'player_of_match' column
df['player_of_match'] = df['player_of_match'].replace(player_name_replacements)

# Display the unique values after the replacements
print("Unique values in 'player_of_match' after standardization:")
print(df['player_of_match'].unique())

# Dictionary for venue replacements
venue_replacements = {
    'M Chinnaswamy Stadium': 'M Chinnaswamy Stadium, Bengaluru',
    'M.Chinnaswamy Stadium': 'M Chinnaswamy Stadium, Bengaluru',
    'Punjab Cricket Association Stadium, Mohali': 'Punjab Cricket Association IS Bindra Stadium, Mohali',
    'Punjab Cricket Association IS Bindra Stadium, Mohali': 'Punjab Cricket Association IS Bindra Stadium, Mohali',
    'Punjab Cricket Association IS Bindra Stadium': 'Punjab Cricket Association IS Bindra Stadium, Mohali',
    'Feroz Shah Kotla': 'Arun Jaitley Stadium, Delhi',
    'Arun Jaitley Stadium': 'Arun Jaitley Stadium, Delhi',
    'Wankhede Stadium': 'Wankhede Stadium, Mumbai',
    'Wankhede Stadium, Mumbai': 'Wankhede Stadium, Mumbai',
    'MA Chidambaram Stadium, Chepauk': 'MA Chidambaram Stadium, Chepauk, Chennai',
    'MA Chidambaram Stadium, Chepauk, Chennai': 'MA Chidambaram Stadium, Chepauk, Chennai',
    'MA Chidambaram Stadium': 'MA Chidambaram Stadium, Chepauk, Chennai',
    'Rajiv Gandhi International Stadium, Uppal': 'Rajiv Gandhi International Stadium, Hyderabad',
    'Rajiv Gandhi International Stadium': 'Rajiv Gandhi International Stadium, Hyderabad',
    'Rajiv Gandhi International Stadium, Uppal, Hyderabad': 'Rajiv Gandhi International Stadium, Hyderabad',
    'Dr DY Patil Sports Academy': 'Dr DY Patil Sports Academy, Mumbai',
    'Dr DY Patil Sports Academy, Mumbai': 'Dr DY Patil Sports Academy, Mumbai',
    'Vidarbha Cricket Association Stadium, Jamtha': 'Vidarbha Cricket Association Stadium, Nagpur',
    'Nehru Stadium': 'Nehru Stadium, Kochi',
    'Holkar Cricket Stadium': 'Holkar Cricket Stadium, Indore',
    'JSCA International Stadium Complex': 'JSCA International Stadium, Ranchi',
    'Sharjah Cricket Stadium': 'Sharjah Cricket Stadium, Sharjah',
    'Dubai International Cricket Stadium': 'Dubai International Cricket Stadium, Dubai',
    'Shaheed Veer Narayan Singh International Stadium': 'Shaheed Veer Narayan Singh International Stadium, Raipur',
    'Barsapara Cricket Stadium': 'Barsapara Cricket Stadium, Guwahati',
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium': 'Ekana Cricket Stadium, Lucknow',
    'Sawai Mansingh Stadium': 'Sawai Mansingh Stadium, Jaipur',
    'Sawai Mansingh Stadium, Jaipur': 'Sawai Mansingh Stadium, Jaipur',
    'Himachal Pradesh Cricket Association Stadium': 'Himachal Pradesh Cricket Association Stadium, Dharamsala',
    'Himachal Pradesh Cricket Association Stadium, Dharamsala': 'Himachal Pradesh Cricket Association Stadium, Dharamsala'
}

# Replace venue names in the 'venue' column
df['venue'] = df['venue'].replace(venue_replacements)

# Display the unique values after the replacements
print("Unique values in 'venue' after standardization:")
print(df['venue'].unique())

# Dictionary for team replacements
team_replacements = {
    'Royal Challengers Bengaluru': 'Royal Challengers Bangalore',
    'Rising Pune Supergiant': 'Rising Pune Supergiants',
    'Delhi Daredevils': 'Delhi Capitals',
    'Kings XI Punjab': 'Punjab Kings'
}

# Apply the replacements to the columns 'team1', 'team2', and 'toss_winner'
df['team1'] = df['team1'].replace(team_replacements)
df['team2'] = df['team2'].replace(team_replacements)
df['toss_winner'] = df['toss_winner'].replace(team_replacements)

# Display the unique values after the replacements
print("Unique values in 'team1' after standardization:")
print(df['team1'].unique())

print("Unique values in 'team2' after standardization:")
print(df['team2'].unique())

print("Unique values in 'toss_winner' after standardization:")
print(df['toss_winner'].unique())

# Apply the replacements to the 'winner' column
df['winner'] = df['winner'].replace(team_replacements)

# Display the unique values in 'winner' after standardization
print("Unique values in 'winner' after standardization:")
print(df['winner'].unique())

# Replace common umpire names in both columns using a dictionary for consistency
umpire_replacements = {
    'RE Koertzen': 'RE Koertzen',
    'SJA Taufel': 'SJA Taufel',
    'BF Bowden': 'BF Bowden',
    'MR Benson': 'MR Benson',
    'DJ Harper': 'DJ Harper',
    'Aleem Dar': 'Aleem Dar',
    'SJ Davis': 'SJ Davis',
    'IL Howell': 'IL Howell',
    # Add other umpire standardizations as needed
}

# Apply the replacements to both 'umpire1' and 'umpire2'
df['umpire1'] = df['umpire1'].replace(umpire_replacements)
df['umpire2'] = df['umpire2'].replace(umpire_replacements)

# Display the unique values in 'umpire1' and 'umpire2' after standardization
print("Unique values in 'umpire1' after standardization:")
print(df['umpire1'].unique())

print("Unique values in 'umpire2' after standardization:")
print(df['umpire2'].unique())

df.to_csv('cleaned_matches.csv')

dff = pd.read_csv('cleaned_matches.csv')

for column in df.columns:
    unique_values = df[column].unique()
    print(f"Unique values in '{column}':\n{unique_values}\n")

# Iterate over each column
for column in df.columns:
    # Get unique values and sort them alphabetically
    unique_values = sorted(df[column].dropna().unique())  # Sort values and drop nulls for sorting
    print(f"Unique values in '{column}' (sorted):\n{unique_values}\n")
for column in df.columns:
    # Count null values
    null_count = df[column].isnull().sum()
    print(f"Null values in '{column}': {null_count}\n")

# Fill missing values in 'player_of_match' with 'Unknown'
df['player_of_match'] = df['player_of_match'].fillna('Unknown')

# Fill missing values in 'winner' with 'No Winner'
df['winner'] = df['winner'].fillna('No ')

# Fill numerical columns with 0 (or another number)
df['target_runs'] = df['target_runs'].fillna(0)

# Fill missing values in numerical columns with the mean
df['target_runs'] = df['target_runs'].fillna(df['target_runs'].mean())

# Fill missing values in a categorical column with the mode
df['player_of_match'] = df['player_of_match'].fillna(df['player_of_match'].mode()[0])



# Forward fill missing values
df = df.ffill()

# Backward fill missing values
df = df.bfill()



# Example: Fill missing 'target_runs' with 0 if 'result' is 'No Result'
df['target_runs'] = df.apply(lambda row: 0 if pd.isna(row['target_runs']) and row['result'] == 'No Result' else row['target_runs'], axis=1)


# Flag rows where 'player_of_match' is missing
df['player_of_match_missing'] = df['player_of_match'].isna()

# Flag rows where 'winner' is missing
df['winner_missing'] = df['winner'].isna()

for column in df.columns:
    # Count null values
    null_count = df[column].isnull().sum()
    print(f"Null values in '{column}': {null_count}\n")

df.to_csv('cleaned_matches.csv')

x = df['team1'].value_counts()
y = df['team2'].value_counts()
(x+y).plot(kind='barh')

x = df['team1'].value_counts()
y = df['team2'].value_counts()
(x+y).plot(kind='barh')

x = pd.DataFrame({'winner':df['winner']}).value_counts()
print(x)

x.plot(kind='barh')
plt.title('Number of matches won by each team')
plt.xlabel('Number of wins')
plt.ylabel('Team Name')
plt.show()

df1 = pd.read_csv('deliveries.csv')

for column in df1.columns:
    # Count null values
    null_count = df1[column].isnull().sum()
    print(f"Null values in '{column}': {null_count}\n")
for column in df1.columns:
    unique_values = df1[column].unique()
    print(f"Unique values in '{column}':\n{unique_values}\n")

df1['extras_type'].fillna('None', inplace=True)
df1['player_dismissed'].fillna('None', inplace=True)
df1['dismissal_kind'].fillna('Not Out', inplace=True)
df1['fielder'].fillna('None', inplace=True)

player_name_mapping = {
    'SC Ganguly': 'Sourav Ganguly',
    'RT Ponting': 'Ricky Ponting',
    'V Kohli': 'Virat Kohli',
    'MS Dhoni': 'Mahendra Singh Dhoni',
    'SR Tendulkar': 'Sachin Tendulkar',
    'AB de Villiers': 'AB de Villiers',
    'SPD Smith': 'Steve Smith',
    'BB McCullum': 'Brendon McCullum',
    'DA Warner': 'David Warner',
    'CH Gayle': 'Chris Gayle',
    'MEK Hussey': 'Michael Hussey',
    'KA Pollard': 'Kieron Pollard',
    'SK Raina': 'Suresh Raina',
    'RG Sharma': 'Rohit Sharma',
    'AJ Finch': 'Aaron Finch',
    'DPMD Jayawardene': 'Mahela Jayawardene',
    'SE Marsh': 'Shaun Marsh',
    'JH Kallis': 'Jacques Kallis',
    'A Symonds': 'Andrew Symonds',
    'DJ Bravo': 'Dwayne Bravo',
    'Harbhajan Singh': 'Harbhajan Singh',
    'Z Khan': 'Zaheer Khan',
    'SL Malinga': 'Lasith Malinga',
    'B Kumar': 'Bhuvneshwar Kumar',
    'Imran Tahir': 'Imran Tahir',
    'R Ashwin': 'Ravichandran Ashwin',
    'JC Buttler': 'Jos Buttler',
    'Q de Kock': 'Quinton de Kock',
    'YK Pathan': 'Yusuf Pathan',
    'KP Pietersen': 'Kevin Pietersen',
    'MG Johnson': 'Mitchell Johnson',
    'AD Russell': 'Andre Russell',
    'SP Narine': 'Sunil Narine',
    'KD Karthik': 'Dinesh Karthik',
    'AM Rahane': 'Ajinkya Rahane',
    'SR Watson': 'Shane Watson',
    'R Dravid': 'Rahul Dravid',
    'PA Patel': 'Parthiv Patel',
    'Yuvraj Singh': 'Yuvraj Singh',

}

team_name_mapping = {
    'RCB': 'Royal Challengers Bangalore',
    'MI': 'Mumbai Indians',
    'KKR': 'Kolkata Knight Riders',
    'CSK': 'Chennai Super Kings',
    'SRH': 'Sunrisers Hyderabad',
    'RR': 'Rajasthan Royals',
    'DC': 'Delhi Capitals',
    'KXIP': 'Kings XI Punjab',
    'PBKS': 'Punjab Kings',  # Updated name
    'GL': 'Gujarat Lions',
    'PWI': 'Pune Warriors India',
    'RPS': 'Rising Pune Supergiants',
    'Kochi Tuskers Kerala': 'Kochi Tuskers Kerala',

}

venue_name_mapping = {
    'M Chinnaswamy Stadium': 'M. Chinnaswamy Stadium',
    'MA Chidambaram Stadium': 'M. A. Chidambaram Stadium',
    'Wankhede Stadium': 'Wankhede Stadium, Mumbai',
    'Eden Gardens': 'Eden Gardens, Kolkata',
    'Feroz Shah Kotla': 'Arun Jaitley Stadium',
    'Rajiv Gandhi Intl. Cricket Stadium': 'Rajiv Gandhi International Cricket Stadium',
    'Punjab Cricket Association Stadium': 'Punjab Cricket Association IS Bindra Stadium',
    'Sawai Mansingh Stadium': 'Sawai Mansingh Stadium, Jaipur',
    'Brabourne Stadium': 'Brabourne Stadium, Mumbai',
    'IS Bindra Stadium': 'Punjab Cricket Association IS Bindra Stadium',
    'DY Patil Stadium': 'DY Patil Stadium, Mumbai',
    'Sheikh Zayed Stadium': 'Sheikh Zayed Stadium, Abu Dhabi',
    'Sharjah Cricket Stadium': 'Sharjah Cricket Stadium, Sharjah',
    'Dubai Intl. Cricket Stadium': 'Dubai International Stadium',

}

for column in df.columns:
    print(column)

df1['player_dismissed'] = df1['player_dismissed'].replace(player_name_mapping)
df1['fielder'] = df1['fielder'].replace(player_name_mapping)

team_name_mapping = {
    "Delhi Daredevils": "Delhi Capitals",
    "Deccan Chargers": "Sunrisers Hyderabad",
    "Kochi Tuskers Kerala": "Kochi Tuskers",
    "Rising Pune Supergiants": "Rising Pune Supergiant",
    "Rajasthan Royals": "Rajasthan Royals"
}

# For df1 (deliveries dataset)
df1['batting_team'] = df1['batting_team'].replace(team_name_mapping)
df1['bowling_team'] = df1['bowling_team'].replace(team_name_mapping)

df1.rename(columns={
    'match_id': 'id',  # Matches the 'id' column in df
    'inning': 'inning',  # Keep 'inning' as is
    'batting_team': 'team1',  # Renamed to match 'team1' in df
    'bowling_team': 'team2',  # Renamed to match 'team2' in df
    'over': 'over',  # Keep 'over' as is
    'ball': 'ball',  # Keep 'ball' as is
    'batter': 'player_of_match',  # Renamed to match 'player_of_match' in df
    'bowler': 'bowler',  # Keep 'bowler' as is
    'non_striker': 'non_striker',  # Keep 'non_striker' as is
    'batsman_runs': 'batsman_runs',  # Keep 'batsman_runs' as is
    'extra_runs': 'extra_runs',  # Keep 'extra_runs' as is
    'total_runs': 'total_runs',  # Keep 'total_runs' as is
    'extras_type': 'extras_type',  # Keep 'extras_type' as is
    'is_wicket': 'is_wicket',  # Keep 'is_wicket' as is
    'player_dismissed': 'player_dismissed',  # Keep 'player_dismissed' as is
    'dismissal_kind': 'dismissal_kind',  # Keep 'dismissal_kind' as is
    'fielder': 'fielder'  # Keep 'fielder' as is
}, inplace=True)

df1['batsman_runs'].fillna(0, inplace=True)
df1['extra_runs'].fillna(0, inplace=True)
df1['total_runs'].fillna(0, inplace=True)
df1['is_wicket'].fillna(0, inplace=True)
df1['player_dismissed'].fillna('Not Dismissed', inplace=True)
df1['dismissal_kind'].fillna('Not Applicable', inplace=True)
df1['fielder'].fillna('Unknown', inplace=True)

# Step 5: Remove duplicates from df1 (deliveries dataset)
df1.drop_duplicates(inplace=True)

df1.rename(columns={
    'match_id': 'id',  # Matches the 'id' column in df
    'inning': 'inning',  # Keep 'inning' as is
    'batting_team': 'team1',  # Renamed to match 'team1' in df
    'bowling_team': 'team2',  # Renamed to match 'team2' in df
    'over': 'over',  # Keep 'over' as is
    'ball': 'ball',  # Keep 'ball' as is
    'batter': 'player_of_match',  # Renamed to match 'player_of_match' in df
    'bowler': 'bowler',  # Keep 'bowler' as is
    'non_striker': 'non_striker',  # Keep 'non_striker' as is
    'batsman_runs': 'batsman_runs',  # Keep 'batsman_runs' as is
    'extra_runs': 'extra_runs',  # Keep 'extra_runs' as is
    'total_runs': 'total_runs',  # Keep 'total_runs' as is
    'extras_type': 'extras_type',  # Keep 'extras_type' as is
    'is_wicket': 'is_wicket',  # Keep 'is_wicket' as is
    'player_dismissed': 'player_dismissed',  # Keep 'player_dismissed' as is
    'dismissal_kind': 'dismissal_kind',  # Keep 'dismissal_kind' as is
    'fielder': 'fielder'  # Keep 'fielder' as is
}, inplace=True)

df1['batsman_runs'].fillna(0, inplace=True)
df1['extra_runs'].fillna(0, inplace=True)
df1['total_runs'].fillna(0, inplace=True)
df1['is_wicket'].fillna(0, inplace=True)
df1['player_dismissed'].fillna('Not Dismissed', inplace=True)
df1['dismissal_kind'].fillna('Not Applicable', inplace=True)
df1['fielder'].fillna('Unknown', inplace=True)

df1['fielder'].fillna('Unknown', inplace=True)

# Step 6: Remove duplicates from df1 (deliveries dataset)
df1.drop_duplicates(inplace=True)

df1.to_csv('cleaned_deliveries.csv')
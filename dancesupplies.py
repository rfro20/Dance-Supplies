import numpy as np
import pandas as pd

def main():
    # Read in the CSV File with the rewards numbers and points
    rewards = pd.read_csv("rewards.csv")

    # Read in the CSV File with the customer information
    data = pd.read_csv("testdata.csv")

    # Add all phone numbers to a dictionary for constant lookup time
    rewards_map = {}
    for i in range(len(rewards)):
        rewards_map[rewards.iloc()[i,0]] = [rewards.iloc()[i,1], 0]

    output = pd.DataFrame(columns=["First Name", "Last Name", "E-Mail", "Registered Phone Number", "Points"])
    flagged_numbers = pd.DataFrame(columns=["Flagged Numbers"])

    # Iterate through each customer and check if any of their numbers are registered
    # If so, add them to the migrated data
    for i in range(len(data)):
        first_name = data.iloc()[i,0]
        last_name = data.iloc()[i,1]
        home_number = data.iloc()[i,2]
        mobile_number = data.iloc()[i,3]
        work_number = data.iloc()[i,4]
        email = data.iloc()[i,5]
        
        if not pd.isna(home_number):
            if home_number in rewards_map.keys():
                output.loc[len(output.index)] = [first_name, last_name, email, home_number, rewards_map[home_number][0]]
                rewards_map[home_number][1] = rewards_map[home_number][1] + 1

        if not pd.isna(mobile_number):
            if mobile_number in rewards_map.keys():
                output.loc[len(output.index)] = [first_name, last_name, email, mobile_number, rewards_map[mobile_number][0]]
                rewards_map[mobile_number][1] = rewards_map[mobile_number][1] + 1

        if not pd.isna(work_number):
            if work_number in rewards_map.keys():
                output.loc[len(output.index)] = [first_name, last_name, email, work_number, rewards_map[work_number][0]]
                rewards_map[work_number][1] = rewards_map[work_number][1] + 1

    # Check to see if any phone numbers have been registered more than once
    for number in rewards_map.keys():
        if rewards_map[number][1] == 0:
            output.loc[len(output.index)] = ["", "", "", number, rewards_map[number][0]]
        elif rewards_map[number][1] > 1:
            flagged_numbers.loc[len(flagged_numbers.index)] = [number]

    # Write output to CSV files
    output.to_csv("migration.csv")
    flagged_numbers.to_csv("flagged_numbers.csv")

main()

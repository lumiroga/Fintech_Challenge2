# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(bank_filtered_data):
    """Ask for the file path to save the bank filtered data 

    Returns:
        True or False if the file was saved succesfully
    """

    csvpath = questionary.text("Enter the file path where you want to store the bank filtered data with .csv extension").ask()
    csvpath = Path(csvpath)

    with open(csvpath,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(bank_filtered_data)
        return True
    
    return False

def save_qualifying_loans():
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """

    save_loan = questionary.confirm("Do you want to save the qualifying loans?").ask()

    return save_loan
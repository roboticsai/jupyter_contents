import pandas as pd
import numpy as np
import sys
sys.path.append('../')

def solution():
    #reading from the file Titanic_train.csv
    train=pd.read_csv('res/Titanic_train.csv')
    #view the dataset
    #print(train.head())
    '''Write your code here....
    .......
    .......
    '''
    #1. Print the total number of cells having missing values in the Age column.
    cells_having_missing_values = train['Age'].isnull().sum()
    list = []
    for index, row in train.iterrows():
        if pd.isnull(row['Age']):
            list.append(index)

    df1 = train.
    # Creating a list of the answer
    result=[cells_having_missing_values, sum(list), 300]
    # NOTE: Here, 100, 200 and 300 are the answer of 1st, 2nd and 3rd question respectively. Change it accordingly.

    # Finally create a dataframe of the final output  and write the output to output.csv

    result=pd.DataFrame(result)
    # writing output to output.csv
    result.to_csv('output/output.csv', header=False, index=False)
"""
THIS FILE IS LOCKED. IT IS RECOMMENDED THAT YOU DO NOT MODIFY THIS FILE. ANY MODIFICATIONS IN THIS FILE IS NOT CONSIDERED DURING THE EVALUATION OF THIS QUESTION.
"""

import pandas as pd
import sys
sys.path.append('../')

def solution():
    #reading from the file Titanic_train.csv
    train=pd.read_csv('res/Titanic_train.csv')
    #view the dataset
    print(train.head())
    '''Write your code here....
    .......
    .......
    '''
    # Creating a list of the answer
    result=[100, 200, 300]
    # NOTE: Here, 100, 200 and 300 are the answer of 1st, 2nd and 3rd question respectively. Change it accordingly.
    
    # Finally create a dataframe of the final output  and write the output to output.csv
    
    result=pd.DataFrame(result)
    # writing output to output.csv
    result.to_csv('output/output.csv', header=False, index=False)
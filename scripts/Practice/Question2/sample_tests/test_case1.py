"""
THIS FILE IS LOCKED. IT IS RECOMMENDED THAT YOU DO NOT MODIFY THIS FILE. ANY MODIFICATIONS IN THIS FILE IS NOT CONSIDERED DURING THE EVALUATION OF THIS QUESTION.
"""

import pandas as pd
import sys
sys.path.append('../')
from src import source

def test_sample():
    try:
        source.solution()
        
    except AttributeError:
        print("Expected function named solution() not found. Please use the code provided in the stub file to write your code in the correct format.")
        assert True==False

    except TypeError:
        print("Please do not pass any arguments to the function solution(). Use the code provided in the stub file to write your code in the correct format.")
        assert True==False
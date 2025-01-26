"""
Module: utils_kleopold

Purpose: To show roller skate sales data collected.

Description: This data was collected over a 12 month period.
The goal is to determine if there are enough sales to continue
to stock roller skates in our stores.

Author: Kellie Leopold

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
sells_roller_skates: bool = True
sells_roller_skate_accessories: bool = False

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
skate_brands_in_stock: int = 4

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_sales_per_month: float = 77.7

# declare a list of strings
# TODO: Add or replace this with your own list  
skate_brands_sold: list = ["Moxi Roller Skates", "Impala Roller Skates", "Riedell", "Sure Grip"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
customer_review_scores: list = [9.5, 4.7, 8.2, 7.0, 6.3]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_score: float = min(customer_review_scores)  
max_score: float = max(customer_review_scores)  
mean_score: float = statistics.mean(customer_review_scores)  
stdev_score: float = statistics.stdev(customer_review_scores)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Roller Skate Sales Data
---------------------------------------------------------
We Sell Roller Skates:    {sells_roller_skates}
We Sell Roller Skate Accessories:    {sells_roller_skate_accessories}
Number of Roller Skate Brands in Stock:    {skate_brands_in_stock}
Average Roller Skate Sales Per Month:    {average_sales_per_month}
Skate Brands Sold:    {skate_brands_sold}
Customer Review Scores:    {customer_review_scores}
Minimum Review Score:    {min_score}
Maximum Review Score:    {max_score}
Mean Review Score:    {mean_score:.2f}
Standard Deviation of Review Scores:    {stdev_score:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.

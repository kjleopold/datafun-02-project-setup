'''
Module: kleopold_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Kellie Leopold

'''

#####################################
# Import Modules at the Top
#####################################

# Import modules from standard library
import pathlib
import time

# Import local modules
import utils_kleopold

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")
    
    # Loop through a range of years and include end year
    for year in range(start_year, end_year + 1): 
        folder_name = data_path.joinpath(str(year)) # Create the folder path
        folder_name.mkdir(exist_ok=True) # Create the folder if it doesn't already exist
        print(f"Folder Created: {folder_name}") # Log the folder creation
   

  
#####################################
# Define Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool, remove_spaces: bool) -> None:
    '''
    Create folders from a list of folder names, with optional transformations.
    
    Arguments:
        folder_list -- A list of folder names to create.
        to_lowercase -- Convert folder names to lowercase, if True.
        remove_spaces -- Removes spaces from folder names, if True.
    '''

    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}, to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")
    
    # Process each folder name from the list
    for folder_name in folder_list:
        # Transform the folder name if options are True.
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "")

        folder_path = data_path.joinpath(folder_name) # Join the folder name to the path
        folder_path.mkdir(exist_ok=True) # Create the folder if it doesn't already exist
        print(f"Folder Created: {folder_path}") # Confirm the folder was created


  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Adds a prefix to each folder name in the list and creates them at the specified path.
    
    Arguments:
        folder_list -- A list of folder names.
        prefix -- The prefix to be added to the folder name.
    '''
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list:{folder_list} and prefix={prefix}")
    
    # Process each folder name from the list
    for folder_name in folder_list:
        prefixed_name = prefix + folder_name # Add a prefix to the folder name
        folder_path = data_path.joinpath(prefixed_name) # Join the folder name to the path
        folder_path.mkdir(exist_ok=True) # Create the folder if it doesn't already exist
        print(f"Folder Created: {folder_path}") # Confirm the folder was created

  

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Periodically create a new folder from list of folder names after a predefined delay in seconds
    
    Arguments:
        duration_seconds -- The total duration for creating folders (in seconds).
    '''
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")

    # Initialize the folder counter and start time
    folder_count = 1
    while folder_count <= 7:
    
    # Create a folder with a sequence number
        folder_name = f"new_folder{folder_count}"
        folder_path = data_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=True) # Create folder if it doesn't exist
        print(f"Folder Created: {folder_path}") # Confirm the folder was created

        folder_count += 1
        time.sleep(duration_seconds)


#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_kleopold.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=1985, end_year=1990)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names, to_lowercase=True, remove_spaces=True)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 3 # duration in seconds
    create_folders_periodically(duration_secs)

    # TODO: Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
        "North America",
        "South America",
        "Europe",
        "Asia",
        "Africa",
        "Oceania",
        "Middle East"
        ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.
print("This code ran perfectly.")

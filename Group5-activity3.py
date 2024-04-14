# Group 5
# Activity 3 (CLI: Command Line Interface)

"""
# Names:-

- Ahmed Ali
- Mohammad Ali
- Naqiya
- Yaseen Gaber

# Contribution:-

- Ahmed Ali ---> 'clean_and_prepare_data' function ~ (25%)
- Mohammad Ali ---> 'load_data' function and 'main()' function ~ (25%)
- Naqiya ---> 'analyze_data' function ~ (25%)
- Yaseen Gaber ---> 'visualize_data' function ~ (25%)

# Description:-

- Python script designed to handle CSV files...
It contains 4 primary functions: Load Data; Clean and prepare data; Analyze data; Visualize and present the data.

- User enters the file path however if it doesn't exist an error message is provided...
Now the file is processed for each stage step by step.

- There are columns in the file: Branch / Product / Price / Units sold...
For the 'Price' column, it calculates the minimum/maximum/average of non-empty cells, replaces empty cells with this average, and prints the updated data...
Similarly, for the 'Units sold' column, it calculates the minimum/maximum/average and replaces empty cells.
These operations ensure data integrity by handling empty values appropriately, enhancing the accuracy of subsequent analysis.

* The file cursor is used to reset file pointer to the beginning of the CSV file, and the file is updated with the replacement values...
after that, the data is restructured into its original format and printed to the console, ensuring consistency.

- Next step is the process of sorting the data in the selected column ('Price' or 'Units sold') either in ascending or descending order...
It first confirms the column selected by the user ('Price' or 'Units sold'). Then, it asks the user to choose the sorting order: ascending or descending...
After getting the user's input, the code implements the insertion sort algorithm to sort the data accordingly...
For ascending order, it compares each element with the previous ones and moves it to the correct position...
Likewise, for descending order, it compares each element with the previous ones and moves it to the correct position accordingly.

- Once the sorting is done, it replaces the original column data with the sorted values. Finally, it prints the updated table with the sorted column values.
This functionality enhances the data analysis capability by allowing users to sort the data in the selected column in either ascending or descending order, facilitating easier interpretation and analysis.
Lastly, the 'analyze_data' function updates the CSV file with the sorted data and displayes the updated table.

- Finally, 'visualize_data' function checks the selected column, processes the data, and displays it using asterisks...
The function gracefully handles non-numeric values and relies on robust file handling for accurate visualization.

# Github:-

- Mohammad Ali: https://github.com/MohammadAlSubaiei/GCIS
- Naqiya: https://github.com/naqiyahathiari/group.git
- Yaseen Gaber: https://github.com/Yaseen-Gaber/Group_5.git
- Ahmed Ali: https://github.com/Aah353/aah5142.git
"""

# csv module is imported to ease the use of 'comma separated value' files
import csv

# After stage 2, 'PROCESSED_COLUMN' list (constant) aids in maintaing the selected column in stage 3 and 4.
PROCESSED_COLUM = []

# the 'load_data' function takes a parameter 'csvfile' (for user input)
def load_data(csvfile):
    '''
this function opens the selected CSV file, after that the CSV reader attribute is initialized as a variable called 'reader'.
The file is passed as an argument to 'reader', then the function checks if the file exists using 'try' and 'except' FileNotFoundError.
If the file is found (existing), then the function prints the contents of the CSV file to the console with a feedback message indicating successfull loading.
    '''
    # open the csv file using 'with open' that opens the file to perform operations and then close it back instead of using file.open() and file.close()
    with open(csvfile) as file:
        # initialize a 'reader' object using 'csv.reader()' method
        reader = csv.reader(file)
        # skipping the headers will affect the way the file looks, hence leading to false informaiton (SemanticError)
        '''
        next(reader)
        '''
        # print the contents of the file
        for line in reader:
            print(line)
        print("\nFile successfully loaded!")
        
# again, the 'clean_and_prepare_data' function takes a pramater 'csvfile' (for user input)
def clean_and_prepare_data(csv_file):
    '''
The "clean_and_prepare_data" function facilitates data cleaning and preparation for a selected column in a CSV file.
It first prompts the user to choose from available columns, ensuring a valid selection.

If the chosen column contains numerical data (i.e., 'Price' or 'Units sold')...
it offers options to replace empty values with either the minimum, maximum, or average of the existing data.

After validating the operation selection, it executes the chosen operation to handle empty values in the column.
Once completed, the function confirms the successful replacement of empty values.

Overall, clean_and_prepare_data guides users through the process of selecting and preparing a column, enhancing the data's integrity for subsequent analysis.
    '''
    def minimum(csv_file):
        '''
this function is designed to find the minimum from the selected column in a CSV file.
it will substitute the empty cells with the minimum value found.

Initially, it first checks to whether the chosen column is either 'Price' or 'Unites sold'...
then it performs next step which is replacing the minimum value in the selected column in the file.

The replacement process is implemented as follows:-

- It indicates minimum value in the 'Price' column (if selected) and replaces all empty cells with the value.
- Likewise, if the selected column is 'Units sold', it finds the least value in the column and then populates the empty cells with the information.

Upon completion, it prints the updated table which includes the empty cells that are replaced.
This function makes use of file handling consistently to perform the algorithm tasks exclusively.
        '''
        # check if the entered input is either 'Price' or 'Units sold'
        if COLUMN_NAME == "Price" or COLUMN_NAME == "Units sold":
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                # Skip the header row
                next(reader)
                if COLUMN_NAME == "Price":
                    # print the index of the column. helpful info
                    print(f"\nColumn '{COLUMN_NAME}' found at index 2.")
                elif COLUMN_NAME == "Units sold":
                    # print the index of the column. helpful info
                    print(f"\nColumn '{COLUMN_NAME}' found at index 3.")

                # initialize variables for implementation of the ALGORITHM
                empty_space = ' '
                replacement_count = 0
                # check if the selected column is 'Price'
                if COLUMN_NAME == "Price":
                    # create the list that stores the array
                    price_values = []
                    # Iterate over the rows of the 'reader' object
                    for row in reader:
                        # add the contents of 'Price' column to the list 
                        price_values.append(row[2])
                    # Print the value in the Price column (index 2)
                    print("\nStored data:", price_values)
                    # check if 'price_values' list is NOT empty
                    if price_values:
                        # convert the first value in the list to integer and store that integer into a varaible called 'minimum_price'
                        minimum_price = int(price_values[0])
                        # Iterate over the 'price_values' list starting from the second element/index/string
                        for value in price_values[1:]:
                            # check if the 'value' in the for loop does not equal an empty space (' ')
                            if value != empty_space:
                                try:
                                    # convert each value to Type 'int' and store it to 'numeric_value' variable
                                    numeric_value = int(value)
                                    # compare 'numeric_value' in each iteration to the first value in the list
                                    if numeric_value < minimum_price:
                                        # if it's less than, then assign (replace) the number to the 'minimum_price' (first value) and update it
                                        minimum_price = numeric_value
                                # if there's a non-numeric value in the column selected, it's skipped using 'continue'
                                except ValueError:
                                    continue
                        # print the found minimum value/number/integer from the list onto the screen
                        print("\nMinimum found:", minimum_price)

                    # Iterate over the length of the 'price_values' list to find the empty space and replace it with the found minimum
                    for i in range(len(price_values)):
                        # if the index of 'price_values' is an empty space and the number of cells in that row does not exceed (less than or equal to) 8...
                        if price_values[i] == empty_space and replacement_count <= 8:
                            # then, assign (replace) that index to the 'minimum_price' value of Type 'str'
                            price_values[i] = str(minimum_price)
                            # increment the counter by one during each iteration
                            replacement_count += 1
                    # print the replaced data onto the screen
                    print("\nReplaced data:", price_values)
                    
                    """
file.seek(0) is used to move the file cursor (the position from where the next read or write operation will occur) to the beginning of the file before iterating over the file contents again.

Without file.seek(0), if you try to read the file again without closing and reopening it, you'll be at the end of the file.

So, basically it resets the cursor to the beginning of the file before re-reading it.
                    """
                    
                    file.seek(0)
                    # assign the 'str' Type of the 'minimum_price' variable to 'replacement_value_price'
                    replacement_value_price = str(minimum_price)
                    # initialize 'updated_price' list
                    updated_price = []
                    # Iterate over the rows of the file
                    for row in reader:
                        # assign the stripped (removed whitespaces) version of row[2] (index 2 [Price column]) to 'price_cell'
                        price_cell = row[2].strip()
                        # check if 'price_cell' is an empty string and row[2] is an empty string
                        '''
                        this ensures that both conditions (empty strings and ONLY strings) are True instead of causing SemanticError
                        '''
                        if price_cell == '' and row[2].strip() == '':
                            # replace the empty string in row[2] to the value defined above (replacement_value_price) 
                            row[2] = replacement_value_price
                        # 'extend' option is used to discard the square brackets of the file
                        '''
                        if 'append' is used, then the output will be a list of lists (SemanticError)
                        '''
                        updated_price.extend(row)
                    
                    # print a new-line onto the screen
                    print()
                    # 'chunks' is assigned to a list comprehension to organize the contents/data back to previous form (form: same as the file appreanace)
                    '''
                    Create 4-field row sublists:

                    arranging 'updated_price' list into chunks consisting of 4-field row sublists (just like the file) for 'writing' purposes
                    'writing' ---> writer.writerow(VARIABLE), for updating the file
                    '''
                    updated_price_chunks = [updated_price[i:i+4] for i in range(0, len(updated_price), 4)]
                    # Iterate over the length of 'chunks' and assign the index to a list comprehension that prints the rows horizontally
                    for i in range(len(updated_price_chunks)):
                        updated_price_chunks[i] = [field.strip() for field in updated_price_chunks[i]]

                # check if the selected column is 'Units sold'
                elif COLUMN_NAME == "Units sold":
                    # create the list that stores the array
                    units_sold_values = []
                    # Iterate over the rows of the 'reader' object
                    for row in reader:
                        # add the contents of 'Units sold' column to the list
                        units_sold_values.append(row[3])
                    # Print the value in the Units sold column (index 3)
                    print("\nStored data:", units_sold_values)
                    # check if 'price_values' list is NOT empty
                    if units_sold_values:
                        # convert the first value in the list to integer and store that integer into a varaible called 'minimum_units_sold'
                        minimum_units_sold = int(units_sold_values[0])
                        # Iterate over the 'units_sold_values' list starting from the second element/index/string
                        for value in units_sold_values[1:]:
                            # check if the 'value' in the for loop does not equal an empty space (' ')
                            if value != empty_space:
                                try:
                                    # convert each value to Type 'int' and store it to 'numeric_value' variable
                                    numeric_value = int(value)
                                    # compare 'numeric_value' in each iteration to the first value in the list
                                    if numeric_value < minimum_units_sold:
                                        # if it's less than, then assign (replace) the number to the 'minimum_units_sold' (first value) and update it
                                        minimum_units_sold = numeric_value
                                # if there's a non-numeric value in the column selected, it's skipped using 'continue'
                                except ValueError:
                                    continue
                        # print the found minimum value/number/integer from the list onto the screen
                        print("\nMinimum found:", minimum_units_sold)
                    
                    # Iterate over the length of the 'units_sold_values' list to find the empty space and replace it with the found minimum
                    for i in range(len(units_sold_values)):
                        # if the index of 'price_values' is an empty space and the number of cells in that row does not exceed (less than or equal to) 7...
                        if units_sold_values[i] == empty_space and replacement_count <= 7:
                            # then, assign (replace) that index to the 'minimum_units_sold' value of Type 'str'
                            units_sold_values[i] = str(minimum_units_sold)
                            # increment the counter by one during each iteration
                            replacement_count += 1
                    # print the replaced data onto the screen
                    print("\nReplaced data:", units_sold_values)

                    # reset the cursor to the beginning of the file before re-reading it
                    file.seek(0)
                    # assign the 'str' Type of the 'minimum_price' variable to 'replacement_value_units_sold'
                    replacement_value_units_sold = str(minimum_units_sold)
                    # initialize 'updated_units_sold' list
                    updated_units_sold = []
                    # Iterate over the rows of the file
                    for row in reader:
                        # assign the stripped (removed whitespaces) version of row[3] (index 3 [Units sold column]) to 'units_sold_cell'
                        units_sold_cell = row[3].strip()
                        # check if 'units_sold_cell' is an empty string and row[3] is an empty string
                        '''
                        this ensures that both conditions (empty strings and ONLY strings) are True instead of causing SemanticError
                        '''
                        if units_sold_cell == '' and row[3].strip() == '':
                            # replace the empty string in row[3] to the value defined above (replacement_value_units_sold)
                            row[3] = replacement_value_units_sold
                        '''
                        if 'append' is used, then the output will be a list of lists (SemanticError)
                        '''
                        updated_units_sold.extend(row)
                    
                    # print a new-line
                    print()
                    # 'chunks' is assigned to a list comprehension to organize the contents/data back to previous form (form: same as the file appreanace)
                    '''
                    Create 4-field row sublists:

                    arranging 'updated_price' list into chunks consisting of 4-field row sublists (just like the file) for 'writing' purposes
                    'writing' ---> writer.writerow(VARIABLE), for updating the file
                    '''
                    updated_units_sold_chunks = [updated_units_sold[i:i+4] for i in range(0, len(updated_units_sold), 4)]
                    # Iterate over the length of 'chunks' and assign the index to a list comprehension that prints the rows horizontally
                    for i in range(len(updated_units_sold_chunks)):
                        updated_units_sold_chunks[i] = [field.strip() for field in updated_units_sold_chunks[i]]
            
            # open the csv file in write mode and use the argument ('') with the built-in parameter 'newline='
            '''
The newline='' parameter prevents Python from automatically appending newline characters (\n) to each line in the file.
This helps to avoid the addition of extra blank lines between rows in the output CSV file.
            '''
            with open(csv_file, 'w', newline='') as file:
                # Create writer object to write to file for the purpose of updating the data
                writer = csv.writer(file)
                # because 'minimum' function acts as a supplementary function. it's preferred to refer to the same constant of the outer function
                if COLUMN_NAME == "Price":
                    # Iterate over the newly replaced list
                    for row in updated_price_chunks:
                        # write (update) the new data to the file for later printing
                        writer.writerow(row)
                # else if the other column name...
                elif COLUMN_NAME == "Units sold":
                    # Iterate over the newly replaced list
                    for row in updated_units_sold_chunks:
                        # write (update) the new data to the file for later printing
                        writer.writerow(row)

        # Print updated table with replaced values
        print("Updated table with replaced values using minimum values:\n")
        with open(csv_file) as file:
            reader = csv.reader(file)
            for line in reader:
                print(line)

# ---------------------------------------------------------------------------------------------------------------------------------

    def maximum(csv_file):
        '''
The maximum function is designed to find the maximum value from the selected column in a CSV file and substitute any empty cells with this maximum value.
Initially, it checks whether the chosen column is either 'Price' or 'Units sold'. Then, it proceeds to find and replace the maximum value in the selected column in the file.

The replacement process is executed as follows:-

- It identifies the maximum value in the 'Price' column (if selected) and replaces all empty cells with this value.
- Similarly, if the selected column is 'Units sold', it locates the maximum value in the column and fills the empty cells with this information.

Upon completion, the function prints the updated table, showcasing the replaced empty cells with their respective maximum values.
Throughout its execution, this function relies on consistent file handling techniques to perform the algorithmic tasks effectively and accurately.
        '''
        # check if the entered input is either 'Price' or 'Units sold'
        if COLUMN_NAME == "Price" or COLUMN_NAME == "Units sold":
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                # Skip the header row
                next(reader)
                if COLUMN_NAME == "Price":
                    # print the index of the column. helpful info
                    print(f"\nColumn '{COLUMN_NAME}' found at index 2.")
                elif COLUMN_NAME == "Units sold":
                    # print the index of the column. helpful info
                    print(f"\nColumn '{COLUMN_NAME}' found at index 3.")

                # initialize variables for implementation of the ALGORITHM
                empty_space = ' '
                replacement_count = 0
                # check if the selected column is 'Price'
                if COLUMN_NAME == "Price":
                    # create the list that stores the array
                    price_values = []
                    # Iterate over the rows of the 'reader' object
                    for row in reader:
                        # add the contents of 'Price' column to the list 
                        price_values.append(row[2])
                    # Print the values in the Price column (index 2)
                    print("\nStored data:", price_values)  
                    # # check if 'price_values' list is NOT empty
                    if price_values:
                        # convert the first value in the list to integer and store that integer into a varaible called 'minimum_price'
                        maximum_price = int(price_values[0])
                        # Iterate over the 'price_values' list starting from the second element/index/string
                        for value in price_values[1:]:
                            # check if the 'value' in the for loop does not equal an empty space (' ')
                            if value != empty_space:
                                try:
                                    # convert each value to Type 'int' and store it to 'numeric_value' variable
                                    numeric_value = int(value)
                                    # Compare 'numeric_value' in each iteration to the first value in the list
                                    if numeric_value > maximum_price:
                                        # if it's less than, then assign (replace) the number to the 'minimum_price' (first value) and update it
                                        maximum_price = numeric_value
                                # if there's a non-numeric value in the column selected, it's skipped using 'continue'
                                except ValueError:
                                    continue
                        # print the found minimum value/number/integer from the list onto the screen
                        print("\nMaximum found:", maximum_price)
                    
                    # Iterate over the length of the 'price_values' list to find the empty space and replace it with the found minimum
                    for i in range(len(price_values)):
                        # if the index of 'price_values' is an empty space and the number of cells in that row does not exceed (less than or equal to) 8...
                        if price_values[i] == empty_space and replacement_count <=8:
                            # then, assign (replace) that index to the 'minimum_price' value of Type 'str'
                            price_values[i] = str(maximum_price)
                            # increment the counter by one during each iteration
                            replacement_count += 1
                    # print the replaced data onto the screen
                    print("\nReplaced data:", price_values)

                    """
file.seek(0) is used to move the file cursor (the position from where the next read or write operation will occur) to the beginning of the file before iterating over the file contents again.

Without file.seek(0), if you try to read the file again without closing and reopening it, you'll be at the end of the file.

So, basically it resets the cursor to the beginning of the file before re-reading it.
                    """

                    file.seek(0)
                    # assign the 'str' Type of the 'minimum_price' variable to 'replacement_value_price'
                    replacement_value_price = str(maximum_price)
                    # initialize 'updated_price' list
                    updated_price = []
                    # Iterate over the rows of the file
                    for row in reader:
                        # assign the stripped (removed whitespaces) version of row[2] (index 2 [Price column]) to 'price_cell'
                        price_cell = row[2].strip()
                        # check if 'price_cell' is an empty string and row[2] is an empty string
                        '''
                        this ensures that both conditions (empty strings and ONLY strings) are True instead of causing SemanticError
                        '''
                        if price_cell == '' and row[2].strip() == '':
                            # replace the empty string in row[2] to the value defined above (replacement_value_price) 
                            row[2] = replacement_value_price
                        # 'extend' option is used to discard the square brackets of the file
                        '''
                        if 'append' is used, then the output will be a list of lists (SemanticError)
                        '''
                        updated_price.extend(row)
                        
                    # print a new-line onto the screen
                    print()
                    # 'chunks' is assigned to a list comprehension to organize the contents/data back to previous form (form: same as the file appreanace)
                    '''
                    Create 4-field row sublists:

                    arranging 'updated_price' list into chunks consisting of 4-field row sublists (just like the file) for 'writing' purposes
                    'writing' ---> writer.writerow(VARIABLE), for updating the file
                    '''
                    updated_price_chunks = [updated_price[i:i+4] for i in range(0, len(updated_price), 4)]
                    # Iterate over the length of 'chunks' and assign the index to a list comprehension that prints the rows horizontally
                    for i in range(len(updated_price_chunks)):
                        updated_price_chunks[i] = [field.strip() for field in updated_price_chunks[i]]
                
                # check if the selected column is 'Units sold'
                elif COLUMN_NAME == "Units sold":
                    # create the list that stores the array
                    units_sold_values = []
                    # Iterate over the rows of the 'reader' object
                    for row in reader:
                        # add the contents of 'Units sold' column to the list
                        units_sold_values.append(row[3])
                    # Print the value in the Units sold column (index 3)
                    print("\nStored data:", units_sold_values)
                    # check if 'price_values' list is NOT empty
                    if units_sold_values:
                        # convert the first value in the list to integer and store that integer into a varaible called 'maximum_units_sold'
                        maximum_units_sold = int(units_sold_values[0])
                        # Iterate over the 'units_sold_values' list starting from the second element/index/string
                        for value in units_sold_values[1:]:
                            # check if the 'value' in the for loop does not equal an empty space (' ')\
                            if value != empty_space:
                                try:
                                    # convert each value to Type 'int' and store it to 'numeric_value' variable
                                    numeric_value = int(value)
                                    # compare 'numeric_value' in each iteration to the first value in the list
                                    if numeric_value < maximum_units_sold:
                                        # if it's less than, then assign (replace) the number to the 'maximum_units_sold' (first value) and update it
                                        maximum_units_sold = numeric_value
                                # if there's a non-numeric value in the column selected, it's skipped using 'continue'
                                except ValueError:
                                    continue
                        # print the found minimum value/number/integer from the list onto the screen
                        print("\nMaximum found:", maximum_units_sold)
                    
                    # Iterate over the length of the 'units_sold_values' list to find the empty space and replace it with the found minimum
                    for i in range(len(units_sold_values)):
                        # if the index of 'price_values' is an empty space and the number of cells in that row does not exceed (less than or equal to) 7...
                        if units_sold_values[i] == empty_space and replacement_count <= 7:
                            # then, assign (replace) that index to the 'maximum_units_sold' value of Type 'str'
                            units_sold_values[i] = str(maximum_units_sold)
                            # increment the counter by one during each iteration
                            replacement_count += 1
                    # print the replaced data onto the screen
                    print("\nReplaced data:", units_sold_values)
                    
                    # reset the cursor to the beginning of the file before re-reading it
                    file.seek(0)
                    # assign the 'str' Type of the 'minimum_price' variable to 'replacement_value_units_sold'
                    replacement_value_units_sold = str(maximum_units_sold)
                    # initialize 'updated_units_sold' list
                    updated_units_sold = []
                    # Iterate over the rows of the file
                    for row in reader:
                        # assign the stripped (removed whitespaces) version of row[3] (index 3 [Units sold column]) to 'units_sold_cell'
                        units_sold_cell = row[3].strip()
                        # check if 'units_sold_cell' is an empty string and row[3] is an empty string
                        '''
                        this ensures that both conditions (empty strings and ONLY strings) are True instead of causing SemanticError
                        '''
                        if units_sold_cell == '' and row[3].strip() == '':
                            # replace the empty string in row[3] to the value defined above (replacement_value_units_sold)
                            row[3] = replacement_value_units_sold
                        '''
                        if 'append' is used, then the output will be a list of lists (SemanticError)
                        '''
                        updated_units_sold.extend(row)
                        
                    # print a new-line
                    print()
                    # 'chunks' is assigned to a list comprehension to organize the contents/data back to previous form (form: same as the file appreanace)
                    '''
                    Create 4-field row sublists:

                    arranging 'updated_price' list into chunks consisting of 4-field row sublists (just like the file) for 'writing' purposes
                    'writing' ---> writer.writerow(VARIABLE), for updating the file
                    '''
                    updated_units_sold_chunks = [updated_units_sold[i:i+4] for i in range(0, len(updated_units_sold), 4)]
                    # Iterate over the length of 'chunks' and assign the index to a list comprehension that prints the rows horizontally
                    for i in range(len(updated_units_sold_chunks)):
                        updated_units_sold_chunks[i] = [field.strip() for field in updated_units_sold_chunks[i]]

            # open the csv file in write mode and use the argument ('') with the built-in parameter 'newline='
            '''
The newline='' parameter prevents Python from automatically appending newline characters (\n) to each line in the file.
This helps to avoid the addition of extra blank lines between rows in the output CSV file.
            '''
            with open(csv_file, 'w', newline='') as file:
                # Create writer object to write to file for the purpose of updating the data
                writer = csv.writer(file)
                # because 'maximum' function acts as a supplementary function. it's preferred to refer to the same constant of the outer function
                if COLUMN_NAME == "Price":
                    # Iterate over the newly replaced list
                    for row in updated_price_chunks:
                        # write (update) the new data to the file for later printing
                        writer.writerow(row)
                # else if the other column name...
                elif COLUMN_NAME == "Units sold":
                    # Iterate over the newly replaced list
                    for row in updated_units_sold_chunks:
                        # write (update) the new data to the file for later printing
                        writer.writerow(row)

        # Print updated table with replaced values
        print("Updated table with replaced values using maximum values:\n")
        with open(csv_file) as file:
            reader = csv.reader(file)
            for line in reader:
                print(line)

# ---------------------------------------------------------------------------------------------------------------------------------

    def average(csv_file):
        '''
The average function works in the same manner as the others, finding the average value of the column the user selects to replace any empty cells with this average value.
Primarily, it makes sure that the selected column is either the 'Price' or 'Units sold'...
Then, it moves over to do the averaging calculation of the cells and substitutes the empty ones with the average values from the column in the source file.

The replacement process unfolds as follows:-

- If the user selects 'Price' as the column, it calculates the average of all non-empty cell's value in the column and replaces the cells without data with this number.
- Likewise, when the selected column is "Units sold", it fills the empty cells with this average value of the non-empty cells.

Upon completion, the function outputs the processed table, demonstrating the replaced cells, which now contain their average value.
File handling techniques are often used to perform the neccessary algorithms of this function deliberately and accurately.
        '''
        # check if the entered input is either 'Price' or 'Units sold'
        if COLUMN_NAME == "Price" or COLUMN_NAME == "Units sold":
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                # Skip the header row
                next(reader)
                if COLUMN_NAME == "Price":
                    # print the index of the column. helpful info
                    print(f"\nColumn name '{COLUMN_NAME}' found at index 2")
                    # print the index of the column. helpful info
                elif COLUMN_NAME == "Units sold":
                    print(f"\nColumn name '{COLUMN_NAME}' found at index 3")
                
                # initialize variables for implementation of the ALGORITHM
                empty_space = ' '
                replacement_count = 0
                units_sold_sum = 0
                price_sum = 0
                units_sold_count = 0
                price_count = 0
                # check if the selected column is 'Price'
                if COLUMN_NAME == "Price":
                    # create the list that stores the array
                    price_values = []
                    # Iterate over the rows of the 'reader' object
                    for row in reader:
                        # add the contents of 'Price' column to the list 
                        price_values.append(row[2])
                    # Print the values in the Price column (index 2)
                    print("\nStored data:", price_values)
                    # check if 'price_values' list is NOT empty
                    if price_values:
                        # Iterate over the 'price_values' list starting from the second element/index/string
                        for value in price_values:
                            # check if the 'value' in the for loop does not equal an empty space (' ')
                            if value != empty_space:
                                try:
                                    # convert each value to Type 'int'
                                    value = int(value)
                                    # increment 'price_sum' for later average calculation...
                                    price_sum += value
                                    # increment 'price_count' for later average calculation...
                                    price_count += 1
                                # if there's a non-numeric value in the column selected, a warning message appears
                                except ValueError:
                                    print("Warning: Non-numeric value found in 'Price' column.")
                    
                    # Calculate average of 'Price' column (the use of '//' is because of the Type) | '//' ---> int & '/' ---> float
                    price_average = price_sum // price_count if price_count != 0 else 0
                    # print the calculated average
                    print("\nCalculated Average:", price_average)
                    # Iterate over the length of the 'price_values' list
                    for i in range(len(price_values)):
                        # if the index of the list during iteration is an empty space and the amount of cells is less than or equal to 8...
                        if price_values[i] == empty_space and replacement_count <= 8:
                            # replace/overwrite that empty space with the 'str' version of the calculated average
                            price_values[i] = str(price_average)
                            # increment the count by 1 for each iteration of the list
                            replacement_count += 1
                    # print the replaced data onto the screen
                    print("\nReplaced data:", price_values)

                    """
file.seek(0) is used to move the file cursor (the position from where the next read or write operation will occur) to the beginning of the file before iterating over the file contents again.

Without file.seek(0), if you try to read the file again without closing and reopening it, you'll be at the end of the file.

So, basically it resets the cursor to the beginning of the file before re-reading it.
                    """

                    file.seek(0)
                    # assign the 'str' Type of the 'price_average' variable to 'replacement_value_price'
                    replacement_value_price = str(price_average)
                    # initialize 'updated_price' list
                    updated_price = []
                    # Iterate over the rows of the file
                    for row in reader:
                        # assign the stripped (removed whitespaces) version of row[2] (index 2 [Price column]) to 'price_cell'
                        price_cell = row[2].strip()
                        # check if 'price_cell' is an empty string and row[2] is an empty string
                        '''
                        this ensures that both conditions (empty strings and ONLY strings) are True instead of causing SemanticError
                        '''
                        if price_cell == '' and row[2].strip() == '':
                            # replace the empty string in row[2] to the value defined above (replacement_value_price) 
                            row[2] = replacement_value_price
                        # 'extend' option is used to discard the square brackets of the file
                        '''
                        if 'append' is used, then the output will be a list of lists (SemanticError)
                        '''
                        updated_price.extend(row)

                    # print a new-line onto the screen
                    print()
                    # 'chunks' is assigned to a list comprehension to organize the contents/data back to previous form (form: same as the file appreanace)
                    '''
                    Create 4-field row sublists:

                    arranging 'updated_price' list into chunks consisting of 4-field row sublists (just like the file) for 'writing' purposes
                    'writing' ---> writer.writerow(VARIABLE), for updating the file
                    '''
                    updated_price_chunks = [updated_price[i:i+4] for i in range(0, len(updated_price), 4)]
                    # Iterate over the length of 'chunks' and assign the index to a list comprehension that prints the rows horizontally
                    for i in range(len(updated_price_chunks)):
                        updated_price_chunks[i] = [field.strip() for field in updated_price_chunks[i]]
                
                # check if the selected column is 'Units sold'
                elif COLUMN_NAME == "Units sold":
                    # create the list that stores the array
                    units_sold_values = []
                    # Iterate over the rows of the 'reader' object
                    for row in reader:
                        # add the contents of 'Units sold' column to the list
                        units_sold_values.append(row[3])
                    # Print the values in the Units sold column (index 3)
                    print("\nStored data:", units_sold_values)
                    # check if 'price_values' list is NOT empty
                    if units_sold_values:
                        # Iterate over the 'price_values' list starting from the second element/index/string
                        for value in units_sold_values:
                            # check if the 'value' in the for loop does not equal an empty space (' ')
                            if value != empty_space:
                                try:
                                    # convert each value to Type 'int'
                                    value = int(value)
                                    # increment 'price_sum' for later average calculation...
                                    units_sold_sum += value
                                    # increment 'price_count' for later average calculation...
                                    units_sold_count += 1
                                # if there's a non-numeric value in the column selected, a warning message appears
                                except ValueError:
                                    print("Warning: Non-numeric value found in 'Price' column.")
                    
                    # Calculate average of 'Units sold' column (the use of '//' is because of the Type) | '//' ---> int & '/' ---> float
                    units_sold_average = units_sold_sum // units_sold_count if units_sold_count != 0 else 0
                    # print the calculated average
                    print("\nCalculated Average:", units_sold_average)
                    # Iterate over the length of the 'price_values' list
                    for i in range(len(units_sold_values)):
                        # if the index of the list during iteration is an empty space and the amount of cells is less than or equal to 7...
                        if units_sold_values[i] == empty_space and replacement_count <= 7:
                            # replace/overwrite that empty space with the 'str' version of the calculated average
                            units_sold_values[i] = str(units_sold_average)
                            # increment the count by 1 for each iteration of the list
                            replacement_count += 1
                    # print the replaced data onto the screen
                    print("\nReplaced data:", units_sold_values)

                    """
file.seek(0) is used to move the file cursor (the position from where the next read or write operation will occur) to the beginning of the file before iterating over the file contents again.

Without file.seek(0), if you try to read the file again without closing and reopening it, you'll be at the end of the file.

So, basically it resets the cursor to the beginning of the file before re-reading it.
                    """

                    file.seek(0)
                    # assign the 'str' Type of the 'units_sold_average' variable to 'replacement_value_units_sold'
                    replacement_value_units_sold = str(units_sold_average)
                    # initialize 'updated_units_sold' list
                    updated_units_sold = []
                    # Iterate over the rows of the file
                    for row in reader:
                        # assign the stripped (removed whitespaces) version of row[3] (index 3 [Units sold column]) to 'units_sold_cell'
                        units_sold_cell = row[3].strip()
                        # check if 'units_sold_cell' is an empty string and row[2] is an empty string
                        '''
                        this ensures that both conditions (empty strings and ONLY strings) are True instead of causing SemanticError
                        '''
                        if units_sold_cell == '' and row[3].strip() == '':
                            # replace the empty string in row[3] to the value defined above (replacement_value_units_sold) 
                            row[3] = replacement_value_units_sold
                        # 'extend' option is used to discard the square brackets of the file
                        '''
                        if 'append' is used, then the output will be a list of lists (SemanticError)
                        '''
                        updated_units_sold.extend(row)
                    
                    # print a new-line onto the screen
                    print()
                    # 'chunks' is assigned to a list comprehension to organize the contents/data back to previous form (form: same as the file appreanace)
                    '''
                    Create 4-field row sublists:

                    arranging 'updated_price' list into chunks consisting of 4-field row sublists (just like the file) for 'writing' purposes
                    'writing' ---> writer.writerow(VARIABLE), for updating the file
                    '''
                    updated_units_sold_chunks = [updated_units_sold[i:i+4] for i in range(0, len(updated_units_sold), 4)]
                    # Iterate over the length of 'chunks' and assign the index to a list comprehension that prints the rows horizontally
                    for i in range(len(updated_units_sold_chunks)):
                        updated_units_sold_chunks[i] = [field.strip() for field in updated_units_sold_chunks[i]]

            # open the csv file in write mode and use the argument ('') with the built-in parameter 'newline='
            '''
The newline='' parameter prevents Python from automatically appending newline characters (\n) to each line in the file.
This helps to avoid the addition of extra blank lines between rows in the output CSV file.
            '''
            with open(csv_file, 'w', newline='') as file:
                # Create writer object to write to file for the purpose of updating the data
                writer = csv.writer(file)
                # because 'average' function acts as a supplementary function. it's preferred to refer to the same constant of the outer function
                if COLUMN_NAME == "Price":
                    # Iterate over the newly replaced list
                    for row in updated_price_chunks:
                        # write (update) the new data to the file for later printing
                        writer.writerow(row)
                # else if the other column name...
                elif COLUMN_NAME == "Units sold":
                    # Iterate over the newly replaced list
                    for row in updated_units_sold_chunks:
                        # write (update) the new data to the file for later printing
                        writer.writerow(row)

        # Print updated table with replaced values
        print("Updated table with replaced values:\n")
        with open(csv_file) as file:
            reader = csv.reader(file)
            for line in reader:
                print(line)
        # '''

    # Print available columns
    print("Choose a column to clear and prepare data:\n")
    columns = ['Branch', 'Product', 'Price', 'Units sold']
    for col in columns:
        print(col)

    # Validate user input for column selection (User input validation)
    while True:
        # column_name = input("\nPlease enter the selected column: ").strip()
        COLUMN_NAME = input("\nPlease select a column name: ").strip()
        if COLUMN_NAME.capitalize() not in columns:
            print(f"\nColumn '{COLUMN_NAME}' not found. Please select from the available columns.")
        elif COLUMN_NAME.capitalize() == "Branch":
            print("\nSelected column 'Branch' does not contain numerical values\n")
            print("Please select another column name...")
        elif COLUMN_NAME.capitalize() == "Product":
            print("\nSelected column 'Product' does not contain numerical values\n")
            print("Please select another column name...")
        else:
            break

    # Validate column input for numerical columns
    if COLUMN_NAME.casefold() in ['Price'.casefold(), 'Units sold'.casefold()]:
        if COLUMN_NAME == 'Price':
            PROCESSED_COLUM.append('Price')
            print("\nYou selected column: 'Price'")
            # print(PROCESSED_COLUM)
        elif COLUMN_NAME == 'Units sold':
            PROCESSED_COLUM.append('Units sold')
            print("\nYou selected column: 'Units sold'")
            # print(PROCESSED_COLUM)
        submenu = ['minimum', 'maximum', 'average']
        print("\nChoose an operation to replace empty values (minimum, maximum, or average):\n")
        for op in submenu:
            print(op)

        # Validate user input for operation selection
        while True:
            selected_operation = input("\nEnter your choice: ").strip().casefold()
            if selected_operation not in submenu:
                print("\nInvalid choice. Please select a valid operation.")
            else:
                break

        # Execute the selected operation
        if selected_operation == 'minimum':
            minimum(csv_file=csv_file)
        elif selected_operation == 'maximum':
            maximum(csv_file=csv_file)
        elif selected_operation == 'average':
            average(csv_file=csv_file)
        print("\nEmpty values in the column have been successfully replaced!")

def analyze_data(csv_file):
    '''
At the inception, it decides whether the chosen column is 'Price' or 'Units sold'. Next, column is sorted according to the selected operation happens...
based on the column selection by user such as 'Price' or 'Units sold', the function processes and sorts data chips from the CSV file.

the function then asks the user to enter the preferred opration:-

- Ascending order (operation)
- Descending order (operation)

In the sorting process, it uses the insertion sort algorithm to organize it either in ascending or descending order, depending on the preferences.
The function takes user's input for sorting the order, and then it sorts data as per their input.

When sorting process finishes, the function replaces values in CSV file with the sorted entries...
It swaps the content of the original column with the sorted values of the file...
After sorting the selected column in the CSV file, the function prints the sorted values with updated table by printing to the console.

During its run time, the analyze_data function repeatedly utilizes regular file handling approaches to deal with the CSV file and meet user criteria...
where appropriate item classification takes place.
    '''
    # Define the insertion sort function
    def insertion_sort(column_data):
        '''
The insertion_sort function allows for the insertion sort algorithm to sort data within a CSV file in either the ascending or the descending sequence as requested by the user.
Primarily, it checks if the option column is just either 'Price' or 'Units sold'. Next it will contrive the structure by just selecting the column which will support the data ordering.

In the sorting process, it takes a form of insertion sort to look at every element and put them in the proper order (selected by user) through comparison...
The sorting function of the program supports the sorting operations that are done in both ascending and descending order which depends on the preference of the user...
lastly it will print the updated table, displaying the sorted values to the console.

Upon execution of the function, file handling methods are used that reads and writes data to CSV files, resulting in the implementation of sorting columns of the CSV file according to the user's selection.
        '''
        # Check the sorting order
        if ORDER_CHOICE == '1' or ORDER_CHOICE == 'ascending':
            # Sort in ascending order
            for index in range(1, len(column_data)):
                current_value = column_data[index]
                while index > 0 and column_data[index - 1] == '' or int(column_data[index - 1]) > int(current_value):
                    column_data[index] = column_data[index - 1]
                    index -= 1
                column_data[index] = current_value
        elif ORDER_CHOICE == '2' or ORDER_CHOICE == 'descending':
            # Sort in descending order
            for index in range(1, len(column_data)):
                current_value = column_data[index]
                while index > 0 and column_data[index - 1] == '' or int(column_data[index - 1]) < int(current_value):
                    column_data[index] = column_data[index - 1]
                    index -= 1
                column_data[index] = current_value

    # Check if 'Price' or 'Units sold' has been previously selected
    if 'Price' in PROCESSED_COLUM:
        print("Previously selected column: 'Price'\n")
        print("Please proceed for further processing")
    elif 'Units sold' in PROCESSED_COLUM:
        print("Previously selected column: 'Units sold'\n")
        print("Please proceed for further processing")

    # Define valid sorting orders
    valid_sorting_orders = ['1', '2', 'ascending', 'descending']
    while True:
        # Check if 'Price' column has been selected
        if 'Price' in PROCESSED_COLUM:
            print("\nHow do you want to sort the 'Price' column?\n")
            orders = ['1. Ascending order', '2. Descending order']
            for order in orders:
                print(order)
            
            while True:
                ORDER_CHOICE = input("\nEnter your choice (1/2): ").strip().casefold()
                if ORDER_CHOICE in valid_sorting_orders:
                    updated_price = []
                    column_data = []

                    with open(csv_file, 'r') as file:
                        reader = csv.reader(file)
                        next(reader)
                        for row in reader:
                            column_data.append(row[2])
                        print()
                        print("Unsorted column:", column_data)
                        insertion_sort(column_data=column_data)

                        # for value in column_data:
                        print("\nSorting column...\n")
                        #     print(value)

                        print("Sorted column:", column_data)
                        print("\nValues in the 'Price' column have been sorted!\n")

                        file.seek(0)
                        for row in reader:
                            if row[2] != 'Price' and column_data:
                                row[2] = column_data.pop(0)
                            updated_price.extend(row)
                        # print()
                        # print(updated_price)
                    
                        print()
                        updated_price_chunks = [updated_price[i:i+4] for i in range(0, len(updated_price), 4)]
                        for i in range(len(updated_price_chunks)):
                            updated_price_chunks[i] = [field for field in updated_price_chunks[i]]

                    # Write the updated data back to the CSV file
                    with open(csv_file, 'w', newline='') as file:
                        writer = csv.writer(file)
                        for row in updated_price_chunks:
                            writer.writerow(row)
                
                     # Print the updated table
                    with open(csv_file, 'r') as file:
                        reader = csv.reader(file)
                        print("\nUpdated table with sorted values:\n")
                        for row in reader:
                            print(row)
                    break
                elif ORDER_CHOICE not in valid_sorting_orders:
                    print("Invalid choice! Please try again.")
                    continue
            break

        # Check if 'Units sold' column has been selected
        elif 'Units sold' in PROCESSED_COLUM:
            print("\nHow do you want to sort the 'Units sold' column?\n")
            orders = ['1. Ascending order', '2. Descending order']
            for order in orders:
                print(order)
            
            while True:
                ORDER_CHOICE = input("\nEnter your choice (1/2): ").strip().casefold() # 👀
                if ORDER_CHOICE in valid_sorting_orders:
                    updated_units_sold = []
                    column_data = []
                    with open(csv_file, 'r') as file:
                        reader = csv.reader(file)
                        # Skip the header row
                        next(reader)
                        for row in reader:
                            column_data.append(row[3])
                        print()
                        print("Unsorted column:", column_data)
                        insertion_sort(column_data=column_data)

                        # for value in column_data:
                        print("\nSorting column...\n")
                        #     print(value)

                        print("Sorted column:", column_data)
                        print("\nValues in the 'Units sold' column have been sorted!\n")

                        file.seek(0)
                        for row in reader:
                            if row[3] != 'Units sold' and column_data:
                                row[3] = column_data.pop(0)
                            updated_units_sold.extend(row)
                        # print()
                        # print(updated_units_sold)

                        print()
                        updated_units_sold_chunks = [updated_units_sold[i:i+4] for i in range(0, len(updated_units_sold), 4)]
                        for i in range(len(updated_units_sold_chunks)):
                            updated_units_sold_chunks[i] = [field for field in updated_units_sold_chunks[i]]

                     # Write the updated data back to the CSV file
                    with open(csv_file, 'w', newline='') as file:
                        writer = csv.writer(file)
                        for row in updated_units_sold_chunks:
                            writer.writerow(row)

                    # Print the updated table
                    with open(csv_file, 'r') as file:
                        reader = csv.reader(file)
                        print("\nUpdated table with sorted values:\n")
                        for row in reader:
                            print(row)
                    break
                elif ORDER_CHOICE not in valid_sorting_orders:
                    print("Invalid choice! Please try again.")
                    continue
            break
        else:
            print("\nInvalid choice! Please try again...\n")
            # continue

def visualize_data(csv_file):
    '''
The function 'visualize_data' would help the user visualize data stored in a CSV file whether the previous selection is either 'Price' column or 'Units Sold' column.

First, the algorithm checks if the last-selected column is either 'Price' or 'Units sold' and develops an algorithm that visualizes the nuerical values in the selected column...
after identification the selected column, the function executes the visualization of the data from the previously selected column.

The visualization process is completed by iterating through the CSV file repeatedly...
and if the column 'Price' is previously selected, then it projects/prints the data as a visual e.g. the asterisk (*) character...
after that, the function prints a goodbye message.

Execution of the function is practical in non-numeric cases too, letting the user know those values which were skipped...
After the completion, it exhibits the specified data in the form of visualized charts to the user for analysis and review.

Upon the operation of the 'visualize_data' function, it uses proper technique to process and read details from the CSV file...
ensuring correct comprehension of the contents through visualization.
    '''
    # Check which column was previously processed
    if 'Price' in PROCESSED_COLUM:
        print("Previously selected column: 'Price'\n")
        print("Please proceed for further processing")
    elif 'Units sold' in PROCESSED_COLUM:
        print("Previously selected column: 'Units sold'\n")
        print("Please proceed for further processing")

    # Open the CSV file for reading
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader)

        # Process the data based on the previously selected column
        if 'Price' in PROCESSED_COLUM:
            # Iterate over rows in the CSV file
            for row in reader:
                try:
                    # Extract the value from the 'Price' column
                    value = int(row[2])
                    if value >= 100:
                        # Assigning maximum stars for large values
                        num_stars = 20
                    else:
                        # Calculate the number of stars based on the value
                        num_stars = value // 5
                    print(f"Price: {value}: {'*' * num_stars}")
                except ValueError:
                    # Handle non-numeric values
                    print("Non-numeric value found in the 'Price' column.")
        elif 'Units sold' in PROCESSED_COLUM:
            # Iterate over rows in the CSV file
            for row in reader:
                try:
                    # Extract the value from the 'Units sold' column
                    value = int(row[3])
                    if value >= 100:
                        # Assigning maximum stars for large values
                        num_stars = 20
                    else:
                        # Calculate the number of stars based on the value
                        num_stars = value // 5
                    # Print visual representation of the value
                    print(f"Units sold: {value}: {'*' * num_stars}")
                except ValueError:
                    # Handle non-numeric values
                    print("Non-numeric value found in the 'Units sold' column.")

def main():
    '''
this function prints out a main menu for the user to interact with, within the main function there are 4 while true loops within an outer while true loop.
The outer while true loop creates a domain where it gives the user 4 options to chose from...
each one of the inner four while true loops consists of 1 user option with input validation.

There is a sequence that each inner while True loops follows, and that sequence is:-
- cehck if correct input is entered 
- if correct input is entered, then call the function and the loop breaks 

after that it prints the remaining options for the user to proceed with the program
    '''
    # Main Menu
    print()
    print('-' * 50)
    print("Welcome to Data Analysis CLI")
    print('-' * 50)
    program_stages = ["1. Load Data", "2. Clean and prepare data", "3. Analyze Data", "4. Visualize Data\n"]
    for stage in program_stages:
        print(stage)

    # Loop to handle user input and navigate through program stages
    while True:  
        option = input("Please select stage: ")

        # Stage 1: Load Data
        if option == "1" or option.casefold() == "Load Data".casefold():
            if option == "1":
                print(f"\nYou selected the 1st stage...")
            elif option.casefold() == "Load Data".casefold():
                print(f"\nYou selected stage: {option}...")

            # Handling file path input
            while True:
                file_path = input("\nPlease enter path to the CSV file (absolute or relative path): ")
                try:
                    if "sales.csv" in file_path:
                        print("\nChecking if file exists...\n")
                        load_data(csvfile=file_path)
                        break
                    else:
                        print(f"\n{file_path}: Wrong input, please try again...")
                        continue
                except FileNotFoundError:
                    print("ERROR: File not found...")
                    continue
            
            # Displaying remaining options after Stage 1
            print("\nRemaining options:\n")
            for i in range(1, len(program_stages)):
                print(f"{program_stages[i]}")
            valid_options = ["2", "Clean and prepare data", "3", "Analyze Data", "4", "Visualize Data"]
            
            # Loop to handle user selection of the remaining stages
            while True:
                remaining_options = input("Please select stage: ")
                if remaining_options not in valid_options:
                    print("\nWrong input, please reselect stage...\n")
                    continue
                else:
                    if remaining_options == "2" or remaining_options.casefold() == "Clean and prepare data".casefold():
                        print(f"\nYou selected stage: {remaining_options}\n")
                        clean_and_prepare_data(csv_file=file_path)
                        break
            
            # Displaying remaining options after Stage 2
            print("\nRemaining options:\n")
            for i in range(2, len(program_stages)):
                print(f"{program_stages[i]}")
            remaining_valid_options = ["3", "Analyze Data", "4", "Visualize Data"]

            # Loop to handle user selection of the remaining stages
            while True:
                remaining_options = input("Please select stage: ") 
                if remaining_options not in remaining_valid_options:
                    print("\nWrong input, please reselect stage...\n")
                    continue 
                else:
                    if remaining_options == "3" or remaining_options.casefold() == "Analyze Data".casefold():
                        print(f"\nYou selected stage: {remaining_options}\n")
                        analyze_data(csv_file=file_path)
                        break 
            
            # Displaying remaining option after Stage 3
            print("\nRemaining option:\n")
            print("4. Visualize Data")
            final_valid_option = ["4", "Visualize Data"]

            # Loop to handle user selection of the remaining stage
            while True:
                remaining_options = input("Please select stage: ") 
                if remaining_options not in final_valid_option:
                    print("\nWrong input, please reselect stage...\n")
                    continue 
                else:
                    if remaining_options == "4" or remaining_options.casefold() == "Visualize Data".casefold():
                        print(f"\nYou selected stage: {remaining_options}\n")
                        visualize_data(csv_file=file_path)
                        break
            
            # Salute (final message)
            print("\nVisualisation completed!")
            print("\nThank you and good bye!\n")
            break

        else:
            print("\nPlease select stage 1 (Load Data) first before proceeding\n")

if __name__ == "__main__":
    main()
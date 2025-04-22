import pandas as pd
import math
import os
import csv
import sys


sys.path.append("../Sorting_Algorithms")
from sorting_algos import merge_sort, merge


col_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']

####################################################################################
# Donot Modify this Code
####################################################################################
class FixedSizeList(list):
    def __init__(self, size):
        self.max_size = size

    def append(self, item):
        if len(self) >= self.max_size:
            raise Exception("Cannot add item. List is full.")
        else:
            super().append(item)

####################################################################################
# Mystery_Function
####################################################################################
def Mystery_Function(file_path, memory_limitation, columns):
#     """
#     # file_path :  file_path for Individual Folder (datatype : String)
#     # memory_limitation : At each time how many records from the dataframe can be loaded (datatype : integer : 2000)
#     # columns : the columns on which dataset needs to be sorted (datatype : list of strings)
#     # Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
#     # **NOTE : In this Mystery_Function records are accessed from only the folder Individual.

#     #Store all the output files in Folder named "Final".
#     #The below Syntax will help you to store the sorted files :
#                 # name_of_csv = "Final/Sorted_" + str(i + 1)
#                 # sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)
#     #Output csv files must be named in the format Sorted_1, Sorted_2,...., Sorted_93
#     # ***NOTE : Every output csv file must have 2000 sorted records except for the last ouput csv file which might have less
#                 #than 2000 records.
#     """

#     #Need to Code
#     #Helps to Sort all the 1,84,265 rows with limitation.

#     #Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
    chuncks_2000=FixedSizeList(2000)
    
    # Define the output directory for the sorted files
    output_dir = "Final"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)    

    # Determine the number of rows in the CSV file
    
    df = pd.read_csv("imdb_dataset.csv", header=None)
    df = df.values.tolist()
    columns = ['tconst'] + columns
    column_vals = [col_names.index(column) for column in columns]
    df = merge_sort(df, column_vals)
    output_file = os.path.join(file_path, "test.csv")
    df = pd.DataFrame(df, columns=col_names)
    df.to_csv(output_file, index=False)
    
    total_rows = sum(1 for line in open(file_path+"/test.csv", encoding='utf-8'))
    # Iterate over chunks of data with size memory_limitation
    for i in range(0, total_rows, memory_limitation):
        # Read the next chunk of data
        chuncks_2000 = pd.read_csv(file_path+"/test.csv", skiprows=i, nrows=memory_limitation, header=None)
        data = chuncks_2000.values.tolist()


        # print(column_vals)  
        # Sort the chunk by the specified columns using merge sort
        
        sorted_chunk = merge_sort(data, column_vals)
        sorted_df = pd.DataFrame(sorted_chunk, columns=None)
        # Save the sorted chunk to a CSV file in the output directory
        output_file = os.path.join(output_dir, "Sorted_" + str(i // memory_limitation + 1)+ ".csv")
        sorted_df.to_csv(output_file, index=False)
        
    temp = os.path.join(file_path, "test.csv")  
    os.remove(temp)
    

    # data =[]  
    # # Iterate over chunks of data with size memory_limitation
    # for i in range(0, 93):
    #     # Read the next chunk of data
    #     chuncks_2000 = pd.read_csv(file_path+"/Sorted_"+str(i + 1)+".csv", nrows=memory_limitation, header=None)
    #     data = chuncks_2000.values.tolist()
    #     sorted_df = pd.DataFrame(data)
    #     # Save the sorted chunk to a CSV file in the output directory
    #     output_file = os.path.join(output_dir, "Sorted_" + str(i + 1)+ ".csv")
    #     sorted_df.to_csv(output_file, index=False)
            
    # print(data)
    
    
        

    
    


####################################################################################
# Data Chuncks
####################################################################################
# def data_chuncks(file_path, columns, memory_limitation):


def data_chuncks(file_path, columns, memory_limitation):
    """
    Reads a CSV file, separates the data into chunks of data defined by the memory_limitation parameter,
    sorts each chunk of data by the specified columns using the merge_sort algorithm, and saves each sorted chunk
    as a separate CSV file. The chunk sets are determined by the number of rows in the file divided by the
    memory_limitation. The names of the sorted files are stored as "Individual/Sorted_" followed by a number
    starting from 1.
    """
    #Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
    chuncks_2000=FixedSizeList(2000)

    # Define the output directory for the sorted files
    output_dir = "Individual"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Determine the number of rows in the CSV file
    total_rows = sum(1 for line in open(file_path, encoding='utf-8'))
        
    # Iterate over chunks of data with size memory_limitation
    columns = ['tconst'] + columns
    column_vals = [col_names.index(column) for column in columns]
    for i in range(0, total_rows, memory_limitation):
        # Read the next chunk of data
        chuncks_2000 = pd.read_csv(file_path, skiprows=i, nrows=memory_limitation, header=None)
        data = chuncks_2000.values.tolist()
        # print(column_vals)  
        # Sort the chunk by the specified columns using merge sort
        
        sorted_chunk = merge_sort(data, column_vals)
        sorted_df = pd.DataFrame(sorted_chunk, columns=col_names)
        # Save the sorted chunk to a CSV file in the output directory
        output_file = os.path.join(output_dir, "Sorted_" + str(i // memory_limitation + 1)+ ".csv")
        sorted_df.to_csv(output_file, index=False)

        """
        # file_path : dataset file_path for imdb_dataset.csv (datatype : String)
        # columns : the columns on which dataset needs to be sorted (datatype : list of strings)
        # memory_limitation : At each time how many records from the dataframe can be loaded (datatype : integer)
        # Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
        # NOTE : This data_chuncks function uses the records from imdb_dataset. Only 2000 records needs to be loaded at a
                # Time in order to process for sorting using merge sort algorithm. After sorting 2000 records immediately
                # Store those 2000 sorted records into Floder named Individual by following Naming pattern given below.
        #Store all the output files in Folder named "Individual".
        #Output csv files must be named in the format Sorted_1, Sorted_2,...., Sorted_93
        #The below Syntax will help you to store the sorted files :
                    # name_of_csv = "Individual/Sorted_" + str(i + 1)
                    # sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)

        # ***NOTE : Every output csv file must have 2000 sorted records except for the last ouput csv file which
                    might have less than 2000 records.

        Description:
        This code reads a CSV file, separates the data into chunks of data defined by the memory_limitation parameter,
        sorts each chunk of data by the specified columns using the merge_sort algorithm, and saves each sorted chunk
        as a separate CSV file. The chunk sets are determined by the number of rows in the file divided by the
        memory_limitation. The names of the sorted files are stored as "Individual/Sorted_" followed by a number
        starting from 1.
        """

        #Write code for Extracting only 2000 records at a time from imdb_dataset.csv

        #Passing the 2000 Extracted Records and Columns indices for sorting the data
        #column_indxes are Extracted from the imdb_dataset indices by mapping the columns need to sort on which are
        #passed from the testcases.
        # arr=merge_sort(arr,column_indxes)


#Enable only one Function each from data_chuncks and Mystery_Function at a time

#Test Case 13
data_chuncks('imdb_dataset.csv', ['startYear'], 2000)

#Test Case 14
#data_chuncks('imdb_dataset.csv', ['primaryTitle'], 2000)

#Test Case 15
#data_chuncks('imdb_dataset.csv', ['startYear','runtimeMinutes' ,'primaryTitle'], 2000)


#Test Case 13
Mystery_Function("./Individual", 2000, ['startYear'])

#Test Case 14
#Mystery_Function("Individual", 2000, ['primaryTitle'])

#Test Case 15
#Mystery_Function("Individual", 2000, ['startYear','runtimeMinutes' ,'primaryTitle'])

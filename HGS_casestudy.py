#Importing Pandas library for creating dataframe and saving the extracted data 
import pandas as pd

#creating variable with path and name of the file to access the files through looping
file_loc = '/home/sariq16/HGS_casestudy/Assignment-files/Plain output/'
file_name = ['Contoso 1.txt', 'Contoso 2.txt', 'Contoso 3.txt']

#creating dataframe and adding columns for the required data of concerns
extractedDF = pd.DataFrame(columns = ['FileName', 'Date', 'Due Date', 'Balance Due'])

#creating a variable i for indexing the df 
i = 0

for file in file_name: #accessing all the files through loop
    row = [file[:9]] #slicing the file name in the sample format to store it to the df
    
    with open (f'{file_loc}{file}', 'r') as file_object: #open each text files in read mode
        file_contents = file_object.readlines() #reading each line of text file and storing it in the variable as list
        
        extract_values = file_contents[4:9:2] #slicing the lines at index 4,6,8 and storing it in another variable as list
        for value in extract_values: #accessing each stored line through loop
            row.append(value[:-1].split(': ')[1]) #performing slicing, splitting & indexing operation and appending the data to variable row
                                
        
    extractedDF.loc[i] = row #appending the row the final df
    i+=1 #incresing the index value to access the row
    print(f'Data from {file[:9]} Extracted') #indicate that operation is completed for each file
    
extractedDF.to_excel('Output.xlsx', index = False) #saving the df to the required excel format

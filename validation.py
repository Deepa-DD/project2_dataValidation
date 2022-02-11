import pandas as pd
import os
main=["/home/admin123/project2_dataValidation/28_Trial_of_violent_crimes_by_courts.csv","/home/admin123/project2_dataValidation/29_Period_of_trials_by_courts.csv","/home/admin123/project2_dataValidation/30_Auto_theft.csv","/home/admin123/project2_dataValidation/31_Serious_fraud.csv"]
for i in main:  # loop for eccessing all file fath from dictionary
    path1=i
    # print(path1)
    df=pd.read_csv(path1)    # reading file one by one 


    df.dropna(axis=0,inplace = True)   # For drop NA or Null
    # df.to_csv(path)     

    df.drop_duplicates(inplace = True) # For delete Duplicate rows
    df.to_csv(path1)
   
    if os.path.getsize(path1)>0:  # For getting size of file
        pass
    
    else :
        os.remove(path1)
    
    extension=path1[-4:] # for check that file is in CSV format or not 
    if extension==".csv":  # this condithion will check that at the end of the path there is .csv or not if yes then it will pass
        pass
    else:
        os.remove(path1)   # else it will delete the file



# dic1={"/home/admin123/project2_dataValidation/28_Trial_of_violent_crimes_by_courts.csv":{"Area_Name":str,"Year":int,"Group_Name":str,"Sub_Group_Name":int,"PT_1_3_Years":int,"PT_3_5_Years":int,"PT_5_10_Years":int,"PT_6_12_Months":int,"PT_Less_than_6_Months":int,"PT_Over_10_Years":int,"PT_Total":int}}   # dictionary for check data type in column, this code only check str type columns like Area Name / Group name.  
# num="1234567890"        
# df=pd.read_csv("/home/admin123/project2_dataValidation/28_Trial_of_violent_crimes_by_courts.csv")  # Reading CSV file
# for i in dic1:        # I will take path from dict
#     main_path=i       # Save path in a variable
#     for j in dic1[i]:  # It will take values of dict wich will be same as file Header
#         if j in df:     # checking that the value is in file or not 
#             data_type=dic1[i][j]  # storing data type in one variable 
#             if data_type==str:     # condition if data type eill be string then only it will go inside the if body because the code is for str
#                 inn=0               # takeing variable it will increase when anyu row will delete because if any row will drop then every indexing will change then by using this we can find new indexing
#                 c=0                 # it will work as indexing 
#                 for element in df[j]:   # this element will access all alement of column
#                     element_alphabet=0  # it will itrate in the element
#                     count=0             # this variable will count if any number is there in element or not 
#                     while element_alphabet <len(element):   # variable will run till legnth of element
#                         if element[element_alphabet] in num:      
#                             count+=1    # count will increase when there is any number in element
#                         else:
#                             pass
#                         element_alphabet+=1
#                     if count>0:   # if count will be more then 0 then it will go ahead
#                         df.drop(df.index[c-inn],inplace=True) # this will drop row 
#                         df.to_csv(main_path,index=False)
#                         inn+=1   
#                     c+=1    

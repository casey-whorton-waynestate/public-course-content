#!/usr/bin/env python
# coding: utf-8

# In[3]:


#%% 

# Personal Introduction

# TO DO:
# 0.) Run the code below without any changes and view the output
# 1.) Update the first_name variable with your first name
# 2.) Update the github_id variable with your github id
# 3.) Create a variable for your last name
# 4.) Add text to the first print statement to print both your first and last name
# 5.) Add a print statement to print "Github ID: <your github id>"

first_name = 'my first name'
github_id = 'github_id'

print('Hi, my name is ' + first_name)


# Dictionaries and dictionary references
intro_dict = {'First Name':first_name,
              'Last Name':'my last name',
              'Github ID':github_id}

print('\nHere is your introduction dictionary:')
print(intro_dict)
print('\nHere are the Keys of the dictionary:')
print(intro_dict.keys())
print('\nHere are the Values of the dictionary:')
print(intro_dict.values())
print('\nNotice that each value corresponds with a key.\nThe next line will display the value associated with the key for First Name')

print(intro_dict['First Name'])

# TO DO:
# 6.) Add a print statement that prints the value associated with the Last Name key

print('\nNow, lets write a for loop that prints the key-value pairs in a sentence:\n')

for key,value in intro_dict.items():
    print(key +': ' + value)

#TO DO:
# 7.) Add a key-value pair to the introduction dictionary for your email address
# Note: use the update method to do this, refer to this: 
# https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
# 8.) Add a for loop that prints the updated dictionary
# Add the statements below
print('\n\nNew Introduction Dictionary:\n\n')

# TO DO:
# 9.) Commit changes to a new branch in the private repository you are a collaborator on with your instructor
# 10.) Add a review request to the pull request with your instructor as the person you want to review your pull request
# 11.) Allow time for the instructor to review the code and they will commit your changes to the branch or leave comments on how to improve


# In[ ]:





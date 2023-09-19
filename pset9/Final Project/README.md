######################### STUDENT ADMISSION MANAGEMENT ############################

######## Video Demo:https://youtu.be/Ew6o6yz7Cwk

######## Description:

Hello Everyone, Welcome To My Final Project For The Programme CS50P.
So, For My Final Project, I Have Created A Simple Program In Python That Deals With CSV Files, For Which I Have Used The sys,csv,random and datetime libraries.
This Python File Takes 2 Command-Line Inputs, The Input CSV File And The Name Of The Output CSV File....

Format: python "input_file" "output_file"

This Program Takes In A CSV File As Input Which Contains 3 Fields : Name,Birthyear And Programme Respectively And Output Another CSV File After Performing Various Functions.

First Of All, We Perform Basic Error Handling And Input Verification For Our CSV Files Using Try And Except.
Secondly, The Age Of The Student Is Derived Using Their Birthyear And DateTime Library, So The Age Is Always Accurate No Matter When In Time We Run The Program.
Lastly, We Have A Class Hat Which Contains A Function sort, Which Helps Us Sort The New Students Into The 4 Houses In An Unbiased Way.

For Our Test File We Have test_project.py, in which the functions validate_input,assign_house,calculate_age are put through pytest...

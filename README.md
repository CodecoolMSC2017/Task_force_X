# Task_force_X
Pa practice

This repository is open for anyone who want to prepare for the PA held in januray or just to practice in general.

Task details should be added in this file if you modify pls stick to this rule so we can keep it organized,
and please dont upload solutions just yet.

Task1


-sum_of_nums    
write a function that sums elements of the given list.

-sum_of_many_nums 
write a function that sums the elements of two lists, the function should return one 
list with two elements each element representing the sum of the original lists.

-find_all_uppers
your given a list that contains strings and integers alike, your function should return a string that contains how many uppercase letters are in your original list
should look like this : [1,"Fasz",3,"DakonVago"] --»"3"

-find_all_none_primes
write a function that retuns all non prime numbers from zero to n.

-find_the_odd_one_out
your given a list that contains strings and integers alike, write a function that returns a nested list 
with the strings and integers separted and ordered, if there are more integers then strings in the list
the integer list should be the first element in your nested list else the string list should come first.


-many_whelps_handle_it
you are in a bad situation your getting overrun by whelps(little dragons)incase you pondering
write a function that creates a list with 10 elements randomized the options are whelp or raidmember
after the list is created your function should decide if there are more raidmembers then whelps in your list
if there are more raidmembers return 'hit it like you mean it' if there are more whelps it should return 'LEEEEEEROY JENNNKINS'


Task2

-find_every_other
your given a string and your task is to find every other character and decide if its a number or not
if its a number convert it to int or float and return the sum of them, after you done with this insterting at the end of the string


-swithceroo
your given a string and your task is to switch all uppercase and lowercase letters and numbers and all special characters.
special characters should be switched to numbers like this ,."+!%/--»'1234567'.
numbers should be just reversed in order.

-find_chars_between
your given a string that containing a sentence with special characters inside it your goal is to return the characters found between the special characters.

-find_the_truth
your given a string that filled with lies your task is to filter out the truth and return only the truth
your string looks like this="lie lie truth lie truth lie truth lie lie truth"
return value should be a string separeted with words separetad with whitespace

-not_your_usual_string
your goal in this task is to write a function takes two strings as an arguments and prints out 'my birthday is on <insert your birthday here> !' using any number is forbidden in this function.

-tell_your_name
in this exercises you are given a list that contains all letters from the english abc your goal is to return a list of numbers that contains the position of your names characters in the abc

Task3

-give_me_one_list
in this exercises your function takes two arguments both are list your goal is to return one list with all values sorted in it 

-give_me_some_lits
your function takes two arguments a list and an integer your goal is to split your list into n sized lists.

-matrix_time
you have a 3x2 matrix that looks like this my_mat=[[1234,'d'],
                                                   [21562,'d'],
                                                   [12,'y']]
as you your probably guessed by now the letters stand for days and years, your function should return a list containing two elements one of them is the total days and the other is 'd' or the total number of years and 'y' according whats the given argument of the function

-matrix_diagonal
in this task your required to write a function that returns both diagonals of a nxn matrix


-sums_easy
your function takes a matrix as an argument your goal is to sum the values of every row in a the matrix
and then return the matrix with the correct answer added as the last element of the row, 
like this [[1,2,3],  [[1,2,3,6],
           [4,5,6],   [4,5,6,15],  
           [7,8,9]]    [7,8,9,24]]

-sums_hard
you have a matrix your goal is to sum for every element horiztontally and vertically
[[1,2,3], 
 [4,5,6],
 [7,8,9]]

Task4

-add_to_my
your goal is to write a function that takes a list as an argument that containts strings and numbers one after each other and converts it to a dictionary with the numbers being the keys in the dictionary.

-switch_my
your goal in this exercises is to switch the keys and the values of the dictionary created in the previous function if the key was an odd number switch the string to uppercase if its even switch it to lowercase.


-key_change
you have a dictionary and a string that contains a sentence if the dictionary keys contain any of the wodrs from the string change the word in the string to the value of the given key.

-convert
your function takes a string as an argument and your goal is to make a dictionary out of it , in your string every word is separated with whitespace and every word contains an uppercase letter these will be the keys the rest of the letters of the given word will be the value of your dictionary.

-read_my_dict
    your functions arguement is a nested dictionary and it should return a string of the representing the content of the dictionary
    like this:
    {'fej': {'fog': 1, 'kar': 2}, 'torzs': {'kez': 2, 'lab': 2}} should look like this---> fej fog 1 kar 2
                                                                                           torzs kez 2 lab 2
#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'

# 'o'

# 'djan'

# 'jan'

# 'go'

print("Problem 1---------------------")
print("d :"+s[0])
print(" o:"+s[-1])
print("djan :"+s[:4])
print("jan :"+s[1:4])
print("go:"+s[4:])


# Bonus: Use indexing to reverse the string


###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"

print("problem two")
print("Before ",l)
l[2][2]="goodbye"
print("After Reaasign Hello To goodbye:",l)


###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print("Problem 4")
print("q1",d1["simple_key"])
print("q2",d2["k1"]["k2"])
print("q3",d3["k1"][0]["nest_key"][1][0])


###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

print("set  problem")
print(set(mylist))


###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
a="Hello my dog's name is Sammy and he is 4 years old"
print("problem 5")
print("Hello my dog's name is {} and he is {} years old".format(name,age))

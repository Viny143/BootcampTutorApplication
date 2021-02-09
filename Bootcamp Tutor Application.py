"""
Programming Bootcamp Tutor Application!
Created By: Vincent Moussa
Last Edited: 09/02/2021

This program will sort any list of numbers in ascending order!
The main focus of this program is to help teach new programmers the basics of coding.

The program constatly finds the next minimum number of the list, and then swaps it to be in the corresponding initial position of the list.

How it Works:
The program loops through every position in the list, this position is stored in currentPosition.
It then does a nested loop, and loops through every position from currentPosition to the end of the list, this nested position is called findMinIndex.
We set the currentMinIndex as the first position in this nested loop. 
We then compare currentMinIndex and the number referenced by findMinIndex, to see which is smaller, in every iteration of the nested loop.
We set the smaller number to currentMinIndex so that it always holds the current minimum number.
Once the nested loop is completed currentMinIndex will hold the minimum number position in the section from currentPosition to the end of the list.
So we swap the currentPosition with this minimum number.
The next iterations of the currentPosition loop repeats these steps for every position so that the list is then sorted in ascending order.

"""



def AscendNumbers(numbersList):
    """
    This function will take in a list of numbers as a parameter, and then
    return the list sorted in ascending order.
    (lists are mutable in python so a return is not needed, but not necessary for beginners to know)
    """

    # for ease and readability purposes, store length of list in variable
    numbersLen = len(numbersList)

    # a for loop that goes through every position in the list.
    for currentPosition in range(numbersLen):

        # store the current position as the min
        currentMinIndex = currentPosition
        
        # a nested for loop from the current position (not incl) to the end of the list.
        for findMinIndex in range(currentPosition + 1, numbersLen):

            # a check to see if the current min is greater than the current findMinIndex number, if true then set current min to it
            if numbersList[currentMinIndex] > numbersList[findMinIndex]:

                currentMinIndex = findMinIndex

        # swap currentMin with currentPosition
        # we need a temp number to store a value for the swap, as one will be overriden in the next line
        tempNumber = numbersList[currentMinIndex]

        # replace numbersList[currentMinIndex] with numbersList[currentPosition]
        numbersList[currentMinIndex] = numbersList[currentPosition]

        # replace numbersList[currentPosition] with tempNumber
        numbersList[currentPosition] = tempNumber

    # function is complete, return sorted list
    return numbersList

# Test Cases

#####
# test case with random numbers
test = [10, 9, 59, 10000, -100, 20, 9]

print("The first test is " + str(test) + " its output should be [-100, 9, 9, 10, 20, 59, 1000]")

test_result = AscendNumbers(test)
print("The output it gave was: " + str(test_result))
                
# spacing out results
print()

######
# test case in reverse order with all negative numbers
test = [-1000, -2000, -3000, -4000]
            
print("The second test is " + str(test) + " its output should be [-4000, -3000, -2000, -1000]")

test_result = AscendNumbers(test)

#spaced out using \n at the end of the print this time
print("The output it gave was: " + str(test_result) + "\n")


######
# test case with empty list 
test = []

print("The third test is " + str(test) + " its output should still be [] (and not an error)")

test_result = AscendNumbers(test)
print("The output it gave was: " + str(test_result) )

# Program completed !! :)

        
        
    

#!/sur/bin/python3

# Import numpy module in program
import numpy as np
# Default function to use iterative approach
def RecurCombo(iterArray, num):
 char = tuple(iterArray) # converting input string into a tuple
 m = len(char) # length of string or tuple
 if num > m: # checking if length of combinations is more than length of string
   return
 index = np.arange(num) # using numpy arrange() function
 # Yielding the first sequence
 yield tuple(char[i] for i in index)
 # Using while loop with true condition
 while True:
  # iterating over the tuple we made using reversed for loop
  for a in reversed(range(num)):
     if index[a] != a + m - num:
         break
     else:
              return
  index[a] += 1
  # another for loop iteration
  for b in range(a + 1, num):
   index[b] = index[b - 1] + 1
  yield tuple(char[a] for a in index) # yielding possible combinations from given string
# Taking an input string from user
inputinputArray = input("Enter an input string to find combinations: ")
# Printing different combinations as result in output
print("All possible combinations of three letter sets from the string given by you is: ")
print([x for x in RecurCombo(inputArray, 3)])

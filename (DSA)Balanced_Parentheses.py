# Balanced Parentheses


# Parentheses are balanced, if all opening parentheses have their corresponding closing parentheses.

# Given an expression as input, we need to find out whether the parentheses are balanced or not.
# For example, "(x+y)*(z-2*(6))" is balanced, while "7-(3(2*9))4) (1" is not balanced.

# The problem can be solved using a stack.
# Push each opening parenthesis to the stack and pop the last inserted opening parenthesis whenever a closing parenthesis is encountered.
# If the closing bracket does not correspond to the opening bracket, then stop and say that the brackets are not balanced.
# Also, after checking all the parentheses, we need to check the stack to be empty -- if it's not empty, then the parentheses are not balanced.

# Implement the balanced() function to return True if the parentheses in the given expression are balanced, and False if not.

# Sample Input:
# (a( ) eee) )

# Sample Output:
# False

# Ans:

def balanced(expression):
    count = 0 
    for char in expression:
        if char == "(":
            count += 1
        elif char == ")":
            if count == 0:
                return False
            count -= 1 
    return count == 0

print(balanced(input()))
    

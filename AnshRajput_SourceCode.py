'''
Code Artifact: Assignment 1 in Python
Description: This assignment, coded in python, prints out each of the following logical expressions as truth tables without hardcoding them.
             The logical expressions include De Morgan’s First Law, De Morgan’s Second Law, the First Associative Law, the Second Associative Law
             [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T, and p ↔ q ≡ (p → q) ∧ (q → p). The program creates a truth table for each of these and
             neatly prints them.
Programmer Name: Ansh Rajput
Date Created: 8/30/21
Preconditons: None; the user does not input anything.
Postconditions: p, q, r are the return variables that return either true or false based on the logical expressions they are used in.
Exception Conditions: None; there are no errors or exceptions.
'''


'''
The following block of code is a function for question 1.
It prints a truth table for De Morgan's First Law.
'''

def question1(): #Creates a function called question1 to be called later.
    print("  | p | q | ¬(p ∧ q) | ¬p ∨ ¬q  |") #prints the top row of the truth table based on question 1.
    
    p = ["F", "F", "T", "T"] #Sets up p as a list that holds true and false values in each possible combination with q.
    q = ["F", "T", "F", "T"] #Sets up q as a list that holds true and false values in each possible combination with p.

    p_values = [False, False, True, True] #Assigns true and false values to p.
    q_values = [False, True, False, True] #Assigns true and false values to q.

    for i in range(4): #creates a for loop that runs 4 times.

        x = not (p_values[i] and q_values[i]) #Converts De Morgan's First Law into a logic expression python can understand.
        y = (not p_values[i]) or (not q_values[i]) #Converts De Morgan's First Law into a logic expression python can understand.

        if x == True: #if x is true,
            x = "True " #print True.
        else: #If x is not true
            x = "False" #print False.
            
        if y == True: #if y is true,
            y = "True" #print True.
        else: #If x is not true,
            y = "False" #print False.
        
        print("  |",  p[i], "|", q[i], "|", x, "   |", y, "   |") #prints and formats the truth table to make it easy-to-read using the values above. 

'''
The following block of code is a function for question 2.
It prints a truth table for De Morgan's Second Law.
'''

def question2(): #Creates a function called question2 to be called later.
    print("  | p | q | ¬(p ∨ q) | ¬p ∧ ¬q |") #prints the top row of the truth table based on question 2.
    
    p = ["F", "F", "T", "T"] #Sets up p as a list that holds true and false values in each possible combination with q.
    q = ["F", "T", "F", "T"] #Sets up q as a list that holds true and false values in each possible combination with p.

    p_values = [False, False, True, True] #Assigns true and false values to p.
    q_values = [False, True, False, True] #Assigns true and false values to q.

    for i in range(4): #creates a for loop that runs 4 times.

        x = not (p_values[i] or q_values[i]) #Converts De Morgan's Second Law into a logic expression python can understand.
        y = (not p_values[i]) and (not q_values[i]) #Converts De Morgan's Second Law into a logic expression python can understand.

        if x == True: #if x is true,
            x = "True " #print True.
        else: #If x is not true
            x = "False" #print False.
            
        if y == True: #if y is true,
            y = "True" #print True.
        else: #If x is not true,
            y = "False" #print False.
        
        print("  |",  p[i], "|", q[i], "|", x, "   |", y, "  |") #prints and formats the truth table to make it easy-to-read using the values above. 

'''
The following block of code is a function for question 3.
It prints a truth table for the First Associative Law.
'''

def question3(): #Creates a function called question3 to be called later.
    print("  | p | q | r | (p ∧ q) ∧ r | p ∧ (q ∧ r) |") #prints the top row of the truth table based on question 3.
    
    p = ["F", "F", "F", "F", "T", "T", "T", "T"] #Sets up p as a list that holds true and false values in each possible combination with q and r.
    q = ["F", "F", "T", "T", "F", "F", "T", "T"] #Sets up q as a list that holds true and false values in each possible combination with p and r.
    r = ["F", "T", "F", "T", "F", "T", "F", "T"] #Sets up r as a list that holds true and false values in each possible combination with p and q.

    p_values = [False, False, False, False, True, True, True, True] #Assigns true and false values to p.
    q_values = [False, False, True, True, False, False, True, True] #Assigns true and false values to q.
    r_values = [False, True, False, True, False, True, False, True] #Assigns true and false values to r.

    for i in range(8): #creates a for loop that runs 8 times.

        x = (p_values[i] and q_values[i]) and r_values[i] #Converts the First Associative Law into a logic expression python can understand.
        y = p_values[i] and (q_values[i] and r_values[i]) #Converts the First Associative Law into a logic expression python can understand.

        if x == True: #if x is true,
            x = "True " #print True.
        else: #If x is not true
            x = "False" #print False.
            
        if y == True: #if y is true,
            y = "True" #print True.
        else: #If x is not true,
            y = "False" #print False.
        
        print("  |",  p[i], "|", q[i], "|", r[i], "|", x, "      |", y, "      |") #prints and formats the truth table to make it easy-to-read using the values above. 

'''
The following block of code is a function for question 4.
It prints a truth table for the Second Associative Law.
'''

def question4(): #Creates a function called question4 to be called later.
    print("  | p | q | r | (p ∨ q) ∨ r | p ∨ (q ∨ r) |") #prints the top row of the truth table based on question 4.
    
    p = ["F", "F", "F", "F", "T", "T", "T", "T"] #Sets up p as a list that holds true and false values in each possible combination with q and r.
    q = ["F", "F", "T", "T", "F", "F", "T", "T"] #Sets up q as a list that holds true and false values in each possible combination with p and r.
    r = ["F", "T", "F", "T", "F", "T", "F", "T"] #Sets up r as a list that holds true and false values in each possible combination with p and q.

    p_values = [False, False, False, False, True, True, True, True] #Assigns true and false values to p.
    q_values = [False, False, True, True, False, False, True, True] #Assigns true and false values to q.
    r_values = [False, True, False, True, False, True, False, True] #Assigns true and false values to r.

    for i in range(8): #creates a for loop that runs 8 times.

        x = (p_values[i] or q_values[i]) or r_values[i] #Converts the Second Associative Law into a logic expression python can understand.
        y = p_values[i] or (q_values[i] or r_values[i]) #Converts the Second Associative Law into a logic expression python can understand.

        if x == True: #if x is true,
            x = "True " #print True.
        else: #If x is not true
            x = "False" #print False.
            
        if y == True: #if y is true,
            y = "True" #print True.
        else: #If x is not true,
            y = "False" #print False.
        
        print("  |",  p[i], "|", q[i], "|", r[i], "|", x, "      |", y, "      |") #prints and formats the truth table to make it easy-to-read using the values above. 

'''
The following block of code is a function for question 5.
It prints a truth table for the logical expression:
[(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T
'''

def question5(): #Creates a function called question5 to be called later.
    print("  | p | q | r | [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r | T      |") #prints the top row of the truth table based on question 5.
    
    p = ["F", "F", "F", "F", "T", "T", "T", "T"] #Sets up p as a list that holds true and false values in each possible combination with q and r.
    q = ["F", "F", "T", "T", "F", "F", "T", "T"] #Sets up q as a list that holds true and false values in each possible combination with p and r.
    r = ["F", "T", "F", "T", "F", "T", "F", "T"] #Sets up r as a list that holds true and false values in each possible combination with p and q.

    p_values = [False, False, False, False, True, True, True, True] #Assigns true and false values to p.
    q_values = [False, False, True, True, False, False, True, True] #Assigns true and false values to q.
    r_values = [False, True, False, True, False, True, False, True] #Assigns true and false values to r.

    for i in range(8): #creates a for loop that runs 8 times.

        x = not((p_values[i] or q_values[i]) and ((not p_values[i]) or r_values[i]) and ((not q_values[i]) or r_values[i])) or (r_values[i])
        #Converts [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T into a logic expression python can understand.
        y = True #Makes y equal true based on the logic equation.

        if x == True: #if x is true,
            x = "True " #print True.
        else: #If x is not true
            x = "False" #print False.
            
        if y == True: #if y is true,
            y = "True" #print True.
        else: #If x is not true,
            y = "False" #print False.
        
        print("  |",  p[i], "|", q[i], "|", r[i], "|", x, "                            |", y, "  |") #prints and formats the truth table to make it easy-to-read using the values above. 

'''
The following block of code is a function for question 6.
It prints a truth table for the logical expression:
p ↔ q ≡ (p → q) ∧ (q → p)
'''
        
def question6(): #Creates a function called question6 to be called later.
    print("  | p | q | p ↔ q    | (p → q) ∧ (q → p) |") #prints the first and second row of the truth table.
    print("  | p | q | ¬(p ∨ q) | ¬p ∧ ¬q           |")
    
    p = ["F", "F", "T", "T"] #Sets up p as a list that holds true and false values in each possible combination with q.
    q = ["F", "T", "F", "T"] #Sets up q as a list that holds true and false values in each possible combination with p.

    p_values = [False, False, True, True] #Assigns true and false values to p.
    q_values = [False, True, False, True] #Assigns true and false values to q.

    for i in range(4): #creates a for loop that runs 4 times.

        x = ((p_values[i] and q_values[i]) or ((not p_values[i]) and (not q_values[i]))) #Converts (p → q) ∧ (q → p) into a logic expression python can understand.
        y = ((not p_values[i] or q_values[i]) and (not q_values[i] or p_values[i])) #Converts (p → q) ∧ (q → p) into a logic expression python can understand.

        if x == True: #if x is true,
            x = "True " #print True.
        else: #If x is not true
            x = "False" #print False.
            
        if y == True: #if y is true,
            y = "True" #print True.
        else: #If x is not true,
            y = "False" #print False.
        
        print("  |",  p[i], "|", q[i], "|", x, "   |", y, "            |") #prints and formats the truth table to make it easy-to-read using the values above. 

'''
The following block of code calls all of functions
previously created above and prints out the truth
tables in a clean and easy-to-read format.
'''

print("\nQuestion 1:") #Prints to format the output neatly.
question1() #Calls the function written for question 1, De Morgan’s First Law.

print("\nQuestion 2:") #Prints to format the output neatly.
question2() #Calls the function written for question 2, De Morgan’s Second Law.

print("\nQuestion 3:") #Prints to format the output neatly.
question3() #Calls the function written for question 3, First Associative Law.

print("\nQuestion 4:") #Prints to format the output neatly.
question4() #Calls the function written for question 4, Second Associative Law.

print("\nQuestion 5:") #Prints to format the output neatly.
question5() #Calls the function written for question 5.

print("\nQuestion 6:") #Prints to format the output neatly.
question6() #Calls the function written for question 6.

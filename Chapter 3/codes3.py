# Basic exercises 3.1

print("Basic exercises 3.1")
A = ['E5', 'E6', 'E7', 'E8']
B = ['E5', 'E7', 'E9', 'E11']
S = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9','E10', 'E11']
print(f"The intersection A B is {[i for i in A if i in B]}")
# The intersection A B is ['E5', 'E7']
print(f"The union of A and B is {[A+B]}")
# The union of A and B is [['E5', 'E6', 'E7', 'E8', 'E5', 'E7', 'E9', 'E11']]
print(f"The A and B are {'not' if A+B==S else ''} collectively exhaustive as they have {len([i for i in  A if i in B])} in common")


# Basic exercises 3.2-3.4

S = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10']

# 3.2

print("Basic exercises 3.2")
A = ['E1', 'E3', 'E6', 'E9']
print(f"Complements of A are {[i for i in S if i not in A]}")
# Complements of A are ['E2', 'E4', 'E5', 'E7', 'E8', 'E10']


# 3.3

print("Basic exercises 3.3")
A_compl=['E1', 'E4', 'E5', 'E7']
B_compl=['E2', 'E3', 'E5', 'E8']
A=[i for i in S if i not in A_compl]
B=[i for i in S if i not in B_compl]
print(f"a) What is A intersection B_compl?\n{[i for i in A if i in B_compl]}")
print(f"b) What is A intersection B?\n {[i for i in A if i in B ]}")
print(f"c) What is A intersection B?\n {[A+B]}")
print(f"The A and B are {'not' if A+B==S else ''} collectively exhaustive as they have {len([i for i in  A if i in B])} in common")
        

# Basic exercises 3.4
print("Basic exercises 3.4")
A = ['E3', 'E5', 'E7', 'E10']
B =['E3', 'E4', 'E5', 'E9']
print(f"a. What is the intersection of A and B?\n {[i for i in A if i in B]}")
print(f"b. What is the union of A and B?\n{A+B}")
print(f"c. Is the union of A and B collectively exhaustive?\nThe A and B are {'not' if A+B==S else ''} collectively exhaustive as they have {len([i for i in  A if i in B])} in common")


# Basic exercises 3.5
print("Basic exercises 3.5")
S=list(range(1,11))
A=[i for i in S if i>3]
B=[i for i in S if i<7]
A_compl=[i for i in S if i not in A]
print(f"Describe the event that is the complement of event A./n{[i for i in S if i not in A]}")
print(f"b. Describe the event that is the intersection of events A and B.\n{[i for i in A if i in B]}")
print(f"c. Describe the event that is the union of events and B.\n{A+B}")
print(f"d. Are events A and B mutually exclusive?\n Events A and B are {'not' if len(A+B)!=len(A)+len(B) else ''} because there is {'nothing' if len(A+B)!=len(A)+len(B) else [i for i in A if i in B]} in common")
print(f"e. Are events A and B collectively exhaustive?\nThe A and B are {'not' if A+B==S else ''} collectively exhaustive as they have {len([i for i in  A if i in B])} in common")
print(f"f. Show that (uA_B)u(A_compl_B)=B.\n{([i for i in A if i in B]+[i for i in B if i in A_compl])}={B}")



# Basic exercises 3.6

print("Basic exercises 3.6")

print("Consider Example 3.4, with the following four basic outcomes for the Dow Jones Industrial Average over two consecutive days:\nO1: The Dow Jones average rises on both days.\nO2: The Dow Jones average rises on the first daybut does not rise on the second day\nO3: The Dow Jones average does not rise on the first day but rises on the second day.\nO4: The Dow Jones average does not rise on either day.\nLet events A and B be the following:\nA: The Dow Jones average rises on the first day.\nB: The Dow Jones average rises on the second day.")

A=['O1','O2']
B=['O2','O3']
all=set(A+B+['O4'])
print(all)
A_compl=[i for i in all if i not in A]
B_compl=[i for i in all if i not in B]

print(f"\na. Show that (A-B)u(A_compl-B)=B.\n{[i for i in A if i in B]+[i for i in B if i in A_compl]}={B}")
print(f"\nb. Show that Au(A_compl-B)=AuB.\n{A+[i for i in A_compl if i in B]}={set(A+B)}")



# Basic exercises 3.7

print("\nBasic exercises 3.7")

# Florin Frenti operates a small, used car lot that has three Mercedes (M1, M2, M3) and two Toyotas (T1, T2). Two customers, Cezara and Anda, come to his lot, and each selects a car. The customers do not know each other, and there is no communication between them. Let the events A and B be defined as follows:
# A: The customers select at least one Toyota.
# B: The customers select two cars of the same model.
A=['T1,T2','T1,M1','T1,M2','T1,M3','T2,M1','T2,M2','T2,M3']
B=['T1,T2','M1,M2','M1,M3','M2,M3']
print(f"\na. Identify all pairs of cars in the sample space.\n{set(A+B)}")
print(f"\nb. Define event A.\n{A}")
print(f"\nc. Define event B.\n{B}")
print(f"\nd. Define the complement of A.\n{[i for i in set(A+B) if i not in A]}")
print(f"\ne. Show that (A-B)u(A_compl-B)=B\n{set([i for i in A if i in B]+[i for i in B if i not in A])}={B}")
print(f"\nf. Show that Au(A_compl-B)=AuB.\n{set(A+[i for i in B if i not in A])}={set(A+B)}")


# Basic Exercises

print("\nBasic Exercises")
import math
from math import comb
print(f"\n3.8 The sample space contains 5 As and 7 Bs. What is the probability that a randomly selected set of 2 will include 1 A and 1 B?\n{(5*7)/(comb(12,2))}")
print(f"\n3.9 The sample space contains 8 As and 6 Bs. What is the probability that a randomly selected set of 3 will include 2 As and 4 Bs?\n{(comb(8,2)*comb(6,4))/comb(14,6)}")
print(f'\n3.10 The sample space contains 10 As and 6 Bs. What is the probability that a randomly selected set of 4 will include 2 As and 2 Bs?\n{(comb(10,2)*comb(6,2)/comb(16,4))}')
print(f"\n3.11 In a city of 140,000 people there are 40,000 Norwegians.What is the probability that a randomly selected person from the city will be Norwegian?\n{40/140}")
print(f"\n3.12 In a city of 180,000 people there are 20,000 legal immigrants from Latin America. What is the probability that a random sample of two people from the city will contain two legal immigrants from Latin America?\n{comb(20000,2)/(comb(180000,2))}")

print("\n3.13 Sale manager wants to estimate a probability that a car will be returned for a service during the warranty period. The following table shows a manager’s probability assessment for the number of returns.\nNumber of Returns (X)   0 1 2 3 4 \nProbability P(X) 0.28 0.36 0.23 0.09 0.04\nLet A be the event “the number of returns will be more than two,” and let B be the event “the number of returns will be less than four.”\nb. Find the probability of event B.\nc. Find the probability of the complement of event A\nd. Find the probability of the intersection of events A and B.\ne. Find the probability of the union of events A and B.")
X=list(range(0,5))
print(X)
p_X=[0.28,0.36,0.23,0.09,0.04]
A=[i for i in X if i>2]
B=[i for i in X if i<4]
A_compl=[i for i in X if i not in A]
B_compl=[i for i in X if i not in B]
p_A=[p_X[i] for i in A]
p_B=[p_X[i] for i in B]
p_A_compl=[p_X[i] for i in A_compl]
p_B_compl=[p_X[i] for i in B_compl]
p_A_i_B=[i for i in A_compl if i in B_compl]
print(f"\na. Find the probability of event A.\n{sum(p_A)}")
print(f"\nb. Find the probability of event B.\n{sum(p_B)}")
print(f"\nc. Find the probability of the complement of event A.\n{sum(p_A_compl)}")
print(f"\nd. Find the probability of the intersection of events A and B.\n{sum(p_A_i_B)}")
print(f"\ne. Find the probability of the union of events A and B.{sum(set(p_A+p_B))}")

print("\n4.90 A long-distance taxi service owns four vehicles. These are of different ages and have different repair records. The probabilities that, on any given day, each vehicle will be available for use are 0.95, 0.90, 0.90, and 0.80. Whether one vehicle is available is independent of whether any other vehicle is available.")
p_X=[0.95,0.90,0.90,0.80]
print("\na. Find the probability distribution for the number of vehicles available for use on a given day.")
x_0=[1-i for i in p_X]
def Multiplicator(l:list):
    result=1
    for i in l:
        result*=i
        return result

print(Multiplicator(x_0))
x_1=[i*(1-t) for i,t in set()]
print()
print(f"\nb. Find the expected number of vehicles available for use on a given day.\n{sum(p_X)}")
print(f"\nc. Find the standard deviation of the number of vehicles available for use on a given day.\n")





# Exercise 4.85
print("\n4.85 Exercise\n")
print(f"\na. Does the advice imply that after purchasing health insurance it is not necessary to get home insurance? ")
print(f"\nDoes the advice imply that after purchasing health insurance it is not necessary to get home insurance?\nGetting health insurance is more meaningfull than home insuranse as a human can use medical insurance not once but regularly. It's a different between medinsurance and home insurance, also risk of being sick is higher. About damage: let's say the person breakes his arm, if the damage=30 dollars, else(home insurance)=200$,but risks are 0.5 and 0.01, then average(expected) costs are 15 dollars and 2 dollars. Because the cost without med insurance is high, it's better\nb. Is the compensation received from health insurance higher than that from home insurance?\nNo")

# Exercise 4.86
print("\n Exercise 4.86")
def E_x(x:list,p:list):
    px=[i*pr for i,pr in zip(x,p)]
    ex=sum(px)
    return ex 

def P_3(p:list):
    ps=[i for i in p[0:2]]
    px=sum(ps)
    return px 

days=[1,2,3,4,5]
prob=[0.05, 0.20, 0.35, 0.30, 0.10]
print(f"\na) {E_x(days,prob)}")
print(f"\nb) {P_3(prob)}")


def Var(x:list,p:list):
    px=[i*pr for i,pr in zip(x,p)]
    ex=sum(px)
    vx=sum([(i-ex)**2*n for i,n in zip (x,p)])
    return vx



def Std_(x):
    std=x**0.5
    return std
print(f"\nc) {Std_(Var(days,prob))}")
print(f"\nd) Mean: {20000+2000*E_x(days,prob)} \nStandart deviation {20000+2000*Std_(Var(days,prob))}")


# 4.87 


print("\n4.87 A car salesperson estimates the following probabilities for the number of cars that she will sell in the next week:")
def P_2_less(p:list):
    ps=[i for i in p[0:1]]
    px=sum(ps)
    return px 
def P_2_at_least(p:list):
    ps=[i for i in p[3:]]
    px=sum(ps)
    return px 
num=[0,1,2,3,4,5]
prob=[0.10, 0.20, 0.35, 0.16, 0.12, 0.07]
print(f"\na) {E_x(num,prob)}")
print(f"\nb) {Std_(Var(num,prob))}")
print(f"\nc) Mean: {250+300*E_x(num,prob)}\nStd: {300*Std_(Var(num,prob))}")
print(F"\nd) 250+300x>1000, x>2.5. \n{P_2_at_least(prob)}.")





import math
import pandas as pd
import matplotlib as plt

# Exercise 4.100

print("\nExercise 4.100\n4.100 George Allen has asked you to analyze his stock portfolio, which contains 10 shares of stock D and 5 shares of stock C. The joint probability distribution of the stock prices is shown in Table 4.10. Compute the mean and variance for the total value of his stock portfolio.")

import pandas as pd
import numpy as np

# Joint probability table
data = {
    40: [0.00, 0.05, 0.10, 0.20],
    50: [0.00, 0.00, 0.05, 0.10],
    60: [0.05, 0.05, 0.00, 0.05],
    70: [0.20, 0.10, 0.05, 0.00]
}

# X values (Stock C)
X_vals = [45, 50, 55, 60]

df = pd.DataFrame(data, index=X_vals)

# Convert to long format
df_long = df.stack().reset_index()
df_long.columns = ['X', 'Y', 'P']

# Portfolio value T = 5X + 10Y
df_long['T'] = 5 * df_long['X'] + 10 * df_long['Y']

# Expected value
E_T = (df_long['T'] * df_long['P']).sum()

# Expected value of T^2
E_T2 = ((df_long['T']**2) * df_long['P']).sum()

# Variance
Var_T = E_T2 - E_T**2

print(df)
print("")
print(df_long)
print("E[T] =", E_T)
print("Var(T) =", Var_T)




print('\n4.102 When buying property, one of the main considerations for a homebuyer is the reputation of a property developer, that is, if they follow good construction practices, offer financial security, and deliver on time. For the previous month, a random sample of the daily number of units sold at a new housing area by one of the top property developers in your state is recorded as follows: 8, 6, 7, 10, 6, 14, 6, 6, 6, 11, 12, 7, 9, 15, 8, 11, 12, 9, 8, 9.\na. What probability model should be used and why?\nb. What is the probability that 10 or more units will\nbe sold on a typical future date?\nc. What is the probability of selling less than 7 units?\nd. Find the number of units sold such that the probability of exceeding this number is 10% or less.')

print("a) Poisson\nb) ")
 

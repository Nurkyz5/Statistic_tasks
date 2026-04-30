
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
 
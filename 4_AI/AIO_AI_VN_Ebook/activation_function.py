import math as m

alpha = 1.0

def sigmoid(x):
    return 1/(1+m.exp(-x))
def ReLU(x):
    if x > 0:
        return x
    return 0
def ELU(x):
    if x > 0:
        return x
    return alpha*(m.exp(x)-1)
    


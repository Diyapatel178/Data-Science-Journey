import numpy as np

numbers = np.array([10,20,30,40,50,60])

a1 = numbers.reshape(2,3)
a2 = numbers.reshape(3,2)

print("a1:",a1)
print("a2:",a2)
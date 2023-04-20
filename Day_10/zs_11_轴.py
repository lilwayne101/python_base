import numpy as np

# interest_score = np.random.randint(10, size=(4, 3, 2))
# print(interest_score)
# print("-----------------")
# print(np.sum(interest_score, axis=0))
# print("-----------------")
# print(np.sum(interest_score, axis=1))
# print(np.sum(interest_score, axis=2))
# print("-------------------")

a = np.arange(6).reshape(2, 3)
print(a)
print(a.T)
print(a.T.swapaxes(1, 0))

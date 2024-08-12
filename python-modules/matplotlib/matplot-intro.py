import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
1-
x = [1, 2, 3, 4]
y = [2, 34, 12, 41]
plt.plot(x, y,"--g", color="red", linewidth="3")
plt.axis([0, 4, 0, 41])  # defines limits of an axis

plt.title("Complicated Numbers")
plt.xlabel("x numbers")
plt.ylabel("y numbers")
"""
"""
2-
x = np.linspace(0,2,100)
plt.plot(x,x, label = "linear")
plt.plot(x,x**2, label = "quadratic")
plt.plot(x,x**3, label = "cubic")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("Title Example")
plt.legend()

plt.show()

"""
"""
3-
x = np.linspace(0,2,100)

# three graphs are created
fig, axis = plt.subplots(3)
axis[0].plot(x, x, color="red")
axis[0].set_title("linear")

axis[1].plot(x, x ** 2, color="yellow")
axis[1].set_title("quadratic")

axis[2].plot(x, x ** 3, color="blue")
axis[2].set_title("cubic")

plt.tight_layout()
"""
"""
x = np.linspace(0.1, 2, 100)
list = [1, 2, 3, 4, 5, 6]

fig, axis = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("X behavior of lin,quad,cub,quar")
axis[0, 0].plot(x, x, color="blue")
axis[0, 1].plot(x, x ** 2, color="pink")
axis[1, 0].plot(x, x ** 3, color="black")
axis[1, 1].plot(x, x ** 4, color="purple")

plt.tight_layout()
"""

df = pd.read_csv("../pandas/datasets/nba.csv")

df = df.drop(["Number"], axis=1)

df = df.groupby("Team")[["Salary", "Weight", "Age"]].mean()

df.plot(subplots=True, figsize=(12, 4))
plt.legend()
plt.tight_layout()
plt.show()

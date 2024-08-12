import matplotlib.pyplot as plt

"""
years = [2016, 2017, 2018, 2019, 2020]

player1 = [2, 3, 7, 3, 11]
player2 = [21, 32, 16, 19, 23]
player3 = [5, 8, 11, 12, 9]

# Stack Plot

plt.plot([], [], color="y", label="player1")
plt.plot([], [], color="r", label="player2")
plt.plot([], [], color="b", label="player3")

plt.stackplot(years, player1, player2, player3, colors=["y", "r", "b"])

plt.title("Goals Over the Years")
plt.xlabel("Years")
plt.ylabel("Goals")
plt.legend()
plt.show()
"""

"""pie chart
goal_types = ["Freekick", "Penalty", "Corner", "Inside the Penalty Area"]

goals = [12, 15, 29, 35]
colors = ['y', 'r', 'b']

plt.pie(goals, labels=goal_types, colors=colors, shadow=True, explode=(0.05, 0.05, 0.05,))

plt.show()
"""

""" 
Bar chart
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,60,30,40,90],label="BMW",width=0.5)
plt.bar([0.55,1.65,2.75,3.85,4.95],[80,90,40,50,60],label="Audi",width=0.5)

plt.legend()
plt.xlabel("Day")
plt.ylabel("Distance (Km)")
plt.title("Car Details")

plt.show()
"""

"""
histogram graph
ages = [ 45, 37, 23, 59, 68, 33, 51, 28, 72, 14, 39, 49, 71, 21]

age_groups=[10,20,30,40,50,60,70,80]

plt.hist(ages,age_groups,histtype="bar", rwidth=0.5)
plt.xlabel("Number of person")
plt.ylabel("Age groups")
plt.title("Internet Usage by Age")

plt.show()

"""





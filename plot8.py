from matplotlib import pyplot as plt

x = [7,2,2,13,5]
activities = ['sleeping', 'eating', 'working', 'playng']
cols = ['c','m','r','b','k']

plt.pie(x,
	labels=activities,
	colors=cols,
	startangle=90,
	shadow=True,
	explode=(0,0,0,0),
	autopct= '%1,3f%%')

plt.title("Pie Chart")
plt.show()
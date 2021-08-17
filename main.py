# imports packages/libs we will use
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Activate Seaborn
# notice I am using the alias
sns.set()
# Set the axes
# notice I am using the alias
plt.axis([0, 50, 0, 50])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Temp", fontsize=30)
plt.ylabel("Cones Sold", fontsize=30)
# Let's load the data and skip the first row of headers
# So we just get the data
X, Y = np.loadtxt("TempICSalesData.txt", skiprows=1, unpack=True)
# let's plot out our data
plt.plot(X, Y, "bo")
# We have to do this to show our data
plt.show()



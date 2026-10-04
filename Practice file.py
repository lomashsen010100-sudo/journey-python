import matplotlib.pyplot as plt

month=["january", "Februry", "march", "april", "may", "june",]
product=[10, 20, 30, 40, 50, 60]

ax=plt.subplots()

plt.title("Sales Graph")
plt.xlabel("month")
plt.ylabel("product")
plt.bar(month, product)
plt.grid()
fig, ax=plt.subplots(1,1)


plt.title("Sales Graph")
plt.xlabel("month")
plt.ylabel("product")
plt.plot(month, product)
plt.grid()
fig, ax=plt.subplots(1,2)
plt.show()
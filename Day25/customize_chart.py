import matplotlib.pyplot as plt

city = ["Ahemdavad","Surat","Rajkot","Vadodra"]
student = [3,2,3,2]

plt.bar(city,student)

plt.title("Students by city")
plt.xlabel("City")
plt.ylabel("Number of student")
plt.grid(axis="y")

plt.show()
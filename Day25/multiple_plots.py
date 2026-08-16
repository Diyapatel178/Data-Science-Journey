import matplotlib.pyplot as plt

cities = ["Ahmedabad", "Surat", "Vadodara", "Rajkot"]
students = [3, 3, 2, 2]

marks = [85, 92, 78, 88, 67, 95, 74, 81, 90, 76]

plt.subplot(1,2,1)
plt.bar(cities,students)
plt.title("Student by city")

plt.subplot(1,2,2)
plt.hist(marks)
plt.title("marks dustribution")

plt.show()
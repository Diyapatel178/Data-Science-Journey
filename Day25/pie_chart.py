import matplotlib.pyplot as plt

cities = ["Ahmedabad", "Surat", "Vadodara", "Rajkot"]
students = [3, 3, 2, 2]

plt.pie(students,labels=cities,autopct="%1.1f%%")
plt.title("Student Distribution by city")

plt.show()
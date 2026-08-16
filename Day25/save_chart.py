import matplotlib.pyplot as plt

cities = ["Ahmedabad", "Surat", "Vadodara", "Rajkot"]
students = [3, 3, 2, 2]

plt.bar(cities,students)

plt.title("student by city")
plt.xlabel("City")
plt.ylabel("Number of student")

plt.savefig("student_by_city.png")

plt.show()
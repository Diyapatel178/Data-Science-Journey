import statistics

marks = [85, 92, 78, 88, 67, 95, 74, 81, 90, 76]

print("===== STATISTICS SUMMARY =====")

print("Mean:",statistics.mean(marks))
print("Median:",statistics.median(marks))
print("Mode:",statistics.mode(marks))
print("Variance:",statistics.variance(marks))
print("Stadard Deviation:",statistics.stdev(marks))
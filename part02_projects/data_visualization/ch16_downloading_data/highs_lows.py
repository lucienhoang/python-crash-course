import csv

from matplotlib import pyplot as plt

# Get high temperatures from file.
filename = "files/sitka_weather_2021.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        if row[4] != "":
            high = int(row[4])
            highs.append(high)

    # print(highs)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c="red")

# Format plot.
plt.title("Daily high temprratures, 2021.")
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

# sitka_weather_2021.csv
#           │
#           ▼
#       csv.reader
#           │
#           ▼
#    bỏ dòng header
#           │
#           ▼
#      for từng row
#           │
#           ▼
#        row[4] cột thứ 4
#           │
#           ▼
#     nhiệt độ cao nhất
#           │
#           ▼
#      highs.append()
#           │
#           ▼
#       print(highs)

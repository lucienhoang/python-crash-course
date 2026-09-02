import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates and high temperatures from file.
filename = "files/sitka_weather_2021.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []

    for row in reader:
        if row[4] != "":
            current_date = datetime.strptime(row[2], "%Y-%m-%d")  # noqa: DTZ007
            dates.append(current_date)

            high = int(row[4])
            highs.append(high)

    # print(highs)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")

# Format plot.
plt.title("Daily high temperatures, 2021.")
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
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

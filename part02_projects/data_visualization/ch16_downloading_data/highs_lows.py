import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high and lows temperatures from file.
filename = "files/death_valley_2021_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")  # noqa: DTZ007
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


# Format plot.
plt.title("Daily high and low temperatures, 2021.")
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.xlim(datetime(2021, 1, 1), datetime(2021, 12, 31))  # noqa: DTZ001

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

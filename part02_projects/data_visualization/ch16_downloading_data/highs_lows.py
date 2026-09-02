import csv

filename = "files/sitka_weather_2021.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[4])
        highs.append(high)

    print(highs)


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

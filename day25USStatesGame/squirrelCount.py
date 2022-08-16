import csv
import pandas
import string
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    for row in data:
#        print(row)

#Figure out num of gray, white, and cinnamon squirrels
nan = 0
gray = 0
white = 0
cinnamon = 0

data = pandas.read_csv("squirrel_census.csv")
list = data["Primary Fur Color"]
for row in list:
    row = str(row)
    if row == "nan":
        nan += 1
    elif row == 'Gray':
        gray += 1
    elif row == 'White':
        white += 1
    else:
        cinnamon += 1
data_count = {
    "Color": ["White", "Gray", "Cinnamon", "N/A"],
    "Count": [white,gray,cinnamon,nan]
}
data = pandas.DataFrame(data_count)
data.to_csv("squirrel_fur_count.csv")
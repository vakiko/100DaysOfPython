travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, times_visited, cities_visited):
  if times_visited > 1:
    print("You have visited", country, times_visited, "times.")
  else:
    print("You have visited", country, times_visited, "time.")
  length = len(cities_visited)
  if length > 1:
      print("You have been to", ', '.join(cities_visited[0:length-1]), "and", cities_visited[length-1])
  else:
    print("You have been to", cities_visited[length-1])
  sub_dict = {
                "country": country,
                "visits": times_visited,
                "cities": cities_visited
              }
  travel_log.append(sub_dict)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

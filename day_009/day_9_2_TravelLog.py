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
def add_new_country(user_country,user_visits,user_cities):
    travel_log_2 = {}
    travel_log_2["country"] = user_country
    travel_log_2["visits"] = user_visits
    travel_log_2["cities"] = user_cities
    travel_log.append(travel_log_2)  
    




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

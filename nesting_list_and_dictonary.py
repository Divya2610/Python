#Nesting
capitals = {
    "France" : "Paris",
    "Germany" :"Berlin",
}

#Nesting a List in a dictonary
travel_log = {
    "France":  ["Paris", "Lille", "Dijon"], 
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    }

#Nesting Dictonary in a dictonary
travel_log = {
    "France": {"cities_visited ": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany":{"cities_visited ": ["Berlin", "Hamburg", "Stuttgart"],"total_visits": 5},
    }

#Nesting Dictonary in a list
travel_log = [
    {
        "country":"France", 
        "cities_visited ": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
},
{
    "country":"Germany",
    "cities_visited ": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5 
},
    
]

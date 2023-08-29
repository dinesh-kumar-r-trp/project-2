url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

import requests as r

# Fetch and structure data
data = r.get(url)
data = data.json()
results = {}
for record in data["list"]:
    results[record["dt_txt"]] = record


inputs = {"0": "exit" , "1": "Enter date with time to get temprature (ex:yyyy-mm-dd hh:mm:ss)" , "2": "Enter date with time to get wind speed  (ex:yyyy-mm-dd hh:mm:ss)" , "3":"Enter date with time to get pressure  (ex:yyyy-mm-dd hh:mm:ss)"}

while 1:
    item = input("Enter value to continue:- \n 1 - Get Temprature \n 2 - Get Wind speed \n 3 - Get Pressure \n 0 -Quit ")
    
    if item == "0":
        print("Quitting....")
        break
    if item not in inputs.keys():
        print("Wrong option")
        continue
    
    # get input
    date_time = input(inputs[item])
    date_time = date_time.strip()
    result = results.get(date_time)
    
    # un handled inputs     
    if not result:
        print("Invalid date time (ex:yyyy-mm-dd hh:mm:ss) interval one hour")
        continue
    
    # Core     
    if item == "1":
        print(f'Min:- {result["main"]["temp_min"]} , Max:- {result["main"]["temp_max"]}')
    elif item == "2":
        print(" Speed :",result["wind"]["speed"])
    elif item == "3" :
        print(" Pressure :",result["main"]["pressure"])
    else:
        print("wrong option")
        
    print("-"*20)
        
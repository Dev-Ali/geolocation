import sys
import json
from datetime import datetime
import urllib.request, urllib.parse, urllib.error

api_key = None
# If you have a google maps API key, enter it here
# api_key = "abC_342_key"
# Otherwise, set the value to None
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is None:
    api_key = 42
    service_url = "http://py4e-data.dr-chuck.net/json?"
else:
    service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location: ")
    if len(address) < 1 : break

    parameters = dict()
    if api_key is not None:
        parameters["address"] = address
        parameters["key"] = api_key

    url = service_url + urllib.parse.urlencode(parameters)
    #Pretty little banner
    print("-" * 50)
    print("Time Started:", datetime.now())
    print("Reteriving: " + url)
    print("-" * 50)

    #Extracting Data
    print("[+] Searching for the location")
    try:
        connection = urllib.request.urlopen(url)
    except:
        print("==== Failure To Connect ====")
        sys.exit()

    data = connection.read().decode()
    print("[+] Reterived", len(data), "characters")
    
    #Parsing Json Data
    try:
        js = json.loads(data)
    except:
        print("==== Failure To Parse Json Data")
        sys.exit()
    
    ask = input("Do you wish to save the extracted Json data? ")
    ans = ("yes", "Yes")
    if ask in ans:
        path = input("Enter the path: ")
        if "\\" in path:
            new_path = path.replace("\\", "/")
            try:
                handle = open(new_path, "w")
            except:
                print("==== File Not Found ====")
                continue
        else:
            try:
                handle = open(path, "w")
            except:
                print("==== File Not Found ====")
                continue
        handle.write(json.dumps(js, indent=4))
        print("[+] Data has been written to the file")
        sys.exit()
    else:
        for value in js["results"]:
            print("Latitude:", value['geometry']['location']['lat'])
            print("Longitude:", value['geometry']['location']['lng'])




    

    

    

'''
Provide Python code to answer the following questions. 
Include a requirements.txt of your required packages.

Ingest this data set of Green P parking lots: 
https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/b66466c3-69c8-4825-9c8b-04b270069193/resource/8549d588-30b0-482e-b872-b21beefdda22/download/green-p-parking-2019.json

1. What is the number of parking lots in Toronto?

2. What is the maximum rate with a dollar value for any period across all parking lots?

3. What is the total capacity across all parking lots? 

4. What is the total capacity of parking lots that only accept both “Coins” and any type of “Charge”?

5. What changes would you make to this data set? Why?

'''
import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

 
def read_json_from_url(file_path):
    '''
    Description: This function is used to read file from url with the help of urlopen module
    Parameters: file path -> string
    Return: parking data -> dictionary
    '''
    with urllib.request.urlopen(file_path) as url:
        data = json.loads(url.read().decode())
    
    return data

def number_of_parking_lots(data):
    '''
    Description: This function determines how many parking lots are there. 
                 Since each json obj is a parking lot, simply getting the length will tell us 
                 how many there are in total.
    Parameters: parking data -> dictionary
    Return: number of parking lots -> int
    '''
    return len(data["carparks"])

def max_rate(data):
    '''
    Description: This function determines the maximum rate from any of the parking lots. 
                 We need to be careful though because not every 'rate' key, has a number value to it.
                 There are cases where it's empty, where it's 'Free'. We also need to careful as the numbers
                 are not of type int or float, rather a string. 
    Parameters: parking data -> dictionary
    Return: maximum rate -> float
    '''

    #store a temporary max rate
    max_charge = float("-inf")

    for each_parking_lot in data["carparks"]:
        rate_details = each_parking_lot["rate_details"]["periods"]

        for each_period in rate_details:
            for each_rate in each_period["rates"]:
                #only compare prices with values that start with "$"
                if each_rate["rate"].startswith("$"):
                    current_charge = float(each_rate["rate"].split("$")[1])
                    #update the max charge
                    max_charge = max(max_charge, current_charge)

    return max_charge

def total_capacity(data):
    '''
    Description: This function determines the total capacity across all parking lots.
    Parameters: parking data -> dictionary
    Return: total capacity -> integer
    '''
    t_capacity = 0

    for each_parking_lot in data["carparks"]:
        t_capacity += int(each_parking_lot["capacity"])
    
    return t_capacity

def parking_lots_with_coins_and_any_charge_only(data):
    '''
    Description: This function determines the total capacity across all parking lots whom have accept
                 payment options as 'Coins' and 'Charge' only. 
    Parameters: parking data -> dictionary
    Return: 
    '''
    t_capacity = 0

    for each_parking_lot in data["carparks"]:
        payment_methods = each_parking_lot["payment_methods"]
        #make sure there are ONLY 2 options as number of payment options
        #also make sure those 2 options are either 'Coins' or 'Charge' (substring)
        if len(payment_methods) == 2 and "Coins" in payment_methods and any("Charge" in method for method in payment_methods):
            t_capacity += int(each_parking_lot["capacity"])
    
    return t_capacity

#main method
if __name__ == "__main__":

    #read json obj
    json_file_path = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/b66466c3-69c8-4825-9c8b-04b270069193/resource/8549d588-30b0-482e-b872-b21beefdda22/download/green-p-parking-2019.json"
    parking_data = read_json_from_url(json_file_path)

    parking_lot_count = number_of_parking_lots(parking_data)
    print("Total number of parking lots:\t{}".format(parking_lot_count))

    maximum_rate = max_rate(parking_data)
    print("Maximum rate for any period:\t{}".format(maximum_rate))

    capacity_count = total_capacity(parking_data)
    print("Total capacity of all parking lots:\t{}".format(capacity_count))

    capacity_count_with_filter = parking_lots_with_coins_and_any_charge_only(parking_data)
    print("Total capacity with only Coins and Charge:\t{}".format(capacity_count_with_filter))

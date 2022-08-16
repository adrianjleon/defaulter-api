from calendar_functions import is_last_tuesday, get_cronogram_by_year



# TODO 
# OS will run this Script every day (if possible workday) at 10:00 am 
# Set a reliable time source (could be an IP) 
# Extract data from DB and put it into a local DB to test (Luan and Juan)
# Script to predict
# script to save file
# Script to send email
# apply error handling
# containerize the app
# put it into a VM Virtualbox

year = 2023

result_this_last_tuesday_month = is_last_tuesday()

cronogram_by_year = get_cronogram_by_year(year)

# delete the following  lines when you are done with the testing
from datetime import datetime
import random
today_is = datetime.today()


with open(f"/app/prueba{today_is}.txt", "a") as file:
    file.write(f"result_this_last_tuesday_month { result_this_last_tuesday_month } \n {cronogram_by_year } by year {year} \n")




import smtpd
from calendar_functions import is_last_tuesday, get_cronogram_by_year
from email_handler import send_email



# TODO 
# OS will run this Script every day (if possible workday) at 10:00 am 
# Set a reliable time source (could be an IP) 
# Extract data from DB and put it into a local DB to test (Luan and Juan)
# Script to predict
# script to save file
# Script to send email
# apply error handling
# containerize the app
# crontab -e
# crontab minuto hora dia mes dia_de_la_semana
# START CRON JOB
# crontab 0 7 * 3-11 2 python3 /home/limitado/Documents/adrian-python/proyectos/morosidad/main.py
# END CRON JOB
# https://github.com/Adiii717/docker-python-cronjob/blob/master/cron-numpy/Dockerfile
# https://www.linkedin.com/pulse/how-schedule-python-application-docker-container-srinivas-reddy
# put it into a VM Virtualbox




#print(is_last_tuesday())
#print(get_cronogram_by_year(2026)) 

send_email()






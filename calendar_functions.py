from datetime import date 
import calendar 


def is_last_tuesday(year :int = date.today().year, month :int = date.today().month, weekday_value :int = date.today().weekday()) -> bool:
#def is_last_tuesday(year, month, weekdayvalue):
    """ 
        Function takes year and month as parameters and returns a boolean if today is the last tuesday of the month 
        if not receives prameters, it will check actual year and month 
        the module calendar and date should be imported from 'datetime import date' & "import calendar'
    """ 

    # Set Tuesday week value if starting monday as a number 0 
    tuesday = calendar.TUESDAY # 1
    # getting a list of lists. Every list is a week 
    #[[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 0, 0, 0, 0]]
    check_calendar = calendar.monthcalendar(year, month) 
    #print(check_calendar)
    # get last tuesday of the month 
    day_number_to_run = check_calendar[-1][tuesday] or check_calendar[-2][tuesday]
    # return True if today weekday number is equal to last tuesday 
    return day_number_to_run == weekday_value

def get_cronogram_by_year(year :int = date.today().year) -> dict:
    """
    Function takes a year as a parameter and returns a list with the day of the last tuesday of month.
    If a year is not passed then it returns of actual year
    """
    months_fixed = {
    'march': 3,
    'april': 4,
    'may': 5,
    'june':6,
    'july': 7,
    'agost': 8,
    'october': 10,
    'november': 11
    }
    tuesday = calendar.TUESDAY
    cronogram = []
    for month_name, month_value in months_fixed.items():
        c = calendar.monthcalendar(year, month_value)
        day_number_to_run = c[-1][tuesday] or c[-2][tuesday]
        month = {month_name: day_number_to_run}
        cronogram.append(month)
    return {year: cronogram}
    
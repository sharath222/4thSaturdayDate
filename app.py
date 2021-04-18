from datetime import datetime, timedelta

def validate_input(date_string):
    """ Takes a date_string gives datetime and validates the year 

            Parameters:
                    date_string (string): date of format yyyyMMdd. Ex (20200415)

    """
    date = datetime.strptime(date_string, "%Y%m%d")
    if date.year < 1900 or date.year > 2100:
        return None
    else:
        return date


def get_fourth_saturday(start_date, end_date):
    """ Fetches fourth saturdays between given date range

            Parameters:
                    start_date (date): Start Date
                    end_date (date): End Date

    """
    starting_date = validate_input(start_date)
    ending_date = validate_input(end_date)
    if(starting_date == None or ending_date == None):
        print('Invalid Start and End Dates')
    else:
        fourth_dates = []
        while starting_date <= ending_date:
            day = starting_date.isoweekday()
            fourth_saturday = 28 - day
            fourth_sat_date = datetime(
                starting_date.year, starting_date.month, fourth_saturday)
            if(fourth_sat_date > starting_date):
                fourth_dates.append(fourth_sat_date.strftime('%Y%m%d'))
            starting_date = get_next_date(starting_date)
        return fourth_dates

def get_next_date(date):
    """ Calulate next date

            Parameters:
                    date (date): A Date

    """
    month = date.month
    year = date.year
    if month >= 12:
        month = 1
        year = year + 1
    else:
        month = month + 1
    date = datetime(year, month, 1)
    return date


def get_saturday_mulitple_five(start_date, end_date):
    """ Fetches all saturdays which has its date a muliple of 5

            Parameters:
                    start_date (date): Start Date
                    end_date (date): End Date

    """
    starting_date = validate_input(start_date)
    ending_date = validate_input(end_date)
    if(starting_date == None or ending_date == None):
        print('Invalid Start and End Dates')
        return None
    else:
        five_dates = []
        while starting_date <= ending_date:
            if starting_date.isoweekday() == 6 and starting_date.day % 5 == 0:
                five_dates.append(starting_date.strftime('%Y%m%d'))
            starting_date += timedelta(days=1)
        return five_dates

start_date = input('Enter Start Date ')
end_date = input('Enter End Date ')

result_dates = []

# dates = get_fourth_saturday(start_date, end_date) + \
#     get_saturday_mulitple_five(start_date, end_date)

fourth_dates = get_fourth_saturday(start_date, end_date)
five_dates = get_saturday_mulitple_five(start_date, end_date)

result_dates = list(set(fourth_dates)^set(five_dates))

# Remove duplicate items
[result_dates.append(date) for date in result_dates if date not in result_dates]
# adding start and end dates
result_dates.insert(0, start_date)

result_dates.sort()

[print(date) for date in result_dates]

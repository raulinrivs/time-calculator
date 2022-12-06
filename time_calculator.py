import datetime


def add_time(time, time_add, day_week=None):
    if day_week:
        ref_day = reference_day(day_week)
        time = datetime.datetime.strptime(f'{ref_day}-08-22 {time}', '%d-%m-%y %I:%M %p')
    else:
        time = datetime.datetime.strptime(time, '%I:%M %p')
    time_add = time_add.split(':')
    time_add = datetime.timedelta(hours=int(time_add[0]), minutes=int(time_add[1]))
    future_time = time + time_add
    time_interval = datetime.timedelta(days=future_time.day-time.day)
    return string_compose(time_interval, future_time, day_week)


def string_compose(time_interval, future_time, days_week):
    if days_week:
        string = f"{datetime.datetime.strftime(future_time, '%I:%M %p, %A')}"
    else:
        string = f"{datetime.datetime.strftime(future_time, '%I:%M %p')}"
    if time_interval.days == 1:
        string = f"{string} (next day)"
    elif time_interval.days > 1:
        string = f"{string} ({time_interval.days} days later)"
    if string[0] == '0':
        string = string[1:]
    return string


def reference_day(days_week):
    if days_week.lower() == 'monday':
        result = 1
    elif days_week.lower() == 'tuesday':
        result = 2
    elif days_week.lower() == 'wednesday':
        result = 3
    elif days_week.lower() == 'thursday':
        result = 4
    elif days_week.lower() == 'friday':
        result = 5
    elif days_week.lower() == 'saturday':
        result = 6
    elif days_week.lower() == 'sunday':
        result = 7
    return result

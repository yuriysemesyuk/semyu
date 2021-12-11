from datetime import datetime, time, timedelta, date
from user_page.test_variable import dict_services


"""
    Створення годин
"""
def creat_dicr_time_for_day(date_for_day):
    list_for_time = []
    for i in range(96):
        list_for_time.append(date_for_day)
        date_for_day += timedelta(minutes=15)
    return list_for_time


"""
    Створення сервісу 
"""
def generation_servise_list(servise):
    list_servis = []
    long_servis = servise["time_finish"] - servise["time_start"]
    particles_servis = (long_servis // timedelta(minutes=15))
    for key_servise in servise:
        list_servis.append(servise[key_servise])
    while len(list_servis) != particles_servis:
        if len(list_servis) < particles_servis:
            list_servis.append('-')
        elif len(list_servis) > particles_servis:
            list_servis.pop()
    return list_servis


def generation_servises(dict_services, start_date):
    list_time = creat_dicr_time_for_day(start_date)
    list_for_web = []
    list_for_service = []
    list_line = []
    time_fs = start_date - timedelta(minutes=1)
    for calendar_time in list_time:
        try:
            for service in dict_services[start_date]:
                if calendar_time == service['time_start']:
                    if list_for_service:
                        if list_line:
                            l = generation_servise_list(service)
                            l.insert(0, list_line.copy())
                            list_for_service.append(l)
                        else:
                            list_for_service.append(generation_servise_list(service))
                    else:
                        list_for_service.append(generation_servise_list(service))
                    if time_fs < service['time_finish']:
                        time_fs = service['time_finish']-timedelta(minutes=15)
            if calendar_time >= time_fs:
                if list_for_service:
                    list_for_web.append(list_for_service)
                    list_for_service = []
                    list_line = []
                else:
                    list_for_web.append(calendar_time)
            else:
                list_line.append('-')
        except:
            list_for_web.append(calendar_time)
    return(list_for_web)


"""
    Створення дат ключів з пустими даними ліст
"""
def creat_dict_date(start_date=None, number_of_days=None):
    my_dates = {}
    if not start_date:
        start_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    if not number_of_days:
        number_of_days = 30
    for i in range(number_of_days):
        my_dates[start_date] = generation_servises(dict_services, start_date)
        start_date += timedelta(days=1)
    return my_dates


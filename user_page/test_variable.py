from datetime import time, datetime

translate_days_week = {"Mon":"Пн", "Tue":"Вт", "Wed":"Ср", "Thu":"Чт", "Fri":"Пт", "Sat":"Сб", "Sun":"Нд"}

class User_page:

    user_time_works_standert_start = time(10, 0)
    user_time_works_standert_finish = time(20, 0)



dict_services = {datetime(2021, 12, 12, 0, 0): [{"time_start": datetime(2021, 12, 12, 13, 00),
                                                "name_client": "s---1---",
                                                "name_service": "struzhka",
                                                "time_finish": datetime(2021, 12, 12, 14, 00)},


                                               {"time_start": datetime(2021, 12, 12, 14, 00),
                                                "name_client": "s---2---",
                                                "name_service": "struzhka",
                                                "time_finish": datetime(2021, 12, 12, 14, 45)},


                                               {"time_start": datetime(2021, 12, 12, 17, 30),
                                                "ame_client": "s---4---",
                                                "name_service": "struzhka",
                                                "time_finish": datetime(2021, 12, 12, 18, 45)},


                                               {"time_start": datetime(2021, 12, 12, 15, 00),
                                                "name_client": "s---3---",
                                                "name_service": "struzhka",
                                                "time_finish": datetime(2021, 12, 12, 16, 0)},


                                               {"time_start": datetime(2021, 12, 12, 20, 00),
                                                "name_client": "s---5---",
                                                "name_service": "struzhka",
                                                "time_finish": datetime(2021, 12, 12, 23, 00)}],


                 datetime(2021, 12, 13, 0, 0): [{"time_start": datetime(2021, 12, 13, 13, 0),
                                                "name_client": "s---1---",
                                                "name_service": "struzhka",
                                                "time_finish": datetime(2021, 12, 13, 17, 15)},

                                                {"time_start": datetime(2021, 12, 13, 15, 00),
                                                "name_client": "s---5---",
                                                "name_service": "struzhka",
                                                "time_finish": datetime(2021, 12, 13, 17, 00)}]}


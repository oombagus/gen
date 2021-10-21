import re
import setter as st
from datetime import datetime, timedelta

# listtime = [timedelta(hours=1, minutes=0), timedelta(hours=2, minutes=0)]
# # total = timedelta(hours=0, minutes=0)
# # for i in range(len(list)):
# #     total = total + i
# #     print(total)
# result = sum(listtime, timedelta())
# print(result)

dtime_list = []
totalft = timedelta(hours=0, minutes=0)


def get_flight_time():
    '''Get user input of Flight Time & Ground Time'''
    ftgt = input('FT/GT: ')
    return ftgt


def map_flight_time():
    '''Mapping user input of Flight Time & Ground Time'''
    time = get_flight_time()
    dtime = timedelta(hours=0, minutes=0)
    while time:
        hh = time[0:2]
        mm = time[2:4]
        if time == '':
            return 0
        elif not re.match('^(2[0-3]|[01]?[0-9])$', hh):
            st.wrong()
            time = get_flight_time()
        elif not re.match('^([0-5]?[0-9])$', mm):
            st.wrong()
            time = get_flight_time()
        elif len(time) != 4:
            st.wrong()
            time = get_flight_time()
        else:
            x = time
            t = datetime.strptime(x, '%H%M')
            delta = timedelta(hours=t.hour, minutes=t.minute)
            dtime = dtime + delta
            dtime_list.append(dtime)
            return 1


def total_flight_time():
    get_ft = True
    while get_ft:
        add_ft = map_flight_time()
        if add_ft == 1:
            map_flight_time()
        else:
            get_ft = False
            totalft = sum(dtime_list, timedelta())
            str_totalft = str(totalft).split(':')
            ptotalft = str_totalft[0] + ':' + str_totalft[1]
            st.sgl_line()
            print(f'Total FT & GT: {ptotalft}')
    return totalft


# print(dtime_list)
# total_flight_time()
# print(dtime_list)

import setter as st
from datetime import datetime, timedelta


def getft():
    st.dbl_line()
    print('       Masukkan FT & GT')
    st.dbl_line()
    x = input(f': ').strip().split(',')

    ft = list(map(str, x))
    st.dbl_line()
    # to check ft list
    # print(f'FT list is: {ft}')

    dt = []
    # to check dt list
    # print(f'DT list is: {dt}')

    while len(ft) != 0:

        x = ft[0]
        t = datetime.strptime(x, '%H%M')

        delta = timedelta(hours=t.hour, minutes=t.minute)

        # to check delta value
        # print(delta)

        dt.append(delta)

        ft.pop(0)
        # to check ft list
        # print(f'FT list is: {ft}')
        # to check dt list
        # print(f'DT list: {[str(i) for i in dt]}')

        totalft = timedelta(hours=0, minutes=0)

        for q in dt:
            totalft = totalft + q

    # z = 1

    # for i in dt:
        # to check dt list
        # print(f'FT list: {[str(i)  for i in dt]}')
        # print(f'Time {z}    :  {str(i)}')
        # z = z + 1
        # sum ft list
    # print('====================== +')
    # print(f'Time Total:  {totalft}')
    # print('====================== \n')

    # ttl_str = str(totalft).split(':')
    # print(ttl_str[0] + ':' + ttl_str[1])
    return totalft


getft()

import re
import setter as st
from get_flight_time import get_flight_time, map_flight_time, total_flight_time
from datetime import datetime, timedelta

# -------------------- SEPARATOR --------------------


def fdt_14():
    fdt = timedelta(hours=12, minutes=0)
    return fdt


def fdt_16():
    fdt = timedelta(hours=14, minutes=0)
    return fdt


def fdt_17():
    fdt = timedelta(hours=15, minutes=0)
    return fdt


def fdt_18():
    fdt = timedelta(hours=16, minutes=0)
    return fdt


def fdt_20():
    fdt = timedelta(hours=18, minutes=0)
    return fdt


def fdt_add_0():
    fdt = timedelta(hours=0, minutes=0)
    return fdt


def fdt_add_30m():
    fdt = timedelta(hours=0, minutes=30)
    return fdt

# -------------------- SEPARATOR --------------------


def get_etd():
    '''Get user input of Estimated Time Departure'''
    etd = input('ETD: ')
    return etd


def map_etd():
    '''Mapping user input of Estimated Time Departure'''
    time = get_etd()
    dtime = timedelta(hours=0, minutes=0)
    while time:
        hh = time[0:2]
        mm = time[2:4]
        if not re.match('^(2[0-3]|[01]?[0-9])$', hh):
            st.wrong()
            time = get_etd()
        elif not re.match('^([0-5]?[0-9])$', mm):
            st.wrong()
            time = get_etd()
        elif len(time) != 4:
            st.wrong()
            time = get_etd()
        else:
            x = time
            t = datetime.strptime(x, '%H%M')
            delta = timedelta(hours=t.hour, minutes=t.minute)
            dtime = dtime + delta
            return dtime

# -------------------- SEPARATOR --------------------


def get_user_selection():
    '''Get user input of menu selection'''
    user_input = input('Your selection: ')
    return user_input

# -------------------- SEPARATOR --------------------


def get_flight_crew_fdt():
    waiting_for_input = True
    while waiting_for_input:
        st.dbl_line()
        print('1 - STD 2 Flight Crew')
        print('2 - ENLARGE 3 Pax Seat')
        print('3 - ENLARGE 3 FRFS')
        print('4 - ENLARGE 3 FRFB')
        print('5 - ENLARGE 4 Pax Seat')
        print('6 - ENLARGE 4 FRFS')
        print('7 - ENLARGE 4 FRFB')
        st.dbl_line()
        user_selection = get_user_selection()

        if user_selection == '1':
            return fdt_14()
        elif user_selection == '2':
            return fdt_16()
        elif user_selection == '3':
            return fdt_17()
        elif user_selection == '4':
            return fdt_20()
        elif user_selection == '5':
            return fdt_16()
        elif user_selection == '6':
            return fdt_17()
        elif user_selection == '7':
            return fdt_20()
        else:
            st.wrong_selection()

# -------------------- SEPARATOR --------------------


def get_flight_attendant_fdt():
    waiting_for_input = True
    while waiting_for_input:
        st.dbl_line()
        print(' 1 - Standard Complement')
        print(' 2 - Standard Complement + 1')
        print(' 3 - Standard Complement + 2')
        print(' 4 - CARGO FLIGHT 2 FA')
        print(' 5 - CARGO FLIGHT 3 FA')
        print(' 6 - CARGO FLIGHT 4 FA')
        print(' 7 - CARGO FLIGHT 4 FA (20H)')
        print(' 8 - FREIGHTER FLIGHT 3 FA')
        print(' 9 - FREIGHTER FLIGHT 4 FA')
        print('10 - FREIGHTER FLIGHT 5 FA')
        st.dbl_line()
        user_selection = get_user_selection()

        if user_selection == '1':
            return fdt_14()
        elif user_selection == '2':
            return fdt_16()
        elif user_selection == '3':
            return fdt_18()
        elif user_selection == '4':
            return fdt_14()
        elif user_selection == '5':
            return fdt_16()
        elif user_selection == '6':
            return fdt_18()
        elif user_selection == '7':
            return fdt_20()
        elif user_selection == '8':
            return fdt_14()
        elif user_selection == '9':
            return fdt_16()
        elif user_selection == '10':
            return fdt_18()
        else:
            st.wrong_selection()

# -------------------- SEPARATOR --------------------


def duty_start():
    waiting_for_input = True
    while waiting_for_input:
        st.sgl_line()
        print('1 - Home Base')
        print('2 - Out Base')
        st.sgl_line()
        user_selection = get_user_selection()

        if user_selection == '1':
            return fdt_add_0()
        elif user_selection == '2':
            return fdt_add_30m()
        else:
            st.wrong_selection()

# -------------------- SEPARATOR --------------------


def duty_type():
    waiting_for_input = True
    while waiting_for_input:
        st.sgl_line()
        print('1 - ACT')
        print('2 - XCU')
        st.sgl_line()
        user_selection = get_user_selection()

        if user_selection == '1':
            return fdt_add_0()
        elif user_selection == '2':
            return fdt_add_30m()
        else:
            st.wrong_selection()

# -------------------- SEPARATOR --------------------


def main():
    st.dbl_line()
    print('    LA/LD Generator V.1.0.2    ')
    # -------------------- SEPARATOR --------------------

    st.dbl_line()
    # Report Details
    fltNo = input(str('Flight Number: '))
    stnDep = input(str('Departure Station: '))
    stnArr = input(str('Arrival Station: '))
    # -------------------- SEPARATOR --------------------

    st.dbl_line()
    print('         FLIGHT   CREW       ')
    st.dbl_line()
    print('          Duty  Start')
    fdt_add = duty_start()
    st.dbl_line()
    print('          Duty   Type')
    dutytype = duty_type()
    st.dbl_line()
    etd_fc = map_etd()
    st.dbl_line()
    print('  Please select from the menu  ')
    flight_crew_fdt = get_flight_crew_fdt()
    # -------------------- SEPARATOR --------------------

    st.dbl_line()
    print('       FLIGHT  ATTENDANT       ')
    st.dbl_line()
    etd_fa = map_etd()
    st.dbl_line()
    print('  Please select from the menu  ')
    flight_attendant_fdt = get_flight_attendant_fdt()
    # -------------------- SEPARATOR --------------------

    st.dbl_line()
    print('   Flight Time & Ground Time')
    st.dbl_line()
    total_ft = total_flight_time()
    # -------------------- SEPARATOR --------------------

    # ----------------- LATEST  ARRIVAL -----------------
    flight_crew_latest_arrival = etd_fc + flight_crew_fdt + fdt_add + dutytype

    flight_attendant_latest_arrival = etd_fa + flight_attendant_fdt
    # -------------------- SEPARATOR --------------------

    # ---------------- LATEST  DEPARTURE ----------------
    flight_crew_latest_departure = flight_crew_latest_arrival - total_ft

    flight_attendant_latest_departure = flight_attendant_latest_arrival - total_ft
    # -------------------- SEPARATOR --------------------

    # ------------ Format HH:MM  Flight Crew ------------
    str_fcla = str(flight_crew_latest_arrival).split(':')
    fcla = str_fcla[0] + ':' + str_fcla[1]
    str_fcld = str(flight_crew_latest_departure).split(':')
    fcld = str_fcld[0] + ':' + str_fcld[1]
    # -------------------- SEPARATOR --------------------

    # ---------- Format HH:MM Flight Attendant ----------
    str_fala = str(flight_attendant_latest_arrival).split(':')
    fala = str_fala[0] + ':' + str_fala[1]
    str_fald = str(flight_attendant_latest_departure).split(':')
    fald = str_fald[0] + ':' + str_fald[1]
    # -------------------- SEPARATOR --------------------

    # ------------------ Write FDT.txt ------------------
    file = open("FDT.txt", "w")
    file.write("Dear All Unit Concerned,\n\n")
    file.write(
        f"Berikut kami sampaikan limitasi FDT aircrew *{fltNo} {stnDep}-{stnArr}*.\n\n")
    file.write("*Flight Crew*\n")
    file.write("-------------------------------\n")
    file.write(f"Latest Arrival {stnArr}  : {fcla} UTC\n")
    file.write(f"Latest Departure {stnDep}: {fcld} UTC\n\n")
    file.write("*Flight Attendant*\n")
    file.write("-------------------------------\n")
    file.write(f"Latest Arrival {stnArr}  : {fala} UTC\n")
    file.write(f"Latest Departure {stnDep}: {fald} UTC\n\n")
    file.write("Demikian kami sampaikan. Terima kasih atas perhatiannya.\n\n")
    file.write("Salam,\n\n\n")
    file.write("*JKTOGC*\n*Crew Movement Control*")
    file.close()
    # -------------------- SEPARATOR --------------------

    # ----------------- Print  Template -----------------
    st.dbl_line()
    print('Dear All Unit Concerned,\n')
    print(
        f'Berikut kami sampaikan limitasi FDT aircrew *{fltNo} {stnDep}-{stnArr}*.\n')
    print('*Flight Crew*')
    st.sgl_line()
    print(f'Latest Arrival {stnArr}  : {fcla} UTC')
    print(f'Latest Departure {stnDep}: {fcld} UTC')
    print('\n*Flight Attendant*')
    st.sgl_line()
    print(f'Latest Arrival {stnArr}  : {fala} UTC')
    print(f'Latest Departure {stnDep}: {fald} UTC\n')
    print('Demikian kami sampaikan. Terima kasih atas perhatiannya\n')
    print('Salam,\n\n')
    print('*JKTOGC*\n*Crew Movement Control*')
    st.dbl_line()
    input('    Copy paste dari FDT.txt')

    # main()


if __name__ == '__main__':
    main()

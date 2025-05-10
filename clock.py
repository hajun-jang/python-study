from time import localtime, sleep
from os import system
from keyboard import is_pressed

mod = ''
stopwatch = 0
while True:
    if is_pressed('c'):
        local = localtime()
        wdn = local.tm_wday
        wd = ""
        if wdn == 0:
            wd = "Mon"
        elif wdn == 1:
            wd = "Tue"
        elif wdn == 2:
            wd = "Wed"
        elif wdn == 3:
            wd = "Thu"
        elif wdn == 4:
            wd = "Fri"
        elif wdn == 5:
            wd = "Sat"
        elif wdn == 6:
            wd = "sun"
        print(f"\033[1m{local.tm_hour}:{local.tm_min}\033[0m ({local.tm_sec})\n{local.tm_year}.{local.tm_mon}.{local.tm_mday} ({wd})")
        sleep(0.5)
        system('cls')
    elif is_pressed('s'):
        if is_pressed('r'):
            stopwatch = 0
        stopwatch += 1
        print(f"{stopwatch}s")
        sleep(0.999)
        system('cls')
    elif is_pressed('t'):
        print("We are makeing.") #Not made yet.
        sleep(1)
        system('cls')
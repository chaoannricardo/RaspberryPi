import time as t


if __name__ == '__main__':
    while True:
        year = t.localtime().tm_year
        month = t.localtime().tm_mon
        day = t.localtime().tm_mday
        hour = t.localtime().tm_hour
        minute = t.localtime().tm_min
        sec = t.localtime().tm_sec
        print(year, '-', month, '-', day, '   ', hour, ':', minute, ':', sec, sep="")
        t.sleep(5)

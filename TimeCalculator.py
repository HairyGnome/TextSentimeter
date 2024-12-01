import math

def sec_to_time(sec):
    days = math.floor(sec/86400)
    sec = sec % 86400
    hours = math.floor(sec/3600)
    sec = sec % 3600
    minutes = math.floor(sec/60)
    sec = sec % 60
    return days, hours, minutes, sec
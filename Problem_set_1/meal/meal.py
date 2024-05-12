def main():
    time = input("What time is it? ")
    time_float = convert(time)
    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    if "a.m." in time or "p.m." in time:
        hours_minutes, pm_am = time.split(" ")
        hours, minutes = hours_minutes.split(":")
        if pm_am == "p.m." and int(hours) != 12:
            time_float = int(hours) + 12
    else:
        hours, minutes = time.split(":")
    time_float = float(hours) + (float(minutes)/ 60)

    return time_float



if __name__ == "__main__":
    main()

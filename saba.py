def sam():
    hour = input("enter hour: ")
    rate = input("enter rate: ")
    print("hours: " + hour + "    " + "rate: " + rate + "$")
    hour = int(hour)
    rate = float(rate)

    if hour >= 40:
        print("overtime")
        xel = hour * rate
        xel2 = (hour - 40) * (rate * 0.5)
        xel2 += xel
        month = xel2 * 4
        year = month * 12
        day = (xel2 / 7)
        minute = (rate / 60)
        second = (minute / 60)
        print("second rate: " + str(second) + "$")
        print("minute rate: " + str(minute) + "$")
        print("hour rate: " + str(rate) + "$")
        print("daily rate: " + str(day) + "$")
        print("weekly rate: " + str(xel2) + "$")
        print("monthly rate: " + str(month) + "$")
        print("yearly rate: " + str(year) + "$")
    elif hour < 40:
        print("normal")
        xel = hour * rate
        month = xel * 4
        year = month * 12
        day = (xel / 7)
        minute = (rate / 60)
        second = (minute / 60)
        print("second rate: " + str(second) + "$")
        print("minute rate: " + str(minute) + "$")
        print("hour rate: " + str(rate) + "$")
        print("daily rate: " + str(day) + "$")
        print("weekly rate: " + str(xel) + "$")
        print("monthly rate: " + str(month) + "$")
        print("yearly rate: " + str(year) + "$")
    else:
        print("error")


sam()


def grade():
    gr = input("Enter your grade: {0, 1.0} ")
    print("Enter garde: " + str(gr))
    gr = float(gr)

    if gr >= 0 and gr < 0.6:
        print("F")
    elif gr >= 0.6 and gr < 0.7:
        print("D")
    elif gr >= 0.7 and gr < 0.8:
        print("C")
    elif gr >= 0.8 and gr < 0.9:
        print("B")
    elif gr >= 0.9 and gr < 1.0:
        print("A")
    else:
        print("bad score")


grade()

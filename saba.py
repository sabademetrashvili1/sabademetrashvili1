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
    gra = input("enter grade: ")

    try:
        gra = float(gra)

        if gra < 0:
            print("bad score: " + str(gra))
        elif gra < 0.6:
            print("F: " + str(gra))
        elif gra < 0.7:
            print("D: " + str(gra))
        elif gra < 0.8:
            print("C: " + str(gra))
        elif gra < 0.9:
            print("B: " + str(gra))
        elif gra <= 1.0:
            print("A: " + str(gra))
        elif gra > 1.0:
            print("bad score: " + str(gra))
        else:
            print("bad score: " + str(gra))
    except:
        print("bad score: " + str(gra))



grade()

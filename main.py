import os
import datetime
import time

first_release = 1559260800
second_release = 1679011200
date_gradient = 0.00007515632515632515632515632515632515632515632515632515632
gec_gradient = 13305.6


def gec_calc():
    run = True
    while run:
        os.system("cls")
        print("I am not a fan of the band '100 gecs', however I realised that given\n"
              "their two studio albums names, '1000 gecs' and '10,000 gecs', and their\n"
              "release dates, May 31, 2019 and March 17, 2023, we can work out the rate of\n"
              "gecs over time, as well as the future predicted rate of gecs. Please type 1\n"
              "if you would like to determine the number of gecs at a specific date, or 2\n"
              "if you would like to determine the date of a specific number of gecs.\n"
              "This gec calculator is only an approximation, and cannot be reliably used\n"
              "to predict gecs.")
        choice = input("")
        while choice not in ("1", "2"):
            print("Please select either 1 or 2.")
            choice = input("")
        if choice == "1":
            date = []
            while len(date) != 3:
                os.system("cls")
                print("Please specify the date you would like to determine the gec amount at.")
                print("Please use the form DD.MM.YYYY.")
                date = input("").split(".")
                date_time = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
                unixdate = time.mktime(date_time.timetuple())
                if unixdate > first_release:
                    date_difference = unixdate - first_release
                    gec_difference = date_difference*date_gradient
                    gec_total = gec_difference+1003
                    print(f"On {time.ctime(unixdate)}, the gec amount will be approximately {int(round(gec_total,0))}")
                    while choice not in ("Y", "N"):
                        print("If you would like to return to the menu, type Y. If you would like to quit, type N.")
                        choice = input("")
                    if choice == "N":
                        run = False
                elif unixdate <= first_release:
                    date_difference = first_release - unixdate
                    gec_difference = date_difference * date_gradient
                    gec_total = 1003 - gec_difference
                    print(f"On {time.ctime(unixdate)}, the gec amount will be approximately {int(round(gec_total,0))}.")
                    while choice not in ("Y", "N"):
                        print("If you would like to return to the menu, type Y. If you would like to quit, type N.")
                        choice = input("")
                    if choice == "N":
                        run = False
        elif choice == "2":
            os.system("cls")
            gec = 0
            num = ""
            while not num.isnumeric():
                print("Please specify the amount of gecs you would like to find the approximate date for.")
                num = input("")
            gec = int(num)
            if gec > 1000:
                gec_diffy = gec - 1000
                date_diffy = gec_diffy*gec_gradient
                date_total = date_diffy+first_release
                print(f"At {gec} gecs, the date will be {datetime.datetime.fromtimestamp(date_total).date()}.")
                while choice not in ("Y", "N"):
                    print("If you would like to return to the menu, type Y. If you would like to quit, type N.")
                    choice = input("")
                if choice == "N":
                    run = False
            elif gec <= 1000:
                gec_diffy = 1000 - gec
                date_diffy = gec_diffy * gec_gradient
                date_total = first_release - date_diffy
                print(f"At {gec} gecs, the date will be {datetime.datetime.fromtimestamp(date_total).date()}.")
                while choice not in ("Y", "N"):
                    print("If you would like to return to the menu, type Y. If you would like to quit, type N.")
                    choice = input("")
                if choice == "N":
                    run = False


if __name__ == '__main__':
    gec_calc()

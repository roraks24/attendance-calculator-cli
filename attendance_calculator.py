total = {}
attended = {}

while True:
    print("----OPTIONS----")
    print("1. Enter Subject")
    print("2. Show Attendance Sheet")
    print("3. Check Eligibility")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter subject name: ")
        t = int(input("Enter total classes: "))
        a = int(input("Enter total classes attended: "))

        total[name] = t
        attended[name] = a
        print("Added successfully")

    elif choice == "2":

        if not total:
            print("No subject added!!")
        else:
            sheet = {}
            total_classes = 0
            total_attended = 0

            for name in total:
                t = total[name]
                a = attended[name]

                percentage = (a / t) * 100
                sheet[name] = percentage

                total_classes += t
                total_attended += a

            overall = (total_attended / total_classes) * 100

            print("Subject-wise attendance:", sheet)
            print("Overall attendance:", overall)

    elif choice == "3":

        if not total:
            print("No subject added!!")
        else:
            total_classes = 0
            total_attended = 0

            for name in total:
                total_classes += total[name]
                total_attended += attended[name]

            overall = (total_attended / total_classes) * 100

            if overall >= 75:
                print("You are eligible!!")
            else:
                print("You are not eligible!!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid input")

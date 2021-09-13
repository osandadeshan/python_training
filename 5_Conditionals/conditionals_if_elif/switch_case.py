class SwitchCase:
    def get_weekday(day_number):
        switcher = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        return switcher.get(day_number, "{} is an invalid day of week".format(day_number))

    print(get_weekday(7))
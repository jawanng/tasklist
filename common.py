import datetime
import time
from os import system


class Common:

    @classmethod
    def get_date(cls, intro_message="Date of the task"):
        while 1:
            system('clear')
            print(intro_message)
            task_date_raw = input("Please use DD/MM/YYYY: ")
            task_date_num = task_date_raw.split("/")
            try:
                task_date = datetime.date(year=int(task_date_num[2]),
                                          month=int(task_date_num[1]),
                                          day=int(task_date_num[0]))
            except (ValueError, IndexError) as e:
                print("\n\n{}".format(e))
                time.sleep(3)
            else:
                break
        return task_date

    @classmethod
    def get_minutes(cls):
        while 1:
            system('clear')
            try:
                minutes = int(input("Time spent (rounded minutes) : "))
            except ValueError as e:
                print("\n\n{}".format(e))
                time.sleep(3)
            else:
                if minutes >= 1:
                    return minutes
                else:
                    print("Time spent must be an integer greater than 1\n")
                    time.sleep(3)

    @classmethod
    def main_message(cls):
        system('clear')
        while 1:
            option = input('''
            WORK LOG
            What would you like to do?
            a) Add new entry
            b) Search in existing entries
            c) Quit program
            > ''')
            if option in ('a', 'b', 'c'):
                return option
            else:
                system('clear')
                print("Please enter a, b, or c")

    @classmethod
    def search_menu(cls):
        system('clear')
        while 1:
            option = input('''
            Do you want to search by:
            a) Exact Date
            b) Range of Dates
            c) Duration of Task
            d) Exact Text Search
            e) Regex Pattern
            f) Return to menu
            > ''')
            if option in ('a', 'b', 'c', 'd', 'e', 'f'):
                return option
            else:
                system('clear')
                print("Please enter a, b, c, d, e or f")

    @classmethod
    def print_result(cls, results, entry, total_num):
        system('clear')
        print(results[entry])
        print("\nResult {} of {}\n".format(entry+1, total_num))

    @classmethod
    def print_result_array(cls, results, idx=0):
        total = len(results)
        while 1:
            Common.print_result(results, idx, total)
            if idx == 0 and total > 1:
                option = input("[N]ext, [E]dit, [D]elete, [R]eturn to search menu\n> ").upper()
                if option in ["N", "E", "D", "R"]:
                    return option
            elif idx == 0:
                option = input("[E]dit, [D]elete, [R]eturn to search menu\n> ").upper()
                if option in ["E", "D", "R"]:
                    return option
            elif idx == total - 1:
                option = input("[P]revious, [E]dit, [D]elete, [R]eturn to search menu\n> ").upper()
                if option in ["P", "E", "D", "R"]:
                    return option
            else:
                option = input("[P]revious, [N]ext, [E]dit, [D]elete, [R]eturn to search menu\n> ").upper()
                if option in ["P", "N", "E", "D", "R"]:
                    return option
            print("\nInvalid Entry")

    @classmethod
    def get_date_options(cls, objects):
        many_dates = []
        for itr in objects:
            many_dates.append(itr.date)
        many_dates.sort()
        many_dates = set(many_dates)
        print("Here are the available dates\n{}".format("\n".join(many_dates)))
        time.sleep(4)
        pass

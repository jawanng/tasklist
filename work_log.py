import time
from os import system
from common import Common
from task import Task, TaskList


def search_results():
    tasks = TaskList.get_all_tasks()
    new_option = Common.search_menu()
    if new_option == 'a':
        results = TaskList.search_exact_date(tasks)
    elif new_option == 'b':
        results = TaskList.search_date_range(Common.get_date("What is the date to start with?"),
                                             Common.get_date("What is the ending date of the search?"), tasks)
    elif new_option == 'c':
        results = TaskList.search_duration(Common.get_minutes(), tasks)
    elif new_option == 'd':
        results = TaskList.exact_search(input("What text to search for: "), tasks)
    elif new_option == 'e':
        results = TaskList.regex_search(input("Please enter the regex: "), tasks)
    else:
        results = None
    return results


def search_sequence():
    tasks = TaskList.get_all_tasks()
    idx = 0
    results = search_results()
    if not results:
        system('clear')
        print("No results were found for the criteria specified")
        time.sleep(5)
        return

    while 1:
        option = Common.print_result_array(results, idx)
        if option == "P":
            idx -= 1
        elif option == "N":
            idx += 1
        elif option == "R":
            break
        elif option == "D":
            results[idx].delete_task(tasks)
            break
        elif option == "E":
            results[idx].edit_task(tasks)
            break


if __name__ == "__main__":
    while 1:
        option = Common.main_message()
        if option == 'c':
            system('clear')
            print("Thanks for using the Work Log program!\nHave a great day\n")
            exit()
        elif option == 'a':
            Task.new_entry()
        elif option == 'b':
            search_sequence()

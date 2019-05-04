import datetime
import csv
import re
import os
from os import system
from common import Common


class Task:
    def __init__(self, date, title, task_time, notes):
        self.date = date
        self.title = title
        self.task_time = task_time
        self.notes = notes

    def __str__(self):
        return "Date: {}\nTitle: {}\nTime Spent: {}\nNotes: {}\n".format(self.date, self.title,
                                                                         self.task_time, self.notes)

    @classmethod
    def new_entry(cls):
        date = Common.get_date()
        system('clear')
        title = input("Title of the task: ")
        task_time = Common.get_minutes()
        system('clear')
        notes = input("Notes (Optional, you can leave this empty) : ")
        row = [date, title, task_time, notes]
        with open('tasks.csv', 'a') as fd:
            task_writer = csv.writer(fd, delimiter=',')
            task_writer.writerow(row)
        system('clear')
        input("The entry has been add.  Press enter to return to the menu")
        system('clear')

    def new_entry_task(self):
        with open('tasks.csv', 'a') as fd:
            task_writer = csv.writer(fd, delimiter=',')
            row = [self.date, self.title, self.task_time, self.notes]
            task_writer.writerow(row)

    def __eq__(self, other):
        if (self.title == other.title and self.task_time == other.task_time and
                self.date == other.date and self.notes == other.notes):
            return True
        return False

    def edit_task(self, tasks):
        original = Task(self.date, self.title, self.task_time, self.notes)

        while 1:
            system('clear')
            print("What would you like to edit?")
            option = input("Title, Date, Time, Notes :  ")
            if option.lower() == "title":
                self.title = input("Title of the task: ")
                break
            elif option.lower() == "date":
                self.date = Common.get_date()
                break
            elif option.lower() == "time":
                self.task_time = Common.get_minutes()
                break
            elif option.lower() == "notes":
                self.notes = input("Notes (Optional, you can leave this empty) : ")
                break
            else:
                print("You entered an invalid option")

        os.remove("tasks.csv")
        for itr in tasks:
            if itr == original:
                self.new_entry_task()
            else:
                itr.new_entry_task()

    def delete_task(self, tasks):
        os.remove("tasks.csv")
        for itr in tasks:
            if itr == self:
                pass
            else:
                itr.new_entry_task()


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    @classmethod
    def get_all_tasks(cls):
        holder = TaskList()
        with open('tasks.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                holder.add_task(Task(row[0], row[1], int(row[2]), row[3]))
        return holder.tasks

    @classmethod
    def search_exact_date(cls, tasks):
        Common.get_date_options(tasks)
        main_date = Common.get_date()
        holder = []
        for itr in tasks:
            if itr.date == main_date.isoformat():
                holder.append(itr)
        return holder

    @classmethod
    def search_date_range(cls, begin_date, end_date, tasks):
        holder = []
        for itr in tasks:
            formatted_date = datetime.date.fromisoformat(itr.date)
            if begin_date <= formatted_date <= end_date:
                holder.append(itr)
        return holder

    @classmethod
    def search_duration(cls, duration, tasks):
        holder = []
        for itr in tasks:
            if itr.task_time == duration:
                holder.append(itr)
        return holder

    @classmethod
    def exact_search(cls, text, tasks):
        holder = []
        for itr in tasks:
            if itr.title == text:
                holder.append(itr)
        return holder

    @classmethod
    def regex_search(cls, text, tasks):
        holder = []
        for itr in tasks:
            hold = re.search(text, itr.title, re.IGNORECASE)
            if not hold:
                hold = re.match(text, itr.notes)
            if hold:
                holder.append(itr)
        return holder


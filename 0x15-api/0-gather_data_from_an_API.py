#!/usr/bin/python3
"""
    Uses a REST API to return information about
    TODO list progress from an employee_id.
"""
import requests


def get_to_do_list(employee_id):
    """
    - Accepts integer (employee ID) as parameter.
    Return:
        - Displays on the standard ouput the employee TODO list
            progress in the format:
            Line1: ``Employee EMPLOYEE_NAME is done with
                tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):``
            2nd & N next lines (title of completed tasks):
            TASK_TITLE (1 tabulation and 1 space before the TASK_TITLE)
    """
    employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    todos = requests.get((
        f'https://jsonplaceholder.typicode.com/users'
        f'{employee_id}/todos')).json()

    employee_name = employee['name']
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])

    print('Employee {} is done with tasks({} / {}): '.
          format(employee_name, done_tasks, total_tasks))

    for todo in todos:
        if todo['completed']:
            print('\t{}'.format(todo['title']))

"""_summary_
    """
# import asyncio
import time
from rich.progress import Progress
from mongodb import Mongodb

mongodb = Mongodb()


def advance_city():
    """add 1 to progress of city"""
    mongodb.insert_city()
    return 1


def advance_road():
    """add 1 to progress of road"""
    mongodb.insert_road()
    return 1


def advance_land():
    """add 1 to progress of land"""
    mongodb.insert_land()
    return 1


def run_progress(number_data=200_000):
    """run progress
    """
    with Progress() as progress:
        task1 = progress.add_task("[red]Task One\t", total=number_data)
        task2 = progress.add_task("[green]Task Two\t", total=number_data)
        task3 = progress.add_task("[cyan1]Task Three\t", total=number_data)

        while not progress.finished:
            progress.update(task1, advance=advance_city())
            progress.update(task2, advance=advance_road())
            progress.update(task3, advance=advance_land())
            time.sleep(0.02)


if __name__ == "__main__":
    run_progress()

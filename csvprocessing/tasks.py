from celery import shared_task
import csv

extensions_cols = ['"col10"', ""]

@shared_task
def csv_task(filename):
    """
    Read a csv file
    """
    file_obj = open(filename, "r")
    reader = csv.reader(file_obj)
    total = 0
    for row in reader:
        column = " ".join(row).split(',')[11]
        if(column not in extensions_cols and len(column)>2):
            column = column.replace('"', '')
            float_col = float(column)
            total += float_col
    print(total)
    return total
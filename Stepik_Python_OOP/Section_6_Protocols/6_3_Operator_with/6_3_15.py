from numpy.core.defchararray import lstrip

from Stepik_3_python.csv_module import writer


def log_for(logfile, date_str):
    with (
        open(logfile, 'r', encoding='utf-8') as log,
        open(f"log_for_{date_str}.txt", 'w', encoding='utf-8') as output
    ):
        for line in log:
            if line.startswith(date_str):
                output.write(line.lstrip(f"{date_str} "))


def log_for(logfile, date_str):
    with open(f'log_for_{date_str}.txt', 'w') as result:
        for line in open(logfile):
            if date_str in line:
                date, info = line.split(' ', 1)
                result.write(info)

# with (
#     open('file.txt', encoding='utf-8') as file,
#     open('output.txt', mode='w', encoding='utf-8') as output
# ):
#     for index, line in enumerate(file, 1):
#         output.write(f'{index}. {line}')
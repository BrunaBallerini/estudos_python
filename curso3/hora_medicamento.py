from datetime import datetime, timedelta
from pathlib import Path

from dateutil.relativedelta import relativedelta

date = datetime.now()
delta = relativedelta(days=5)
final_date = date + delta

FILE_PATH = Path().absolute() / 'curso3' / 'hora_medicamento.txt'
print(FILE_PATH)


# print(f'Final date: {final_date}')
medication_time = datetime(2023, 11, 29, 9, 00, 00)
# medication_time = datetime.now()
delta_hour = relativedelta(hours=6)
medication_hour = []

while final_date > date:
    while final_date > medication_time:
        medication_time += delta_hour
        medication_hour.append(medication_time)
    delta_day = relativedelta(days=1)
    date += delta_day
    # print(f'Date: {date}')

for date in medication_hour:
    print(date.strftime('%d-%m-%Y %H:%M:%S'))

with open(FILE_PATH, 'w') as file:
    for date in medication_hour:
        date_str = date.strftime('%d-%m-%Y %H:%M:%S')
        file.writelines(date_str + '\n')

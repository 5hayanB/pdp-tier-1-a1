import csv, random

from faker import Faker

STUDENT_COUNT = 2_000_000
MONTHS = (
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
)
fake = Faker()

if __name__ == '__main__':
    fees_headers = ['student_id', 'amount', 'day', 'month', 'year']
    with open('fees.csv', 'w') as f:
        writer = csv.DictWriter(f, fees_headers)
        writer.writeheader()
        for i in range(STUDENT_COUNT):
            for j in range(len(MONTHS)):
                writer.writerow({
                    'student_id': i,
                    'amount': random.randint(5_000, 10_000),
                    'day': random.randint(1, 30),
                    'month': MONTHS[j],
                    'year': 'Fall 2024'
                })

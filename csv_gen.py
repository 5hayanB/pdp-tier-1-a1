import csv, random

from faker import Faker

STUDENT_COUNT = 10_000_000
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
    # Unique -> id
    student_headers = ['id', 'first_name', 'last_name', 'address', 'grade']
    with open('students.csv', 'w') as f:
        writer = csv.DictWriter(f, student_headers)
        writer.writeheader()
        for i in range(STUDENT_COUNT):
            name = fake.name().split()
            firstname = name[0]
            lastname = name[1]
            writer.writerow({
                'id': i,
                'first_name': firstname,
                'last_name': lastname,
                'address': fake.address(),
                'grade': random.randint(1, 10)
            })
    fees_headers = ['id', 'amount', 'day', 'month', 'year']
    with open('fees.csv', 'w') as f:
        writer = csv.DictWriter(f, fees_headers)
        writer.writeheader()
        for i in range(STUDENT_COUNT):
            for j in range(len(MONTHS)):
                writer.writerow({
                    'id': i,
                    'amount': random.randint(5_000, 10_000),
                    'day': random.randint(1, 30),
                    'month': MONTHS[j],
                    'year': 'Fall 2024'
                })

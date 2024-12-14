import csv, time, \
    multiprocessing as mp

from argparse import ArgumentParser

def parallel_exec(students_csv, fees_csv):
    process_list = [
        mp.Process(target = , args = ())
        for i in range(0, 10, 10)
    ]
    payment_days = [
        None
        for row in fees_csv
    ]
    pass

def linear_exec(students_csv, fees_csv):
    payment_days = []
    for row in fees_csv:
        payment_days.append(row['day'])
    payment_day_counts = {}
    for i in range(1, 31):
        payment_day_counts[str(i)] = 0
    for day in payment_days:
        payment_day_counts[day] += 1
    max = [None, 0]
    for k, v in payment_day_counts.items():
        if max[1] < v:
            max = [k, v]
    return max

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        'students_csv',
        help = 'Path to students.csv'
    )
    parser.add_argument(
        'fees_csv',
        help = 'Path to fees.csv'
    )
    parser.add_argument(
        '--parallel',
        action = 'store_true',
        help = 'Run in parallel mode'
    )
    args = parser.parse_args()
    with open(args.students_csv) as f:
        students_csv = list(csv.DictReader(f))
    with open(args.fees_csv) as f:
        fees_csv = list(csv.DictReader(f))
    t1 = time.time()
    result = parallel_exec(students_csv, fees_csv) if args.parallel \
        else linear_exec(students_csv, fees_csv)
    t2 = time.time()
    print(f'Most consistent payment date of any month: {result[0]}')
    print(f'Execution time: {(t2 - t1) / 60} minutes')

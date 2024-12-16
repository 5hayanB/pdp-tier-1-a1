import csv, time, \
    threading as thr

from argparse import ArgumentParser

def count(start_ndx, end_ndx, count_list, data_list):
    for i in range(start_ndx, end_ndx):
        count_list[int(fees_csv[i]['day']) - 1] += 1

if __name__ == '__main__':
    parser = ArgumentParser()
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
    print('Reading files...')
    with open(args.fees_csv) as f:
        fees_csv = list(csv.DictReader(f))
    print('Files read successfully')
    payment_day_counts = [0 for _ in range(30)]
    print('Executing...')
    t1 = time.time()
    if args.parallel:
        steps = 1_000_000
        thread_list = [
            thr.Thread(
                target = count,
                args = (i, i + steps, payment_day_counts, fees_csv)
            )
            for i in range(0, len(fees_csv), steps)
        ]
        for process in thread_list:
            process.start()
        for process in thread_list:
            process.join()
    else:
        for row in fees_csv:
            payment_day_counts[int(row['day']) - 1] += 1
    t2 = time.time()
    max = [None, 0]
    for i, e in enumerate(payment_day_counts):
        if max[1] < e:
            max = [i + 1, e]
    print(
        'Execution completed successfully\n'
        f'Most consistent payment date of any month: {max[0]}\n'
        f'Execution time: {t2 - t1} seconds\n'
        'Done'
    )

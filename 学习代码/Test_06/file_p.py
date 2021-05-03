import csv


def red(n):
    with open('demo.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for read in reader:
            if read[0] == n:
                return True


def wri(n, t, q):
    with open('demo.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([n, t, q])

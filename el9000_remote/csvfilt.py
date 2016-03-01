import csv

with open('super_energy.csv.bak', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        if int(row[3]) < 9:
            continue
        row[1] = str(int(row[1])*1000 + int(row[2]))
        del row[2]
        print ', '.join(row)

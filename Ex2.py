import csv
from pprint import pprint
def find_total_visits(*file_names):
    total_visits = {}
    for file_name in file_names:
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)

            for row in reader:
                name = row[0]
                visits = [int(cell) for cell in row[1:]]
             
                if name not in total_visits:
                    total_visits[name] = sum(visits)
                else:
                    total_visits[name] += sum(visits)

    return total_visits
def main():
    file_path1 = "C:/Users/f92slpy/techprojects/python-3/files/week-1.csv"
    file_path2 = "C:/Users/f92slpy/techprojects/python-3/files/week-2.csv"
    file_path3 = "C:/Users/f92slpy/techprojects/python-3/files/week-3.csv"
    totals = find_total_visits(file_path1, file_path2, file_path3)
    pprint(totals)

if __name__=='__main__':
    main()

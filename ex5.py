from pprint import pprint

def build_car_list(*file_names):
    for file_name in file_names:
        with open(file_name, 'r') as file:
            content = file.read()
    for file_name1 in file_names:
        with open(file_name1, 'r') as file1:
            content1 = file1.read()
    with open("file3.txt", 'w+') as file2:
        file2.write(content)
        file2.write(content1)
        content2 = file2.read()
    print(content2)

def ex5():
    file_one = "C:/Users/f92slpy/techprojects/python-3/files/car-ids.txt"
    file_two = "C:/Users/f92slpy/techprojects/python-3/files/input.txt"
    car_list = build_car_list(file_one, file_two)
    pprint(car_list)



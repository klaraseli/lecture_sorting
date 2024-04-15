import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as file:
        content = csv.DictReader(file)
        data = {}
        iter = 0
        for row in content:
            for key, value in row.items():
                if iter == 0:
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
            iter = iter + 1
        return data

def selection_sort(list_of_numbers, direction="up"):
    for idx, number in enumerate(list_of_numbers):
        rest = list_of_numbers[idx + 1:]
        minimum = 1000000000000
        maximum = 0
        position = 0
        for n in rest:
            if direction == "up":
                if n < minimum:
                    minimum = n
                    position = rest.index(n) + idx + 1
            if direction == "down":
                if n > maximum:
                    maximum = n
                    position = rest.index(n) + idx + 1
        if minimum < number:
            list_of_numbers[idx], list_of_numbers[position] = list_of_numbers[position], list_of_numbers[idx]
        if maximum > number:
            list_of_numbers[idx], list_of_numbers[position] = list_of_numbers[position], list_of_numbers[idx]
    return list_of_numbers

def bubble_sort(list_of_numbers):
    list_length = len(list_of_numbers)
    for i in range(list_length):
        l = list_of_numbers[:list_length - i]
        for idx, number in enumerate(l):
            if idx < len(l) - 1:
                next_number = l[idx + 1]
                if number > next_number:
                    l[idx], l[idx + 1] = l[idx + 1], l[idx]
        list_of_numbers[:list_length - i] = l
    return list_of_numbers

def insertion_sort(list_of_numbers):
    n = len(list_of_numbers)
    for i in range(1, n):
        key = list_of_numbers[i]
        j = i - 1
        while j >= 0 and list_of_numbers[j] > key:
            list_of_numbers[j + 1] = list_of_numbers[j]
            j = j - 1
        list_of_numbers[j + 1] = key
    return list_of_numbers

def main():
    pass


if __name__ == '__main__':
    data = read_data("numbers.csv")
    print(data)
    # sorted_data = selection_sort(data["series_2"], "up")
    # print(sorted_data)
    # bubble_data = bubble_sort(data["series_1"])
    # print(bubble_data)
    ins_sort = insertion_sort(data["series_3"])
    print(ins_sort)
    main()

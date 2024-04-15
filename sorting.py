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

def selection_sort(list_of_numbers):
    for idx, number in enumerate(list_of_numbers):
        rest = list_of_numbers[idx + 1:]
        minimum = 1000000000000
        position = 0
        for n in rest:
            if n < minimum:
                minimum = n
                position = rest.index(n) + idx + 1
        if minimum < number:
            list_of_numbers[idx], list_of_numbers[position] = list_of_numbers[position], list_of_numbers[idx]
    return list_of_numbers




def main():
    pass


if __name__ == '__main__':
    data = read_data("numbers.csv")
    print(data)
    sorted_data = selection_sort(data["series_3"])
    print(sorted_data)
    main()

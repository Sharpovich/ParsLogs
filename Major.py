"""
Программа принимает файл с логами,
и обрабатывает их регулярным выражением,
с целью парсинга ip-адресов и выводом их количества
в отдельный файл
"""
import re
from collections import Counter
import csv


def reader(filename):
    """
    Функция принимает файл и обрабатывает его регулярным выражением
    :param filename:
    :return: список данных ip-адресов
    """
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with open(filename) as f:
        log = f.read()
        lst = re.findall(regexp, log)
    return lst


def count(lst):
    """
    Коунтер принимает список данных ip-адресов и считает вхождения уникальных
    :param lst:
    :return: словарь данных
    """
    return Counter(lst)


def writeCsv(count):
    """
    Принимает словарь данных и выводит информацию в файл CSV
    :param count:
    :return: file CSV
    """
    with open("output.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP', 'Frequency']
        writer.writerow(header)

        for item in count:
            writer.writerow((item, count[item]))


if __name__ == '__main__':
    writeCsv(count(reader("test.log")))

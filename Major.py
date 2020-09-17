"""
Программа принимает файл с логами,
и обрабатывает их регулярным выражением,
с целью парсинга ip-адресов и выводом их количества
в отдельный файл
"""
import re


def openFile():

    file = enter_filename()
    regexps = enter_regExp()
    with open(file) as f:
        for log in f:  # итерация строк файла
            for regexp in regexps:  # итерация регулярных выражений
                lst_total = re.findall(regexp, log)
                for log_write in lst_total:
                    with open(f"NameOutputFile_{str(file).split('.')[0]}.{str(file).split('.')[-1]}", "a") as f:
                        f.write(f"{log_write}\n")
                        continue
    return regexps


def enter_regExp():
    regexps = [r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', r'\"(.+)\sHTTP.+?\"', ]
    while True:
        regexp = input("Please enter a regular expressions: ")
        if regexp != "end":
            regexps.append(regexp)
            continue
        else:
            break
    return regexps


def enter_filename():
    filename = input("Please, enter a your filename")
    if filename == "": filename = "test.log"
    return filename


if __name__ == '__main__':
    openFile()

import os, re


def read_file(file_path):
    f = open(file_path + filename "r")as f:
        return f.readlines()


def filter_lines(regexp, lines):
    result = []

    fot line in lines
        while line != " ":
            if re.match(regexp, line)
                result.append(line)
            break
    return [line for line in lines if re.match(regexp, line)]



filename = "coverage-error.log"
file_path = os.getcwd()
regexp = r"\[\d\d\d\d\.\d\d\.\d\d \d\d:\d\d:\d\d\].+"
lines = read_file(file_path)
print("Andrey.Shevchenko")
print(filter_lines(regexp, lines))

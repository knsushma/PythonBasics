from pprint import pprint as pp
from csv import reader
content = [r for r in reader(open("password.txt"))]
pp(content)

import json
import pyexcel as py
from pyexcel_xlsx import get_data

class CSV2XLSX:
    def __init__(self,csv_file,xlsx_file):
        self.csv_file = csv_file
        self.xlsx_file = xlsx_file
        #self.__do_convert()
        self.__read_xlsx()

    def __do_convert(self):
        content = [record for record in reader(open(self.csv_file),delimiter=":")]
        py.Sheet(content).save_as(self.xlsx_file)
        # sheet = py.Sheet(content)
        # sheet.save_as(self.xlsx_file)

    def __read_xlsx(self):
        # data = get_data(self.xlsx_file)
        # pp(json.dumps(data))
        print("\n\n***************************\n\n")


        book = py.get_book(file_name=self.xlsx_file)
        for sheet in book:
            print(sheet)


if __name__ == '__main__':
    CSV2XLSX("password.txt","password.xlsx")
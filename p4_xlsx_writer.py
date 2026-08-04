
''' IMPORTING PARSERS AND WRITING DOWN THE DATA TO xlsx FILE'''

import xlsxwriter
import re
import json
import pandas as pd

from p1_Builtin import Builtin_parser
from p2_justjoin_it import justjoin_1_parser
from p3_djinni_parser import djinni_parser
from p4_Dice import Dice_parser
from p5_justjoin_it_2 import justjoin_2_parser

def writer(parser):
    book = xlsxwriter.Workbook(r"C:\Users\user\Desktop\Jobs_Data.xlsx")
    page = book.add_worksheet("Jobs")


    # Headers
    page.write(0, 0, "Name")
    page.write(0, 1, "Source")
    page.write(0, 2, "Years_of_experience")
    page.write(0, 3, "Salary")
    page.write(0, 4, "Work_arrangement")
    page.write(0, 5, "Location")
    page.write(0, 6, "English_level")
    page.write(0, 7, "Skills")
    page.write(0, 8, "Job_url")

    row = 1
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 50)
    page.set_column("E:E", 50)
    page.set_column("F:F", 50)
    page.set_column("G:G", 50)
    page.set_column("H:H", 50)
    page.set_column("I:I", 50)


    for item in parser:  # run every generator
        page.write(row, 0, item[0])
        page.write(row, 1, item[1])
        page.write(row, 2, item[2])
        page.write(row, 3, item[3])
        page.write(row, 4, item[4])
        page.write(row, 5, item[5])
        page.write(row, 6, item[6])
        page.write(row, 7, ", ".join(item[7] or []))
        page.write(row, 8, item[8])

        row += 1

    book.close()

writer(Builtin_parser())


''' FOR MULTIPLE FUNCTIONS AT ONCE'''

# def writer_multiple(parsers):
#
#     book = xlsxwriter.Workbook(r"C:\Users\user\Desktop\Jobs_Data_multiple.xlsx")
#     page = book.add_worksheet("Jobs")
#
#
#     # Headers
#     page.write(0, 0, "Name")
#     page.write(0, 1, "Source")
#     page.write(0, 2, "Years_of_experience")
#     page.write(0, 3, "Salary")
#     page.write(0, 4, "Work_arrangement")
#     page.write(0, 5, "Location")
#     page.write(0, 6, "English_level")
#     page.write(0, 7, "Skills")
#     page.write(0, 8, "Job_url")
#
#     row = 1
#     column = 0
#
#     page.set_column("A:A", 20)
#     page.set_column("B:B", 20)
#     page.set_column("C:C", 20)
#     page.set_column("D:D", 50)
#     page.set_column("E:E", 50)
#     page.set_column("F:F", 50)
#     page.set_column("G:G", 50)
#     page.set_column("H:H", 50)
#     page.set_column("I:I", 50)
#
#     for parser in parsers:  # iterate through all the parser
#         for item in parser():  # run all the  parsers
#             page.write(row, 0, item[0])
#             page.write(row, 1, item[1])
#             page.write(row, 2, item[2])
#             page.write(row, 3, item[3])
#             page.write(row, 4, item[4])
#             page.write(row, 5, item[5])
#             page.write(row, 6, item[6])
#             page.write(row, 7, ", ".join(item[7] or []))
#             page.write(row, 8, item[8])
#
#             row += 1


    # book.close()

# writer_multiple([djinni_parser, justjoin_1_parser, justjoin_2_parser, Builtin_parser])



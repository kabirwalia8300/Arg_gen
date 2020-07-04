import xlrd
import csv
def csv_from_excel():
    wb = xlrd.open_workbook('arguments_data.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('args.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    your_csv_file.close()
csv_from_excel()

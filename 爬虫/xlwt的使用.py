import xlwt

workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet('sheet1')

for i in range(1, 10):
    for j in range(1, i + 1):
        x = '{}*{}={}'.format(i, j, i * j)
        worksheet.write(i, j, x)

workbook.save('student.xls')

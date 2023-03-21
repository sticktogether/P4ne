from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')  # загрузка таблицы в Excel
sheet = wb['Data']  # лист с именем Data в sheet


def getvalue(x):
    return x.value


year = list(map(getvalue, sheet['A'][1:]))       # содержимое колонки A в значение
temp = list(map(getvalue, sheet['C'][1:]))       # содержимое колонки B в значение
activity = list(map(getvalue, sheet['D'][1:]))   # содержимое колонки D в значение

list_x = year
list_y1 = temp
list_y2 = activity

pyplot.plot(list_x, list_y1, label="Метка")
pyplot.xlabel("years")
pyplot.title("Lab1.2", fontsize=20, fontname='Times New Roman')
pyplot.plot(list_x, list_y2, label="Метка")
pyplot.show()

from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

def getvalue(x): return x.value

cell_A = list(map(getvalue, sheet['A'][1:]))
cell_C = list(map(getvalue, sheet['C'][1:]))
cell_D = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(cell_A, cell_C, label="1")
pyplot.plot(cell_A, cell_D, label="2")
pyplot.show()



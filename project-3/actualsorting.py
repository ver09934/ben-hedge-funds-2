import xlsxwriter
import xlrd

#loading in the sorted data for the return data

loc1 = ("/Users/Ben/Documents/Hedge Fund Strategies Sorted.xlsx")

wb = xlrd.open_workbook(loc)
CA = wb.sheet_by_index(0)
DSB = wb.sheet_by_index(1)
EM = wb.sheet_by_index(2)
EMN = wb.sheet_by_index(3)
Event = wb.sheet_by_index(4)
Fixed = wb.sheet_by_index(5)
FoF = wb.sheet_by_index(6)
GM = wb.sheet_by_index(7)
LS = wb.sheet_by_index(8)
MF = wb.sheet_by_index(9)
Multi = wb.sheet_by_index(10)
Options = wb.sheet_by_index(11)
Other = wb.sheet_by_index(12)
Undefined = wb.sheet_by_index(13)

#loading in the original database to pull the ending date data

loc2 = ("/Users/Ben/Documents/All Data")
orig = xlrd.open_workbook(loc2)
data = loc2.sheet_by_index(15)

#creating the new worksheet for the newly sorted data

new = xlsxwriter.Workbook('sortedFINAL.xlsx')
CAliveW = new.add_worksheet('CAliveW')
CAdeadW = new.add_worksheet('CAdeadW')
CAliveWO = new.add_worksheet('CAliveWO')
CAdeadWO = new.add_worksheet('CAdeadWO')
DSBliveW = new.add_worksheet('DSBliveW')
DSBdeadW = new.add_worksheet('DSBdeadW')
DSBliveWO = new.add_worksheet('DSBliveWO')
DSBdeadWO = new.add_worksheet('DSBdeadWO')
EMliveW = new.add_worksheet('EMliveW')
EMdeadW = new.add_worksheet('EMdeadW')
EMliveWO = new.add_worksheet('EMliveWO')
EMdeadWO = new.add_worksheet('EMdeadWO')
EMNliveW = new.add_worksheet('EMNliveW')
EMNdeadW = new.add_worksheet('EMNdeadW')
EMNliveWO = new.add_worksheet('EMNliveWO')
EMNdeadWO = new.add_worksheet('EMNdeadWO')
EventliveW = new.add_worksheet('EventliveW')
EventdeadW = new.add_worksheet('EventdeadW')
EventliveWO = new.add_worksheet('EventliveWO')
EventdeadWO = new.add_worksheet('EventdeadWO')
FixedliveW = new.add_worksheet('FixedliveW')
FixeddeadW = new.add_worksheet('FixeddeadW')
FixedliveWO = new.add_worksheet('FixedliveWO')
FixeddeadWO = new.add_worksheet('FixeddeadWO')
FoFliveW = new.add_worksheet('FoFliveW')
FoFdeadW = new.add_worksheet('FoFdeadW')
FoFliveWO = new.add_worksheet('FoFliveWO')
FoFdeadWO = new.add_worksheet('FoFdeadWO')
GMliveW = new.add_worksheet('GMliveW')
GMdeadW = new.add_worksheet('GMdeadW')
GMliveWO = new.add_worksheet('GMliveWO')
GMdeadWO = new.add_worksheet('GMdeadWO')
LSliveW = new.add_worksheet('LSliveW')
LSdeadW = new.add_worksheet('LSdeadW')
LSliveWO = new.add_worksheet('LSliveWO')
LSdeadWO = new.add_worksheet('LSdeadWO')
MFliveW = new.add_worksheet('MFliveW')
MFdeadW = new.add_worksheet('MFdeadW')
MFliveWO = new.add_worksheet('MFliveWO')
MFdeadWO = new.add_worksheet('MFdeadWO')
MultiliveW = new.add_worksheet('MultiliveW')
MultideadW = new.add_worksheet('MultideadW')
MultiliveWO = new.add_worksheet('MultiliveWO')
MultideadWO = new.add_worksheet('MultideadWO')
OptionsliveW = new.add_worksheet('OptionsliveW')
OptionsdeadW = new.add_worksheet('OptionsdeadW')
OptionsliveWO = new.add_worksheet('OptionsliveWO')
OptionsdeadWO = new.add_worksheet('OptionsdeadWO')
OtherliveW = new.add_worksheet('OtherliveW')
OtherdeadW = new.add_worksheet('OtherdeadW')
OtherliveWO = new.add_worksheet('OtherliveWO')
OtherdeadWO = new.add_worksheet('OtherdeadWO')
UndefinedliveW = new.add_worksheet('UndefinedliveW')
UndefineddeadW = new.add_worksheet('UndefineddeadW')
UndefinedliveWO = new.add_worksheet('UndefinedliveWO')
UndefineddeadWO = new.add_worksheet('UndefineddeadWO')

#creating array of the sheet names in the new array

sheetnames = new.sheet_names()

#creating array of 

#writing in the dates in each sheet

row = 1
column = 0

for item in sheetnames:
    for i in range(CA.nrows):
        item.write(row, column, CA.cell_value(row, column))
        row+=1

#function to find the return data

#checking the end date and the manager investment of each fund (the actual sorting function)

row = 492 #the bottom of each column of return data
column = 1

for i in range(CA.ncols):
    if(CA.cell_value(row, column)!=None)


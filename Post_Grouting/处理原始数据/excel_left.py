import xlwt #只能写不能读
import xlrd #只能读不能写

def wt_xl(xl):
	book = xlwt.Workbook()#新建一个excel
	sheet = book.add_sheet('Left')#添加一个sheet页
	row = 0#控制行
	for stu in xl:
	    col = 0#控制列
	    for s in stu:#再循环里面list的值，每一列
	        sheet.write(row,col,s)
	        col+=1
	    row+=1
	book.save('xl_left.xls')#保存到当前目录下





book = xlrd.open_workbook('pile_detail.xlsx')#打开一个excel
sheet_right = book.sheet_by_index(1)#根据顺序获取sheet
sheet_left = book.sheet_by_name('Left')#根据sheet页名字获取sheet

# print(sheet_left.cell(0,0).value)#指定行和列获取数据


# print(sheet_left.ncols)#获取excel里面有多少列
# print(sheet_left.nrows)#获取excel里面有多少行

# for i in sheet_right.get_rows():
#     print(i)#获取每一行的数据

xl_left = []

for i in range(sheet_left.nrows):#0 1 2 3 4 5
	pile = sheet_left.cell(i,0).value
	pile_detail = sheet_left.row_values(i)
	if sheet_left.cell(i,1).value == 1:
		xl_left.append(pile_detail)
	elif sheet_left.cell(i,1).value == 2:
		for j in range(2):
			newlist = []
			pile_number = pile + '-' + str(j+1)
			newlist.append(pile_number)
			newlist = newlist + pile_detail[1:]
			xl_left.append(newlist)
	elif sheet_left.cell(i,1).value == 4:
		for j in range(2):
			newlist = []
			pile_number = pile + 'A-' + str(j+1)
			newlist.append(pile_number)
			newlist = newlist + pile_detail[1:]
			xl_left.append(newlist)
		for j in range(2):
			newlist = []
			pile_number = pile + 'B-' + str(j+1)
			newlist.append(pile_number)
			newlist = newlist + pile_detail[1:]
			xl_left.append(newlist)
	elif sheet_left.cell(i,1).value == 6:
		for j in range(3):
			newlist = []
			pile_number = pile + 'A-' + str(j+1)
			newlist.append(pile_number)
			newlist = newlist + pile_detail[1:]
			xl_left.append(newlist)
		for j in range(3):
			newlist = []
			pile_number = pile + 'B-' + str(j+1)
			newlist.append(pile_number)
			newlist = newlist + pile_detail[1:]
			xl_left.append(newlist)
	elif sheet_left.cell(i,1).value == 9:
		for j in range(3):
			newlist = []
			pile_number = pile + 'A-' + str(j+1)
			newlist.append(pile_number)
			newlist = newlist + pile_detail[1:]
			xl_left.append(newlist)
		for j in range(3):
			newlist = []
			pile_number = pile + 'B-' + str(j+1)
			newlist.append(pile_number)
			newlist = newlist + pile_detail[1:]
			xl_left.append(newlist)
		for j in range(3):
			newlist = []
			pile_number = pile + 'C-' + str(j+1)
			newlist.append(pile_number)
			newlist = newlist + pile_detail[1:]
			xl_left.append(newlist)


		

wt_xl(xl_left)


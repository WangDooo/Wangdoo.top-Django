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
	book.save('xl_grout.xls')#保存到当前目录下





book = xlrd.open_workbook('grout.xlsx')#打开一个excel
sheet = book.sheet_by_index(0)#根据顺序获取sheet



xl_grout = []

for i in range(sheet.nrows):#0 1 2 3 4 5
	newlist = []
	pile_name = sheet.cell(i,0).value
	dun_name = pile_name.split('—')[0].upper()
	pile_num = pile_name.split('—')[-1]
	name = dun_name+'-'+pile_num
	newlist.append(name)
	newlist = newlist + sheet.row_values(i)[1:]
	xl_grout.append(newlist)

wt_xl(xl_grout)


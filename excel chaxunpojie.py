import xlrd
import xlwt

book=xlwt.Workbook()
st=book.add_sheet("answer")
f=open("answer.txt","w")
excel=xlrd.open_workbook("123.xlsx",encoding_override="utf-8")

all_sheet=excel.sheets()
sheet=all_sheet[1]
i,j=0,0
for each_row in range(sheet.nrows)[2:]:
    for a in sheet.row_values(each_row)[1:20]:
        st.write(i,j,a)
        j+=1
    j=0
    i+=1

book.save("##answer.xls")
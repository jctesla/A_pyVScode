from excelObjModel import ExcelApplication
excelApp = excelObjModel(ActiveInstance = False)
print(excelApp)
excelApp.Visible = True
print(excelApp.Visible)
xlWorkbook = excelApp.Workbooks.Add()
print(xlWorkbook)




#from win32com.client import Dispatch
#zk = Dispatch("zkemkeeper.ZKEM") 
#zk.Connect_Net(IP_address, port)
from openpyxl import load_workbook

class SpreadSheetDriver():
    def __init__(self,spread_sheet_type, file_name,sheet_name):
        self.file_name = file_name
        self.wb = load_workbook(file_name)
        self.ws = self.wb.get_sheet_by_name(sheet_name)

    def save(self):
        self.wb.save(self.file_name)
    def read(self,row,col):
        row = str(row)
        return self.ws[col+row].value

    def write(self,row,col,value):
        row = str(row)
        self.ws[col+row] = value
    def get_row(self,value,col):
        for i in range(1,self.ws.max_row+1):
            if self.read(i,col) == value:
                return i


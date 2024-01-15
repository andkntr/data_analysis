import openpyxl
import pprint


wb = openpyxl.load_workbook('/Users/Ken/Downloads/UD13-19.xlsx')
ws = wb.worksheets[0]

ws.delete_cols(10,3)
ws.delete_cols(11, 5)
ws.delete_cols(12, 2)
ws.delete_cols(13, 6)

ws.column_dimensions['A'].width = 17
ws.column_dimensions['B'].width = 28
ws.column_dimensions['C'].width = 6
ws.column_dimensions['D'].width = 97.33
ws.column_dimensions['E'].width = 4
ws.column_dimensions['F'].width = 5.33
ws.column_dimensions['G'].width = 15
ws.column_dimensions['H'].width = 5.33
ws.column_dimensions['I'].width = 5.83
ws.column_dimensions['J'].width = 7.67
ws.column_dimensions['K'].width = 30

wb.save('/Users/Ken/Downloads/2月13日〜19日【UD】.xlsx')


#参考
#https://reffect.co.jp/python/python-excel#i-10
#https://genchan.net/it/programming/python/3141/
#https://stackoverrun.com/ja/q/10889695

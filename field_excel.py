# -*- coding: utf-8 -*-
import re
import xlrd
import os
import configparser

def excel_field(field_code):
# pattern = re.compile(r'datajson[.?+]')  # 查找数字
# result1 = pattern.findall('datajson["data"]["overviewData"]["saleAmt"]')
# result2 = re.split('\W+','datajson["data"]["overviewData"]["saleAmt"]')
# print (result2[len(result2 )-2])

# cfgfile = os.getcwd() + '\\dbconf.ini'
# config = configparser.ConfigParser()
# config.read(cfgfile, encoding="utf-8-sig")
# list_4 = config.get('sec7', 'Veri_01')
# results = eval(list_4)
# print (results)

    xlsfile = os.getcwd() + '\\Field to check.xlsx'  # 打开指定路径中的xls文件
    book = xlrd.open_workbook(xlsfile)
    sheet0 = book.sheet_by_index(0)
    row_a = sheet0.nrows - 1

    field_list = []
    dict_1 = {}
    # print(row_a)
    # print(sheet0.row_values(1)[0])  # 字段名
    # print(sheet0.row_values(1)[1])  # 字段含义
    for i in range(1,row_a+1):
        #表中所有字段添加到字典
        # field_total = sheet0.row_values(i)[1] + sheet0.row_values(i)[2]+ sheet0.row_values(i)[3]+ sheet0.row_values(i)[4]+ sheet0.row_values(i)[5]
        # dict_1[field_total] = sheet0.row_values(i)[6]

        #形成核查字段
        field_list_1 = ('datajson' + str(sheet0.row_values(i)[1].split()) + str(sheet0.row_values(i)[2].split()) + str(sheet0.row_values(i)[3].split()) + str(sheet0.row_values(i)[4].split()) + str(sheet0.row_values(i)[5].split())).replace('[]','')
        if field_code == sheet0.row_values(i)[0]:
            field_list.append(field_list_1)
        dict_1[field_list_1] = sheet0.row_values(i)[6]
    return field_list,dict_1
    #print (dict_1)
    # if field in dict_1:
    #     return dict_1[field]
    # else:
    #     return u'excel里没有此核查字段'
# print (r)
# print (r[result2[len(result2 )-2]])
# field_code =  'Veri_06'
# print (excel_field(field_code))
class CaseExcel:
    def __init__(self):
        self.app_xlsfile = 'app_auto_case.xlsx'
        self.app_book = xlrd.open_workbook(self.app_xlsfile)#打开文件
        self.app_sheet0 = self.app_book.sheet_by_index(1)#通过索引顺序获取
        self.app_row_n = self.app_sheet0.nrows - 1

    def app_excel_field(self,case_code):
        for row_i in range(0,self.app_row_n):
            if case_code == self.app_sheet0.col_values(0, start_rowx=0, end_rowx=None)[row_i]:#返回由该列中所有单元格的数据组成的列表
                return self.app_sheet0.row_values(row_i, start_colx=0, end_colx=6)#返回由该行中所有单元格的数据组成的列表

    def auto_caselist(self):
        CodeList = self.app_sheet0.col_values(0, start_rowx=1, end_rowx=None)#返回由该列中所有单元格的数据组成的列表
        whether = self.app_sheet0.col_values(6, start_rowx=1, end_rowx=None)#返回由该列中所有单元格的数据组成的列表
        # print (CodeList,"\n",whether)
        autocase_codelist = []
        for list_code in range(0,len(CodeList)):
            CodeList[list_code].replace('jwt_', '')
            if whether[list_code].strip() == 'NA' or whether[list_code].strip() == 'NT':#不要NA用例、NT用例
                autocase_codelist.append(CodeList[list_code])
        # print(CodeList)
        executed_case = [item for item in CodeList if item not in set(autocase_codelist)]
        return executed_case
    def app_case_name(self):
        CodeList1 = self.app_sheet0.col_values(0, start_rowx=1, end_rowx=None)#返回由该列中所有单元格的数据组成的列表

        CodeList2 = self.app_sheet0.col_values(2, start_rowx=1, end_rowx=None)  # 返回由该列中所有单元格的数据组成的列表
        autocase_casename = []
        # print (CodeList1,'\n',CodeList2)
        match_name =  dict(zip(CodeList1, CodeList2))
        # return match_name[case_code]
        return match_name


# a = CaseExcel()
print (CaseExcel().app_case_name()['jwt_04'])
    # app_field_list_operate = []
    # app_field_list_reset = []
    # app_dict_1 = {}
    # for i in range(1, app_row_a + 1):
    #     if app_sheet0.row_values(i)[3] == '':
    #         app_field_list_1 = (app_sheet0.row_values(i)[1] +','+ app_sheet0.row_values(i)[2]).split(',')
    #     elif app_sheet0.row_values(i)[4] == '':
    #          app_field_list_1 = (app_sheet0.row_values(i)[1] +','+ app_sheet0.row_values(i)[2]  +','+  app_sheet0.row_values(i)[3]).split(',')
    #     elif app_sheet0.row_values(i)[5] == '':
    #          app_field_list_1 = (app_sheet0.row_values(i)[1] +','+ app_sheet0.row_values(i)[2]  +','+  app_sheet0.row_values(i)[3]  +','+  app_sheet0.row_values(i)[4]).split(',')
    #     elif app_sheet0.row_values(i)[6] == '':
    #         app_field_list_1 = (app_sheet0.row_values(i)[1] +','+ app_sheet0.row_values(i)[2]  +','+  app_sheet0.row_values(i)[3]  +','+  app_sheet0.row_values(i)[4]  +','+  app_sheet0.row_values(i)[5]).split(',')
    #     else:
    #         app_field_list_1 = (app_sheet0.row_values(i)[1] +','+ app_sheet0.row_values(i)[2]  +','+  app_sheet0.row_values(i)[3]  +','+  app_sheet0.row_values(i)[4]  +','+ app_sheet0.row_values(i)[5]  +','+  app_sheet0.row_values(i)[6]).split(',')
    #
    #     if app_sheet0.row_values(i)[8] == '':
    #         app_field_list_2 = app_sheet0.row_values(i)[7].split()
    #     elif app_sheet0.row_values(i)[9] == '':
    #         app_field_list_2 = (app_sheet0.row_values(i)[7] + ',' + app_sheet0.row_values(i)[8]).split(',')
    #     else:
    #         app_field_list_2 = (app_sheet0.row_values(i)[7] + ',' + app_sheet0.row_values(i)[8] + ',' + app_sheet0.row_values(i)[9]).split(',')
    #
    #     app_field_list_operate.append(app_field_list_1)
    #     app_field_list_reset.append(app_field_list_2)
    #     app_dict_1[app_sheet0.row_values(i)[0]] = app_sheet0.row_values(i)[10]
            #app_field_list_1 = (app_sheet0.row_values(i)[2]+ app_sheet0.row_values(i)[3]+ app_sheet0.row_values(i)[4] + app_sheet0.row_values(i)[5] + app_sheet0.row_values(i)[6]+ app_sheet0.row_values(i)[7])
    # return app_field_list_operate,app_field_list_reset,app_dict_1
    #print (app_field_list[1])
        # if app_field_code == app_sheet0.row_values(i)[0]:
        #     app_field_list.append(app_field_list_1)

    #print (app_field_list)
    #print ('dic',app_dict_1)
# app_field_code =  'Veri_01'

# app_element = app_excel_field()
# app_element_url = app_element[0]
# app_element_end = app_element[1]
# app_element_name = app_element[2]
# print ('url',app_element[0])
# print ('end',app_element[1])
# print ('name',app_element[2])
# app_excel_field('jwt_16')
# -*- coding: utf8 -*-
import csv
import pandas as pd


def get_data(data_path):
    
    # Load the xlsx file
    excel_data = pd.read_excel(data_path)
    # Read the values of the file in the dataframe
    data = pd.DataFrame(excel_data, columns=[
                        'test_case', 'category', 'service', 'title', 'regulation', 'expect_output'])
    data['title'] = data['title'].astype(str)
    data['regulation'] = data['regulation'].astype(str)
    data['expect_output'] = data['expect_output'].astype(str)
    tc_list = data.values.tolist()
 
    return tc_list
    
    # rows = []
    # csv_data = open(str(data_path), "rt")
    # content = csv.reader(csv_data)

    # next(content, None)

    # for row in content:
    #     rows.append(row)
    # print(rows)
    # return rows
    

get_data('data\create_competition.xlsx')
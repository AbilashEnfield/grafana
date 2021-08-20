import pandas as pd


def data_slicer(data):
    rawSplit = data.split("&")
    splited_data_list = []
    for item in rawSplit:
        splited_data = item.split("=")
        splited_data_list.append(splited_data)

    # print(splited_data_list)
    Column_name = []
    Column_value = []
    for each in splited_data_list:
        Column_name.append(each[0])
        Column_value.append(each[1])

    final_data = dict(zip(Column_name, Column_value))

    print(final_data)

    df = pd.DataFrame(data=final_data, index=[0])

    df = df.T

    # print(df)

    # df.to_excel('dict1.xlsx')

    return final_data

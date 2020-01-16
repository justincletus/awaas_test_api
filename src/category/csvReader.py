from django.shortcuts import render
import pandas as pd
import stringcase

def csvReader(csv_file):
    # data = pd.read_csv(csv_file, nrows=1).columns
    data = pd.read_csv(csv_file)
    return data

    # data_list = pd.DataFrame(data)
    # print(data_list.head())

def main():
    file = '~/Documents/SmartUniversity/course_category_data.csv'
    return csvReader(file)


if __name__ == '__main__':
    main()

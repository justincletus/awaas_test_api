import csv, io
from django.templatetags.static import static
from django.core.exceptions import ValidationError
from .models import State

def csvReader():
    csv_content = open('/Users/justincletus/djangoDev/smartuniv/src/static/other_files/india-state-city-urban.csv', 'r')
    if not csv_content.name.endswith('.csv'):
        raise ValidationError('Invalid file type')

    # with open(, 'r') as csvfile:
    #     try:
    #         csvreader = csv.reader(csvfile)
    #         for row in csvreader:
    #             print(row, '\n')
    #
    #     except csv.Error:
    #         raise ValidationError('failed to parse csv file.')

    try:
        csvdata = csv.reader(csv_content)
        queryset = State.objects.all()
        for res in queryset:
            print(res, '\n')

        for row in csvdata:
            sql_format = 'insert into country_city(city_name, state_id) values(', row[0] ,')'
            # print(sql_format)
    except csv.Error:
        raise ValidationError('failed to read the file')

csvReader()
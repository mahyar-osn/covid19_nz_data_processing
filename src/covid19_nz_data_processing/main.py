import os

from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import requests
import wget

import pandas as pd


class FindExcelFile(object):

    def __init__(self):
        self._parent_url = "https://www.health.govt.nz/"
        self._cases_url = self._parent_url + \
                        "our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases/covid-19-current-cases-details"
        url_reader = urlopen(self._cases_url)
        try:
            html = url_reader.read().decode('utf-8')
        finally:
            url_reader.close()

        self._response = requests.get(self._cases_url)
        self._soup = BeautifulSoup(self._response.content, 'html.parser', parse_only=SoupStrainer('a'))

    def fetch_file(self):
        for link in self._soup:
            if link.has_attr('href'):
                if '.xlsx' in link['href']:
                    data_file = self._parent_url + link['href']
                    # wget.download(data_file)
                    return data_file
        raise FileNotFoundError("Excel file was not found on the MoH website!")


class DataCollector(object):

    def __init__(self, *args):
        self._excel_file = None

        if args:
            self._excel_file = args[0]
        else:
            self._initialize()

        self._confirmed_sheet = None
        self._probable_sheet = None

        self._confirmed_total = None
        self._probable_total = None

        self._combined_sum = None

    def _initialize(self):
        fef = FindExcelFile()
        self._excel_file = fef.fetch_file()

    def parse_confirmed(self):
        self._confirmed_sheet = pd.read_excel(self._excel_file,
                                              sheet_name='Confirmed',
                                              header=1,
                                              skiprows=range(1, 3))

        return self._confirmed_sheet

    def parse_probable(self):
        self._probable_sheet = pd.read_excel(self._excel_file,
                                             sheet_name='Probable',
                                             header=1,
                                             skiprows=range(1, 3))
        return self._probable_sheet

    @staticmethod
    def _get_daily_sum(sheet, col):
        total_num = sheet['Date of report'].map(sheet.groupby('Date of report').size())
        total = pd.concat([sheet['Date of report'], total_num], axis=1).drop_duplicates()
        total.columns = ['Date of report', col]
        total.set_index('Date of report', inplace=True)
        total.index = pd.to_datetime(total.index)
        return total

    def get_daily_sum_confirmed(self):
        self._confirmed_total = self._get_daily_sum(self._confirmed_sheet, 'Daily total of confirmed')

    def get_daily_sum_probable(self):
        self._probable_total = self._get_daily_sum(self._confirmed_sheet, 'Daily total of probable')

    def generate_combined_sum(self):
        self._combined_sum = pd.DataFrame()
        for df in [self._confirmed_total, self._probable_total]:
            self._combined_sum = self._combined_sum.combine_first(df)


if __name__ == '__main__':

    # f = FindExcelFile()
    # f.fetch_file()

    # filename = '../../resources/covid-19-case-details-update-4-april-2020.xlsx'
    excel_file = DataCollector()
    confirmed = excel_file.parse_confirmed()
    probable = excel_file.parse_probable()

    print('done')

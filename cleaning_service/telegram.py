import numpy as np
import re
import pandas as pd


def clean_adress(df: pd.DataFrame):
    '''Считывает эксель, возвращает нормальные адресса tg'''
    df['tg_adress'] = df['Тelegram-канал'].apply(clean)
    series = df[df['tg_adress'].notnull()]['tg_adress']
    return list(series)


def clean(row):
    '''Функция приводит в порядок адреса(как записаны в xlsx - не читаются)
    '''
    if pd.isnull(row) or row == 0:
        return np.nan
    try:
        adress = re.findall(r'\w+', row)[-1]
        adress = '@' + adress
        return adress
    except Exception as e:
        return e 
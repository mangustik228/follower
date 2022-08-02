from dotenv import load_dotenv
import os
import pandas as pd
import cleaning_service
from parsers import tiktok, telegram

file_path = 'example.xlsx'


# Что парсить, а что не надо
PAGE_FOR_PARSING = {
    'tiktok': True,
    'telegram': True,
}


# Подгружаем переменные окружения
dotenv_path = os.path.join('dot.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

SESSION_NAME = os.environ['TELEGRAM_SESSION_NAME']
API_HASH = os.environ['TELEGRAM_API_HASH']
API_ID = os.environ['TELEGRAM_API_ID']


# Основная таблица
df = pd.read_excel(file_path)

# Парсим тикток
if PAGE_FOR_PARSING.get('tiktok'):
    tiktok_adress = list(df[df['ТикТок'].notnull()]['ТикТок']) # Забираем массив url
    pars_tiktok = tiktok.parsing(tiktok_adress) # Парсер
    df = df.merge(pars_tiktok,on='ТикТок', how='left') # Вносим в таблицу

# Парсим телеграмм
if PAGE_FOR_PARSING.get('telegram'):
    telegram_adress = cleaning_service.telegram.clean_adress(df)
    pars_telegram = telegram.parsing(telegram_adress, SESSION_NAME, API_HASH, API_ID)
    df = df.merge(pars_telegram, on='tg_adress', how='left')

# Записываем в файл.
df.to_csv('data.csv', index=False, sep='\n')
with pd.ExcelWriter('data.xlsx') as writer:
    df.to_excel(writer)

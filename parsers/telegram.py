from telethon import TelegramClient, sync
from telethon.tl.functions.channels import GetFullChannelRequest
import re, time
import pandas as pd
from tqdm import tqdm



def parsing(adresses, session_name, api_hash, api_id):
    ''' Парсит подписчиков телеграмма, если сессия еще не создана, 
        то запросит телефон и пришлет сообщение с кодом в телеграмм
        
        adresses [list]    : список адресов, которые надо спарсить, в формате @example
        session_name [str] : произвольное название сессии, создастся одноименный файл, который надо добавить в .gitignore
        api_hash [str]     : получаем на сайт https://core.telegram.org/
        api_id [str]       : также получаем на сайте телеграмма, при регистрации приложения
        
    '''
    pattern = r'participants_count=\d+'
    data = []
    with TelegramClient(session_name, api_id, api_hash) as client:
        for adress in tqdm(adresses[:3], desc='telegram'):
            try:
                ch = client.get_entity(adress)
                ch_full = client(GetFullChannelRequest(channel=ch))
                info = str(ch_full.full_chat) # Получаю инфо и преобразую к строке
                participants = re.search(pattern,info)[0]
                participants = participants.split('=')[1] 
                data.append([adress, int(participants)])
            except Exception as e:
                with open('logs.txt', 'w') as log:
                    log.write(e)
                data.append([adress, None])
            finally:
                time.sleep(1)
    df = pd.DataFrame(columns=['tg_adress', 'tg_participants'], data=data)
    return df
      
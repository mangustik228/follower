### Общая информация

---

### Парсинг телеграмм. Создание сессии
- Зарегистрировать приложение в (телеграмм)[https://my.telegram.org/apps]
- Создать файл dot.env в котором прописать полученные id и hash, а также произвольное имя создаваемой сессии:
```bash
API_ID = xxxxxxx 
API_HASH = xxxxxxxx
SESSION_NAME = 'example_name' 
```
- Если все ок, запросит телефон, затем пришлет сообщение в телеграмм
- После выполнения скрипта создаться файл с сессией `example_name.session`
- Файлы `dot.env` & `example_name.session` обязательно добавить в .gitignore
---



### Парсинг подписчиков тик-ток

```bash 
pip install playwright
pip install tqdm
pip install pandas
```

После установки библиотек необходимо установить "браузер"
```bash
playwright install
```
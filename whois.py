import requests
from datetime import datetime
from bs4 import BeautifulSoup
from models import Registrant, WhoIsModel

def extract_whois_model(domain_name: str):
    whois_url = 'https://www.ps.kz/domains/whois/result?q='

    content = requests.get(whois_url + domain_name).content

    soup = BeautifulSoup(content, 'html.parser')
    soup = soup.table

    fields = {}

    for tr in soup.find_all('tr'):
        key, value = tr.text.split(":", 1)
        fields[key.strip()] = value.strip()

    registrant = None if not fields.get("Регистрант") else extract_registrant(fields.get("Регистрант"))

    whois_model = WhoIsModel(
        domain=fields.get("Доменное имя"),
        status=fields.get("Статус").replace("\n", ", "),
        registrator=fields.get("Регистратор"),
        registrant=registrant,
        server_names=fields.get("Серверы имен").replace("\n", " "),
        created_date=extract_datetime(fields.get("Создан")),
        last_modified_date=extract_datetime(fields.get("Последнее изменение")),
        expiration_date=extract_datetime(fields.get("Дата окончания"))
    )

    return {"data": whois_model.to_dict()}

def extract_registrant(data: str):
    fields = {}
    lines = data.splitlines()

    for line in lines:
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()

    registrant = Registrant(
        contact_id=fields.get("ID Контакта"),
        name=fields.get("Имя"),
        organization=fields.get("Организация"),
        address=fields.get("Адрес"),
        city=fields.get("Город"),
        region=fields.get("Область"),
        postal_code=fields.get("Почтовый индекс"),
        country=fields.get("Страна"),
        phone=fields.get("Телефон"),
        fax=fields.get("Факс"),
        email=fields.get("Email")
    )
    return registrant

def extract_datetime(date_str):
    date_only_str = date_str.split('T')[0]
    return datetime.strptime(date_only_str, '%Y-%m-%d')
import json
class Registrant:
    def __init__(self, contact_id, name, organization, address, city, region, postal_code, country, phone, fax, email):
        self.contact_id = contact_id
        self.name = name
        self.organization = organization
        self.address = address
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.fax = fax
        self.email = email

    def to_dict(self):
        return {
            'contact_id': self.contact_id,
            'name': self.name,
            'organization': self.organization,
            'address': self.address,
            'city': self.city,
            'region': self.region,
            'postal_code': self.postal_code,
            'country': self.country,
            'phone': self.phone,
            'fax': self.fax,
            'email': self.email,
        }

    def __str__(self):
        return f"ID Контакта: {self.contact_id}\n" \
               f"Имя: {self.name}\n" \
               f"Организация: {self.organization}\n" \
               f"Адрес: {self.address}\n" \
               f"Город: {self.city}\n" \
               f"Область: {self.region}\n" \
               f"Почтовый индекс: {self.postal_code}\n" \
               f"Страна: {self.country}\n" \
               f"Телефон: {self.phone}\n" \
               f"Факс: {self.fax}\n" \
               f"Email: {self.email}"

class WhoIsModel:
    def __init__(self, domain, status, registrator, registrant: Registrant,
                 server_names, created_date, last_modified_date, expiration_date):
        self.domain = domain
        self.status = status
        self.registrator = registrator
        self.registrant = registrant
        self.server_names = server_names
        self.created_date = created_date
        self.last_modified_date = last_modified_date
        self.expiration_date = expiration_date


    def to_dict(self):
        return {
            'domain': self.domain,
            'status': self.status,
            'registrator': self.registrator,
            'registrant': None if not self.registrant else self.registrant.to_dict(),
            'server_names': self.server_names,
            'created_date': self.created_date.isoformat() if self.created_date else None,
            'last_modified_date': self.last_modified_date.isoformat() if self.last_modified_date else None,
            'expiration_date': self.expiration_date.isoformat() if self.expiration_date else None
        }

    def __str__(self):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

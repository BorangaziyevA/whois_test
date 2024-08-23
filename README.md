# WHOIS Lookup API - Тестовое задание

Этот проект представляет собой тестовое задание, включающее реализацию простого веб-приложения на Flask для выполнения WHOIS-запросов и сохранения результатов в базу данных.

## Стек технологий

- Python 3.9
- Flask
- MongoDB
- Docker

## Запуск приложения через Docker

```markdown
docker build -t whois_test_app .

docker run -d -p 5001:5001 whois_test_app

import re

from flask import Flask, request, jsonify

import whois

import database

app = Flask(__name__)

@app.route("/lookup_whois", methods=["GET"])
def lookup_whois():
  domain_name = request.args.get("domain_name")

  if not domain_name:
    return jsonify({"error": "Domain name is required"}), 400

  if not is_valid_domain(domain_name):
    return jsonify({"error": "Domain name is incorrect"}), 400

  try:
    result_data = whois.extract_whois_model(domain_name).to_dict()
    ##Сохранение в базу данных
    database.insert_to_db(result_data.copy())
    return jsonify(result_data), 200

  except Exception as e:
      return jsonify({"error": str(e)}), 500

## Валидация для проверки правильности домена
def is_valid_domain(domain_name):
  pattern = r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
  return re.match(pattern, domain_name) is not None

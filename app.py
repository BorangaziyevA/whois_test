import re
import logging
from flask import Flask, request, jsonify
import whois
import database

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route("/lookup_whois", methods=["GET"])
def lookup_whois():
    domain_name = request.args.get("domain_name")

    logging.info(f"Validation of {domain_name} started")
    if not domain_name:
        return jsonify({"error": "Domain name is required"}), 400

    if not is_valid_domain(domain_name):
        return jsonify({"error": "Domain name is incorrect"}), 400

    logging.info(f"Validation of {domain_name} successfully passed")


    try:
        logging.info(f"Extracting information about {domain_name}")
        result_data = whois.extract_whois_model(domain_name)
        logging.info(f"Extracted successfully. {result_data} ")

        # Сохранение в базу данных
        logging.info(f"Inserting information about {domain_name} into the database")
        database.insert_to_db(result_data.get("data").copy())

        logging.info(f"Information about {domain_name} successfully saved into the database")
        return jsonify(result_data), 200

    except Exception as e:
        logging.error(f"Error with {domain_name} - {str(e)}")
        return "Sorry, we're having technical issues.", 500


# Валидация для проверки правильности домена
def is_valid_domain(domain_name):
    pattern = r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, domain_name) is not None


if __name__ == "__main__":
    app.run(debug=True)

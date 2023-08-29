from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from get_external_link import check_status_codes,find_external_links
from get_language_type import selectFunction
from compliance_of_disclosure import all_process
from readability import calculate_readability
# from timeline import getFrequency


app = Flask(__name__)
CORS(app)  # This allows all origins; you can configure it for your specific needs


@app.route('/completeness', methods=['POST'])
def get_url():
    data = request.get_json()
    url = data.get('url')
    results = json.dumps(all_process(url))
    return results

@app.route('/readability', methods=['POST'])
def get_url_readability():
    data = request.get_json()
    url = data.get('url')
    results = json.dumps(calculate_readability(url))
    return {"result": results}

@app.route('/availability', methods=['POST'])
def get_url_availability():
    data = request.get_json()
    url = data.get('url')
    results = json.dumps(selectFunction(url))
    external_links = find_external_links(url)
    status_codes = check_status_codes(external_links)
    link_result = []
    for link, status_code in status_codes.items():
        link_result.append({"Link": link, "Status Code": status_code})
    return {"result": results + json.dumps(link_result)}


# @app.route('/timeliness', methods=['POST'])
# def get_url_timeliness():
#     data = request.get_json()
#     url = data.get('url')
#     results = json.dumps(getFrequency(url))
#     return {"result": results}


if __name__ == '__main__':
    app.run()

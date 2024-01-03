from flask import Flask, request, jsonify
import requests

from flask_cors import CORS
import json
from threading import Thread

from get_external_link import check_status_codes, find_external_links
from get_language_type import selectFunction
from compliance_of_disclosure import all_process
from readability import calculate_readability
from timeline import getFrequency


app = Flask(__name__)
CORS(app)  # This allows all origins; you can configure it for your specific needs

results_dict = {}

def background_task(url, task_type):
    if task_type == 'availability':
        languages = json.dumps(selectFunction(url))
        external_links = find_external_links(url)
        status_codes = check_status_codes(external_links)
        link_result = [{"link": link, "statusCode": status_code} for link, status_code in status_codes.items()]
        results = {
            "languages": languages,
            "externalLinks": link_result
        }
        print('availability job done')
        results_dict['availability'] = results

    elif task_type == 'timeliness':
        results = json.dumps(getFrequency(url))
        print('timeliness job done')
        results_dict['timeliness'] = results

@app.route('/completeness', methods=['POST'])
def get_url():
    data = request.get_json()
    url = data.get('url')
    results = json.dumps(all_process(url))
    return {"result": results}


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
    Thread(target=background_task, args=(url, 'availability')).start()
    return {"availability status": "processing"}
    # languages = json.dumps(selectFunction(url))
    # external_links = find_external_links(url)
    # status_codes = check_status_codes(external_links)
    # link_result = []
    # for link, status_code in status_codes.items():
    #     link_result.append({"link": link, "statusCode": status_code})
    # results = {
    #     "languages": languages,
    #     "externalLinks": link_result
    # }

    return {"result": json.dumps(results)}
    # return {"result": results + json.dumps(link_result)}

@app.route('/timeliness', methods=['POST'])
def get_url_timeliness():
    data = request.get_json()
    url = data.get('url')
    # Start the background task
    Thread(target=background_task, args=(url, 'timeliness')).start()
    return {"timeliness status": "processing"}

    # # results = json.dumps(getFrequency(url))
    # results = requests.post(
    #     'https://34.28.198.83:8000/timeliness', json=data, verify=False)
    # print('response from server:', results.text)
    # res = results.json()
    # return {"result": res}

@app.route('/timelinessori', methods=['POST'])
def get_timeliness():
    data = request.get_json()
    url = data.get('url')
    results = json.dumps(getFrequency(url))
    return {"result": results}

@app.route('/getResult', methods=['POST'])
def get_result():
    data = request.get_json()
    type = data.get('type')
    if type in results_dict:
        return {"result": results_dict[type]}
    else:
        return {"status": "pending"}

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000)
    app.run()

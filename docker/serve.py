from flask import Flask, jsonify, request
import json
import os
import sys

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

print('----load /opt/ml/model/ data')
with open('/opt/ml/model/result.txt') as f:
    l = f.readlines()
    print(l)
    my_text = l[0]

@app.route('/ping')
def ping_request():
    return 'OK'


@app.route("/invocations", methods=['POST'])
def predict():
    post_data = request.json['data']
    return jsonify({'result': my_text, 'post_data': post_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

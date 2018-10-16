import json
import os
import sys

print('----/opt/ml/')
files = os.listdir('/opt/ml/')
for file in files:
    print(file)

print('----/opt/ml/input/')
files = os.listdir('/opt/ml/input/')
for file in files:
    print(file)

print('----/opt/ml/input/data/')
files = os.listdir('/opt/ml/input/data/')
for file in files:
    print(file)

print('----see train data')
with open('/opt/ml/input/data/train/train.txt') as f:
    lines = f.readlines()
print(lines)

print('----see test data')
with open('/opt/ml/input/data/test/test.txt') as f:
    lines = f.readlines()
print(lines)

print('----/opt/ml/input/config/')
files = os.listdir('/opt/ml/input/config/')
for file in files:
    print(file)

print('----see hyperparameters data')
with open('/opt/ml/input/config/hyperparameters.json') as f:
    data = json.load(f)
print(data)

print('----see resourceconfig data')
with open('/opt/ml/input/config/resourceconfig.json') as f:
    data = json.load(f)
print(data)

path_w = '/opt/ml/model/result.txt'
s = 'output as model'
with open(path_w, mode='w') as f:
    f.write(s)

sys.exit(0)

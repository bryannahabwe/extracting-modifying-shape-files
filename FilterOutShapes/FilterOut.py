import itertools
import json
import pprint

with open('parishes.json') as f:
    data = json.load(f)

features = []
for k, v in itertools.groupby([x for x in data['features'] if x['properties']['DNAME_2010'] == 'GULU']):  # filter out city2
    features.append(k)
data['features'] = features
pprint.pprint(data)

with open('gulu_parishes.geojson', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

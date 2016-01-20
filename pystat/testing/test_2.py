from pyjstat import pyjstat
from collections import OrderedDict
import urllib2
import json

dataset_url_1 = 'http://www.cso.ie/StatbankServices/StatbankServices.svc/jsonservice/responseinstance/CDD01'

population_json_data = json.load(urllib2.urlopen(dataset_url_1),
                      object_pairs_hook=OrderedDict)
population_results = pyjstat.from_json_stat(population_json_data, naming="id")

population_dataset = population_results[0]

population_data = population_dataset[population_dataset['ContentsCode'] ==
                  'Folketallet11']
population_data.head()

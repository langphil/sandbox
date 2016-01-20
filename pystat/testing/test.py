from pyjstat import pyjstat
import requests
from collections import OrderedDict

EXAMPLE_URL = 'http://www.cso.ie/StatbankServices/StatbankServices.svc/jsonservice/responseinstance/CDD01'

data = requests.get(EXAMPLE_URL)
results = pyjstat.from_json_stat(data.json(object_pairs_hook=OrderedDict))
print (results)

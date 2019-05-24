# parse json file to retrieve qm & download individual results to iwwb-qm/
# 2019-05-13 by maximilian

import urllib.request
from datetime import datetime
import json
import time

pathJson = 'iwwb-source.json'
pathFolder = 'iwwb-qm/'

json_file = open(pathJson, 'r')
json_file_content = json_file.read()
json_arrays = json.loads(json_file_content)

for quali in json_arrays['qm']:
	myFilenameDate = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	myQmTitle = str(quali['qmTitel'])
	myFilename = myFilenameDate + '_' + myQmTitle + '.html'
	myDownloadPath = pathFolder + myFilename

	myUrl = quali['qmQuelle']
	print(myUrl, myDownloadPath)
	time.sleep(1)

	try:
		urllib.request.urlretrieve(myUrl, myDownloadPath)
	except Exception:
		print ('error', myUrl)

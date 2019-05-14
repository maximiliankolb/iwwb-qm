# search files in iwwb/ for keywords
# 2019-05-13 by maximilian

import os

keywords = ['Digitalisierung', 'Datenschutz', 'DSGVO', 'BWL', 'Finanz', 'Personal', 'EDV', 'Software', 'Betriebsrat', 'Betriebsräte', 'Arbeit 4.0', 'Industrie 4.0', 'Geschäftsführer', 'Führungskraft', 'Führungskräfte', 'Fachkraft', 'Fachkräfte']

pathFolder = 'iwwb/'

for fileName in os.listdir(pathFolder):
	for keyword in keywords:
		i = 0
		fileHtml = pathFolder + fileName
		searchfile = open(fileHtml, "r", encoding = "ISO8859-1")

		for line in searchfile:
			if keyword.casefold() in line.casefold():
			# casefold to ignore upper and lower case
				i = i+1
		if i >= 5:
			beautifulOutput = fileHtml + '|' + keyword + '|' + str(i)
			print(beautifulOutput[25:])
		else:
			continue
		searchfile.close()

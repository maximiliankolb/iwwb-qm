# search files in iwwb/ for keywords
# 2019-05-13 by maximilian

import os

keywords = ['Geschäftsführung', 'Geschäftsführer', 'Chef', 'Vorstand', 'Führungskraft', 'Führungskräfte', 'Geschäftsleitung', 'Unternehmen', 'Fachkraft', 'Fachkräfte', 'Facharbeiter', 'Mitarbeiter', 'Personal', 'Berufstätige', 'Betriebsrat', 'Betriebsräte', 'Mitbestimmung', 'Gewerkschaft', 'BWL', 'Finanz', 'Ökonomie', 'Pflege', 'Gesundheit', 'Krankenhaus', 'Digitalisierung', 'Industrie 4.0', 'Arbeit 4.0', 'Arbeiten 4.0', 'agil', 'EDV', 'Software', 'Office', 'Datenschutz', 'DSGVO', 'Patientendaten']

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

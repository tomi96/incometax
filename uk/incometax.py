import requests, bs4
res = requests.get('https://www.gov.uk/income-tax-rates/current-rates-and-allowances')
res.raise_for_status()
playFile = open('IncomeTax.html', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

exampleFile = open('IncomeTax.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")
elems = exampleSoup.select('table')
tab = elems[0].getText()
tab.raise_for_status()
playFile1 = open('IncomeTaxTable.html', 'wb')
for chunk in tab.iter_content(100000):
    playFile1.write(chunk)
playFile1.close()

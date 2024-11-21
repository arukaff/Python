import requests
from lxml import html
import csv

resp = requests.get(url='https://technical.city/ru/video/rating', headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
})
def get_cell_text(cells):
    ls=[]
    for s in cells:
        s=s.strip()
        if len(s)>0:
            ls.append(s)
    return ls

if resp.status_code == 200 :
    dom = html.fromstring(resp.text)
    data_rows=[]    
    try:
        data_header=dom.xpath("//th/div/div[1]/text()")
        rows=dom.xpath("//tr[contains(@id,'itemrow')]")
        for row in rows:
            cells=row.xpath(".//td//text()") # cells=row.xpath(".//td/text() | .//td/i/span/text() | .//td/a/text()")
            # a=list(map(lambda s: s.strip(),cells))
            data_rows.append(get_cell_text(cells))
    except Exception as e:
        print(e)
        
    with open('DZ4.csv', 'w',encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerow(data_header)
        write.writerows(data_rows)
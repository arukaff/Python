import requests
import wget
# from lxml import html
# from fake_useragent import UserAgent
# ua=UserAgent()

# srt=ua.getRandom
# print(srt['useragent'])
# resp = requests.get(url='https://unsplash.com', headers = {'User-Agent':srt['useragent']})
# print(resp.status_code)
# tree = html.fromstring(html=resp.content)

# movies = tree.xpath("//header/following-sibling::div[1]//ul[2]/li/a")

# print(movies)





# url="https://gkecopoldnr.ru/wp-content/uploads/2021/08/img2321_0.jpg"

# response =requests.get(url)
# with open('own.jpg','wb') as f:
#     f.write(response.content)

wget.download("https://github.com/ArifYetik/NLP-for-Large-Movie-Review-Dataset-Sentiment-Analysis/blob/main/Large_Movie_Review_sentiments.test.csv.zip")
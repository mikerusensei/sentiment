import requests
import re

class WebCrawl:
    def __init__(self,link) -> None:
        self.link = link
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Referer': 'http://www.google.com/',
        }

    def crawl(self):
        response = requests.get(self.link, headers=self.header)
        return response.text
    
class FecthReview:
    def __init__(self,link) -> None:
        self.link = link
        self.reviews = []

    def fetch(self):
        file = WebCrawl(self.link)

        content = file.crawl()

        pattern = r"class=\"cr-widget-FocalReviews\"([\s\S]*)"
        pattern2 = r"<div\sclass=\"a-row a-spacing-small review-data\">([\s\S]*?)<\/div>"
        pattern3 = r"<span>([\s\S]*?)<\/span>"

        result1 = re.search(pattern, content)

        if result1:
            result2 = re.findall(pattern2, result1.group(1))

            for i in range(len(result2)):
                #print(result2[i])
                if result2[i]:
                    review = re.search(pattern3, result2[i])
                    if review:
                        stripped = review.group(1).replace("<br />"," ")
                        self.reviews.append(stripped)
            
            return self.reviews
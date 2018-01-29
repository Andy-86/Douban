import random

import time

from baike import url_manger, html_downloader, html_parser, html_outputer


class SpindMan(object):
    def __init__(self):
        self.count=0
        self.urls=url_manger.UrlManger()
        self.downloader=html_downloader.HtmlDownLoader()
        self.parse=html_parser.HtmlParser()
        self.outputer=html_outputer.Htmloutuputer()
    def craw(self, rootUrl):
        self.urls.add_new_url(rootUrl)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print "craw:"+new_url
                html_con=self.downloader.download(new_url)
                new_urls,new_data=self.parse.parser(new_url,html_con)
                self.urls.add_new_urls(new_urls)
                self.outputer.collet_data(new_data)
                if(self.count==1000):
                    break
                self.count=self.count+1
                extime=random.random()+1
                print extime
                time.sleep(extime)
            except:
                print "can,t craw"


if __name__=='__main__':
    rootUrl="https://movie.douban.com/subject/26611804/?tag=%E7%83%AD%E9%97%A8&from=gaia"
    objectSpider=SpindMan()
    objectSpider.craw(rootUrl)
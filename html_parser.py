from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self,new_url, html_con):
        if html_con is None or new_url is None:
            return None
        soup=BeautifulSoup(html_con,'html.parser',from_encoding='utf-8')
        new_urls=self.get_new_urls(new_url,soup)
        new_datas=self.get_new_datas(new_url,soup)
        return new_urls,new_datas

    def get_new_urls(self, new_url, soup):
        new_urls=set()
        links=soup.find_all('div',class_="recommendations-bd")
        linkstr=links.__str__()
        sos=BeautifulSoup(linkstr[1:len(linkstr)-1],"html.parser",from_encoding='utf-8')
        dls=sos.find_all("dl")
        for link in dls:
            print link.dt.a['href']
            new_urls.add(link.dt.a['href'])
        return new_urls

    def get_new_datas(self, new_url, soup):
        res_data={}
        title_node=soup.find_all('span')
        for title in title_node:
            a=str(title)
            if a.__contains__('temreviewed'):
                print a[a.index('>')+1:len(a)-7]
                res_data['title']=a[a.index('>')+1:len(a)-7]
                break
        score=soup.find_all('strong',class_='ll rating_num')
        scorestr=str(score)
        print scorestr[52:55]
        res_data['score']=scorestr[52:55]
        summary=soup.find_all('div',class_='indent')
        summarystr=str(summary[1].span)
        print summarystr[38:len(summarystr)-7]
        return res_data




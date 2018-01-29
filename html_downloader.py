import urllib2


class HtmlDownLoader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        else:
            send_headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection':'keep-alive'
            }
            requset=urllib2.Request(new_url,headers=send_headers)
            respone=urllib2.urlopen(requset)
            if respone.getcode()==200:
                return respone.read()
            else:
                return None
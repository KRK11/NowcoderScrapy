import scrapy
from lxml import etree
from Design.items import MemberSpiderSpiderItem

class MemberSpiderSpider(scrapy.Spider):
    name = 'member_spider'
    allowed_domains = ['ac.nowcoder.com']
    custom_settings = {
        'ITEM_PIPELINES': {'Design.pipelines.MemberSpiderSpiderPipeline': 300},
    }
    suffix = '/practice-coding'
    count = 0
    all = 0

    def start_requests(self):
        with open('search_page.txt', 'r', encoding='utf-8') as fp:
            self.k = fp.read()
        ins = set()
        with open(r'url_member\url_member{}.txt'.format(self.k),'r',encoding='utf-8') as fp:
            for item in fp:
                if item in ins: continue
                ins.add(item)
                self.all = self.all + 2
                yield scrapy.Request(
                    url = item,
                    callback = self.parse,
                    meta = {'id':item[44:].strip()}
                )
                yield scrapy.Request(
                    url = item+self.suffix,
                    callback = self.parse,
                    meta = {'id':item[44:].strip()}
                )

    def parse(self, response):
        self.count = self.count + 1
        print('member_now:',format(self.count/self.all*100,'.3f'),'%')
        id = response.meta['id']
        response = etree.HTML(response.text)
        item = MemberSpiderSpiderItem()
        try:
            item['id'] = id
            if not response.xpath('/html/body/div[1]/div[2]/div[2]/div/ul/li/a/text()'):
                item['name'] = ' ' + response.xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/a[1]/text()')[0]
                item['rating'] = ' ' + response.xpath('/html/body/div/div[2]/div[2]/section/div[1]/div[1]/div/text()')[0]
                item['rank'] = ' ' + response.xpath('/html/body/div/div[2]/div[2]/section/div[1]/div[2]/div/text()')[0]
                if item['rank'] == ' 暂无' or item['rank'] == ' 9999+': item['rank'] = ' 10000000'
                item['rating_contest'] = ' ' + response.xpath('/html/body/div/div[2]/div[2]/section/div[1]/div[3]/div/text()')[0]
                item['contest'] = ' ' + response.xpath('/html/body/div/div[2]/div[2]/section/div[1]/div[4]/div/text()')[0]
                item['attention'] = ' ' + response.xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/div/a[1]/text()')[0]
                item['fans'] = ' ' + response.xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/div/a[2]/text()')[0]
                item['challenge'] = False
                item['accept'] = False
                item['summit'] = False
                item['ac_rate'] = False
            else:
                item['name'] = False
                item['rating'] = False
                item['rank'] = False
                item['rating_contest'] = False
                item['contest'] = False
                item['attention'] = False
                item['fans'] = False
                item['challenge'] = ' ' + response.xpath('/html/body/div[1]/div[2]/div[2]/section/div[1]/div[1]/div/text()')[0]
                item['accept'] = ' ' + response.xpath('/html/body/div[1]/div[2]/div[2]/section/div[1]/div[2]/div/text()')[0]
                item['summit'] = ' ' + response.xpath('/html/body/div[1]/div[2]/div[2]/section/div[1]/div[3]/div/text()')[0]
                item['ac_rate'] = ' ' + response.xpath('/html/body/div[1]/div[2]/div[2]/section/div[1]/div[4]/div/text()')[0]
        except Exception:
            item['name'] = False
            item['rating'] = False
            item['rank'] = False
            item['rating_contest'] = False
            item['contest'] = False
            item['attention'] = False
            item['fans'] = False
            item['challenge'] = False
            item['accept'] = False
            item['summit'] = False
            item['ac_rate'] = False

        yield item
        pass

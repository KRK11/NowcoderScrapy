import scrapy
from lxml import etree
from Design.items import RankSpiderSpiderItem

class RankSpiderSpider(scrapy.Spider):
    name = 'rank_spider'
    allowed_domains = ['ac.nowcoder.com']
    start_urls = 'https://ac.nowcoder.com/acm/contest/rating-index?pageSize=50&searchUserName=&onlyMyFollow=false&page={}'
    count = 0
    all = 0
    custom_settings = {
        'ITEM_PIPELINES': {'Design.pipelines.RankSpiderSpiderPipeline': 300},
    }

    def start_requests(self):
        with open('search_page.txt','r',encoding='utf-8') as fp:
            k = fp.read()
            self.all = eval(k)*50
            for i in range(1,eval(k)+1):
                url = self.start_urls.format(i)
                yield scrapy.Request(
                    url = url,
                    callback = self.parse
                )

    def parse(self, response):
        response = etree.HTML(response.text)
        for i in range(1, 51):
            self.count = self.count + 1
            print('rank_now:',format(self.count / self.all * 100, '.3f'), '%')
            item = RankSpiderSpiderItem()
            item['rank'] = ' ' + response.xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr[{}]/td[1]/span/text()'.format(i))[0]
            item['name'] = ' ' + response.xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr[{}]/td[2]/a/span/text()'.format(i))[0]
            state = response.xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr[{}]/td[3]/span/a/text()'.format(i))
            if state:
                item['school'] = ' ' + state[0]
            else:
                item['school'] = ' 无'
            state = response.xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr[{}]/td[4]/span/text()'.format(i))
            if state:
                item['description'] = ' ' + state[0]
            else:
                item['description'] = ' 无'
            item['rating'] = ' ' + response.xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr[{}]/td[5]/span/text()'.format(i))[0]
            item['id'] = ' ' + response.xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr[{}]/@data-uid'.format(i))[0]
            if response.xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr[{}]/td[2]/a/i'.format(i)):
                item['team'] = True
            else:
                item['team'] = False
            yield item

        pass

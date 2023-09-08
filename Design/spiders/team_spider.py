import re
import scrapy
from lxml import etree
from Design.items import TeamSpiderSpiderItem

class TeamSpiderSpider(scrapy.Spider):
    name = 'team_spider'
    allowed_domains = ['ac.nowcoder.com']
    suffix = '/practice-coding'
    prefix = 'https://ac.nowcoder.com/acm/team/member-list?token=&teamId='
    custom_settings = {
        'ITEM_PIPELINES': {'Design.pipelines.TeamSpiderSpiderPipeline': 300},
    }
    k = 0
    count = 0
    all = 0

    def start_requests(self):
        with open('search_page.txt', 'r', encoding='utf-8') as fp:
            self.k = fp.read()
        with open(r'url_team\url_team{}.txt'.format(self.k)) as fp:
            for item in fp:
                self.all = self.all + 3
                yield scrapy.Request(
                    url = item,
                    callback = self.parse,
                    meta = {'id':item[44:].strip()}
                )
                yield scrapy.Request(
                    url = item + self.suffix,
                    callback = self.parse,
                    meta = {'id':item[44:].strip()}
                )
                yield scrapy.Request(
                    url = self.prefix + item[44:].strip(),
                    callback = self.parse,
                    meta = {'id':item[44:].strip()}
                )

    def parse(self, response):
        item = TeamSpiderSpiderItem()
        self.count = self.count + 1
        print('team_now:',format(self.count/self.all*100,'.3f'),'%')
        id = response.meta['id']
        if response.text[0] == '{':
            item['id'] = id
            item['rating_contest'] = re.findall(r'"name":"(.*?)",',response.text)
            item['contest'] = re.findall(r'"uid":(\d+),',response.text)
            item['fans'] = False
            item['member_num'] = False
            item['page'] = False
        else:
            response = etree.HTML(response.text)
            try:
                item['id'] = id
                if not response.xpath('/html/body/div[1]/div[2]/div[2]/div/ul/li/a/text()'):
                    item['rating_contest'] = ' ' + response.xpath('/html/body/div/div[2]/div[2]/section/div[1]/div[3]/div/text()')[0]
                    item['contest'] = ' ' + response.xpath('/html/body/div/div[2]/div[2]/section/div[1]/div[4]/div/text()')[0]
                    item['fans'] = ' ' + response.xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/div/a/text()')[0]
                    item['member_num'] = ' ' + response.xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[4]/div/a/text()')[0]
                    item['page'] = True
                else:
                    item['rating_contest'] = ' ' + response.xpath('/html/body/div[1]/div[2]/div[2]/section/div[1]/div[1]/div/text()')[0]
                    item['contest'] = ' ' + response.xpath('/html/body/div[1]/div[2]/div[2]/section/div[1]/div[2]/div/text()')[0]
                    item['fans'] = ' ' + response.xpath('/html/body/div[1]/div[2]/div[2]/section/div[1]/div[3]/div/text()')[0]
                    item['member_num'] = ' ' + response.xpath('/html/body/div[1]/div[2]/div[2]/section/div[1]/div[4]/div/text()')[0]
                    item['page'] = False
            except Exception:
                item['id'] = ' '
                item['rating_contest'] = ' '
                item['contest'] = ' '
                item['fans'] = ' '
                item['member_num'] = ' '
                item['page'] = False

        yield item

        pass

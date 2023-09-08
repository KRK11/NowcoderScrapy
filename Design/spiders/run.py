import os
# from scrapy.crawler import CrawlerProcess
# from design.Design.spiders.rank_spider import RankSpiderSpider
# from design.Design.spiders.team_spider import TeamSpiderSpider
# from design.Design.spiders.member_spider import MemberSpiderSpider
# from scrapy.utils.project import get_project_settings
from subprocess import run, PIPE


class spider_main:
    def __init__(self,k):
        self.k = k
        with open('search_page.txt','w',encoding='utf-8') as fp: fp.write(k)
        if not os.path.exists('data_member\member{}.xlsx'.format(k)) or k == '1':
            self.implement = True
        else:
            self.implement = False

    def spider(self):
        if self.implement:
            # process = CrawlerProcess(get_project_settings())
            # process.crawl(RankSpiderSpider)
            # process.crawl(TeamSpiderSpider)
            # process.start()
            r = run('ping www.baidu.com',stdout = PIPE,stderr = PIPE,stdin = PIPE,shell = True)
            if not r:
                print("NetWork Error!")
                return
            os.system('scrapy crawl rank_spider -s CLOSESPIDER_TIMEOUT=3600')
            os.system('scrapy crawl team_spider -s CLOSESPIDER_TIMEOUT=3600')
            os.system('scrapy crawl member_spider -s CLOSESPIDER_TIMEOUT=3600')

        print('Successfully import!')

def main():
    if __name__ == '__main__':
        ac = spider_main('2')
        ac.spider()
        # from openpyxl import load_workbook
        # wb = load_workbook('data_Rank\Rank1.xlsx')
        # rank = wb['Rank']
        # print(rank.max_row)
        # wb.save('data_Rank\Rank1.xlsx')

main()
# print('!')
# start = time.time()
# main()
# print(time.time()-start,'s')
import time
from design.BS4.ac_spider import spider_main

# 测试用的，可以删掉

def main():
    if __name__ == '__main__':
        print('!')



start = time.time()
ac = spider_main('100')
ac.spider()
print(format(time.time() - start, '.4f'), 's')

#10 800s BS4
#20 2381s BS4
#100 7165s BS4
#10 385s scrapy
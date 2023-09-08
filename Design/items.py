import scrapy


class DesignItem(scrapy.Item):
    pass


# 榜单数据类
class RankSpiderSpiderItem(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    school = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    id = scrapy.Field()
    team = scrapy.Field()
    pass


# 团队类
class TeamSpiderSpiderItem(scrapy.Item):
    id = scrapy.Field()
    rating_contest = scrapy.Field() # challenge member1 member2 member3
    contest = scrapy.Field() # accept uid1 udi2 udi3
    fans = scrapy.Field() # summit
    member_num = scrapy.Field() # ac_rate
    page = scrapy.Field()
    pass


# 成员类
class MemberSpiderSpiderItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    rank = scrapy.Field()
    rating_contest = scrapy.Field()
    contest = scrapy.Field()
    attention = scrapy.Field()
    fans = scrapy.Field()
    challenge = scrapy.Field()
    accept = scrapy.Field()
    summit = scrapy.Field()
    ac_rate = scrapy.Field()
    pass
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    courseNumber = scrapy.Field()
    courseName = scrapy.Field()
    term = scrapy.Field()
    instructor = scrapy.Field()
    gpa = scrapy.Field()
    query = scrapy.Field()

# -*- coding: utf-8 -*-
import scrapy
from .. import items

class MuGradeDistSpider(scrapy.Spider):
    name = 'mu_grade_dist'
    start_urls = ['https://musis1.missouri.edu/gradedist/mu_grade_dist_intro.cfm#CGI.script.name#']

    def parse(self, response):
        try:
            yield scrapy.FormRequest.from_response(response, formdata={'vdept': self.dep}, callback=self.parse_dist)
        except AttributeError:
            print("\nDepartment code is required as an argument\nTry: scrapy crawl mu_grade_dist -a dep=<department code>\n")

    def parse_dist(self, response):
        ROW_SELECTOR = 'tr'
        CELL_TEXT_SELECTOR = 'td.flabelcell ::text'
        
        COURSE_NAME_INDEX = 1
        COURSE_NUMBER_INDEX = 2
        TERM_INDEX = 4
        INSTRUCTOR_INDEX = 6
        GPA_INDEX = 12
        for course in response.css(ROW_SELECTOR):
            
            if course.css(CELL_TEXT_SELECTOR).extract_first() != None:
                item = items.CourseItem()
                
                if len(course.css(CELL_TEXT_SELECTOR).extract()) <= GPA_INDEX:
                    item['courseNumber'] = course.css(CELL_TEXT_SELECTOR).extract()[COURSE_NUMBER_INDEX]
                    item['courseName'] = course.css(CELL_TEXT_SELECTOR).extract()[COURSE_NAME_INDEX]
                    item['term'] = course.css(CELL_TEXT_SELECTOR).extract()[TERM_INDEX]
                    item['instructor'] = "NA"
                    item['gpa'] = float(course.css(CELL_TEXT_SELECTOR).extract()[GPA_INDEX - 1])
                    item['query'] = self.dep
                else:
                    item['courseNumber'] = course.css(CELL_TEXT_SELECTOR).extract()[COURSE_NUMBER_INDEX]
                    item['courseName'] = course.css(CELL_TEXT_SELECTOR).extract()[COURSE_NAME_INDEX]
                    item['term'] = course.css(CELL_TEXT_SELECTOR).extract()[TERM_INDEX]
                    item['instructor'] = course.css(CELL_TEXT_SELECTOR).extract()[INSTRUCTOR_INDEX]
                    item['gpa'] = float(course.css(CELL_TEXT_SELECTOR).extract()[GPA_INDEX])
                    item['query'] = self.dep
                
                yield item
            
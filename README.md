# MU Grade Distribution Scraper

The MU Grade Distribution Scraper is a web scraper written with [Scrapy](https://doc.scrapy.org/en/latest/) that is designed to help students at Mizzou find the best classes to take and the best professors to take them with.

## How It Works
The project works by scraping data from the [MU Grade Distribution site](https://musis1.missouri.edu/gradedist/mu_grade_dist_intro.cfm#CGI.script.name#). It requests all records for the department code entered by the user (ex. CMP_SC for Computer Science). It then scrapes the course name, course number, course term, instructor, and GPA for each result and stores this data in a local [MongoDB](https://docs.mongodb.com/) collection.

## Usage
```
$ scrapy crawl mu_grade_dist -a dep=<department code>
```
**Note:** Department code can be any of the codes available in Course Subject dropdown on the [MU Grade Distribution site](https://musis1.missouri.edu/gradedist/mu_grade_dist_intro.cfm#CGI.script.name#).

The scraper will collect all of the data for the given department. The scraped data will be stored in the MongoDB database 'mu_grade_dist' in a collection named 'courses'.

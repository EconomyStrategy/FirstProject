''''' 
Created on 2019-8-28 
 
@author: test 
'''  
import scrapy.cmdline  
  
if __name__ == '__main__':  
    scrapy.cmdline.execute(argv=['scrapy','crawl','quotes'])  
    
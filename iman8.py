#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen

# if has Chinese, apply decode()
html = urlopen("https://www.arzlive.com/").read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')
#<td class="s3_10 price">28,510,000</td>

# print with title
for item in soup.find("td", {"class": "s3_11 price"}): 
    int_b = int(item.replace(',',''))
for item2 in soup.find("td", {"class": "s3_12 price"}):
    int_b2 = int(item2.replace(',',''))
for item3 in soup.find("td", {"class": "s3_13 price"}):
    int_b3 = int(item3.replace(',',''))
    a = int(int_b) 
    b = int(int_b2)
    c = int(int_b3)
    print (a)
    print (b)
    print (c)
    #a = int(raw_input("Price of nim = "))
    #b = int(raw_input("price of rob = "))
    #c = int(raw_input("price of euro= "))
    d = (b - 12550000)*20
    e = (b - 13650000)*8
    f = (b - 13550000)*11
    #g = d + e + f 
    h = (c - 7050000)*12
    #i = (b-9500)*2000
    g = d + e + f + h 
    print ('sod ='),g
    t=(b*39)+(12*c)
    print ('total='),t
    #k = (b*40) + (b*15) + (b*3000) + 7000000  
    #print k

#print("-------------------------")
# print without title
#for item in soup.find("table", {"id": "course-list"}).tr.next_siblings:
 #   print(item)

#print("-------------------------")
# navigate using next_sibling/previous_sibling
#print(soup.find("img", {"src": "https://morvanzhou.github.io/static/img/course_cover/scraping.jpg"}
#                ).parent.previous_sibling.get_text())

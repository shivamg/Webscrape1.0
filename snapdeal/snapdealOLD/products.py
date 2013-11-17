__author__ = 'shivamgupta'

import requests
import re

def productScraper():
    catId = [290, 21, 575, 7, 9, 17, 23, 226, 227, 474, 476, 473, 481, 6, 586, 658, 31,
             318, 5, 580, 694, 475, 364, 461, 159, 682, 66, 310, 493, 502, 516, 524, 539, 557, 217, 643, 619
            ]
    filename = "all products links.txt"
    for catI in catId:
        for i in range(1,2):
            url = 'http://www.snapdeal.com/json/product/get/search/%d/%i/20?q=&sort=plrty&keyword=&clickSrc' \
                  '=&viewType=Grid'%(catI,i*20)
            html = requests.get(url).text
            #print html[1:2]

            with open(filename, 'a') as f:

                positions = list(re.finditer('pageUrl', html))
                endPositions = list(re.finditer('addedToday', html))
                i = 1
                for position, endPosition in zip(positions,endPositions):
                        link = html[position.end()+3:endPosition.start()-3]
                        #link = link[link.index("href")+6:link.index("amp")-1]
                        if i == 1:
                            f.write("www.snapdeal.com/"+link)
                            print link
                            f.write("\n")
                        i = + 1

productScraper()

"""
http://www.snapdeal.com/products/catUrl?sort=plrty&, span id=no-of-results-filter
http://www.snapdeal.com/json/produc%t/get/search/%catId/i/20?q=&sort=plrty&keyword=&clickSrc=&viewType=Grid
   
    
    <a class="headerProductCategories" id='12' catId='12' catUrl="mobiles" name="Mobiles & Tablets" onclick="pickCategory(this)" vId="p">Mobiles & Tablets</a>
        </li>
        <li>
            <a class="headerProductCategories" id='21' catId='21' catUrl="computers" name="Computers & Peripherals" onclick="pickCategory(this)" vId="p">Computers & Peripherals</a>
        </li>
        <li>
            <a class="headerProductCategories" id='290' catId='290' catUrl="cameras" name="Cameras & Accessories" onclick="pickCategory(this)" vId="p">Cameras & Accessories</a>
        </li>
        <li>
            <a class="headerProductCategories" id='575' catId='575' catUrl="gaming" name="Gaming" onclick="pickCategory(this)" vId="p">Gaming</a>
        </li>
        <li>
            <a class="headerProductCategories" id='7' catId='7' catUrl="electronic" name="TVs, Audio & Video" onclick="pickCategory(this)" vId="p">TVs, Audio & Video</a>
        </li>
        <li>
            <a class="headerProductCategories" id='9' catId='9' catUrl="appliances" name="Appliances" onclick="pickCategory(this)" vId="p">Appliances</a>
        </li>
        <li>
            <a class="headerProductCategories" id='17' catId='17' catUrl="men-apparel" name="Men's Apparel" onclick="pickCategory(this)" vId="p">Men's Apparel</a>
            </li>
        <li>
            <a class="headerProductCategories" id='23' catId='23' catUrl="women-apparel" name="Women's Apparel" onclick="pickCategory(this)" vId="p">Women's Apparel</a>
            </li>
        <li>
            <a class="headerProductCategories" id='226' catId='226' catUrl="mens-footwear" name="Men's Footwear" onclick="pickCategory(this)" vId="p">Men's Footwear</a>
            </li>
        <li>
            <a class="headerProductCategories" id='227' catId='227' catUrl="womens-footwear" name="Women's Footwear" onclick="pickCategory(this)" vId="p">Women's Footwear</a>
            </li>
        <li>
            <a class="headerProductCategories" id='476' catId='476' catUrl="lifestyle-watches" name="Watches" onclick="pickCategory(this)" vId="p">Watches</a>
        </li>
        <li>
            <a class="headerProductCategories" id='474' catId='474' catUrl="bags" name="Bags & Luggage" onclick="pickCategory(this)" vId="p">Bags & Luggage</a>
        </li>
        <li>
            <a class="headerProductCategories" id='473' catId='473' catUrl="eyewear" name="Eyewear" onclick="pickCategory(this)" vId="p">Eyewear</a>
        </li>
        <li>
            <a class="headerProductCategories" id='481' catId='481' catUrl="fashion" name="Fashion Accessories" onclick="pickCategory(this)" vId="p">Fashion Accessories</a>
        </li>
        <li>
            <a class="headerProductCategories" id='6' catId='6' catUrl="jewelry" name="Fashion Jewellery" onclick="pickCategory(this)" vId="p">Fashion Jewellery</a>
        </li>
        <li>
            <a class="headerProductCategories" id='586' catId='586' catUrl="beauty" name="Beauty & Personal Care" onclick="pickCategory(this)" vId="p">Beauty & Personal Care</a>
        </li>
        <li>
            <a class="headerProductCategories" id='658' catId='658' catUrl="jewellery-precious" name="Precious Jewellery" onclick="pickCategory(this)" vId="p">Precious Jewellery</a>
        </li>
        <li>
            <a class="headerProductCategories" id='31' catId='31' catUrl="perfumes-beauty" name="Fragrances" onclick="pickCategory(this)" vId="p">Fragrances</a>
        </li>
        <li>
            <a class="headerProductCategories" id='318' catId='318' catUrl="health" name="Health & Nutrition" onclick="pickCategory(this)" vId="p">Health & Nutrition</a>
        </li>
        <li>
            <a class="headerProductCategories" id='5' catId='5' catUrl="home-kitchen" name="Home & Kitchen" onclick="pickCategory(this)" vId="p">Home & Kitchen</a>
        </li>
        <li>
            <a class="headerProductCategories" id='580' catId='580' catUrl="furniture" name="Furniture" onclick="pickCategory(this)" vId="p">Furniture</a>
        </li>
        <li>
            <a class="headerProductCategories" id='694' catId='694' catUrl="kitchen-bathroom-fittings" name="Kitchen & Bathroom Fittings" onclick="pickCategory(this)" vId="p">Kitchen & Bathroom Fittings</a>
        </li>
        <li>
            <a class="headerProductCategories" id='475' catId='475' catUrl="home-furnishing" name="Home Furnishing" onclick="pickCategory(this)" vId="p">Home Furnishing</a>
        </li>
        <li>
            <a class="headerProductCategories" id='364' catId='364' catUrl="books" name="Books" onclick="pickCategory(this)" vId="p">Books</a>
        </li>
        <li>
            <a class="headerProductCategories" id='461' catId='461' catUrl="stationery" name="Stationery & Office Supplies" onclick="pickCategory(this)" vId="p">Stationery & Office Supplies</a>
        </li>
        <li>
            <a class="headerProductCategories" id='159' catId='159' catUrl="sports-hobbies" name="Sports & Fitness" onclick="pickCategory(this)" vId="p">Sports & Fitness</a>
        </li>
        <li>
            <a class="headerProductCategories" id='682' catId='682' catUrl="hobbies" name="Hobbies" onclick="pickCategory(this)" vId="p">Hobbies</a>
        </li>
        <li>
            <a class="headerProductCategories" id='66' catId='66' catUrl="kids-toys" name="Infants, Kids & Toys" onclick="pickCategory(this)" vId="p">Infants, Kids & Toys</a>
        </li>
        <li>
            <a class="headerProductCategories" id='715' catId='715' catUrl="baby-care" name="Baby Care" onclick="pickCategory(this)" vId="p">Baby Care</a>
        </li>
        <li>
            <a class="headerProductCategories" id='720' catId='720' catUrl="kids-decor" name="Kids Decor" onclick="pickCategory(this)" vId="p">Kids Decor</a>
        </li>
        <li>
            <a class="headerProductCategories" id='310' catId='310' catUrl="automotive" name="Automotive" onclick="pickCategory(this)" vId="p">Automotive</a>
        </li>
        <li>
            <a class="headerProductCategories" id='493' catId='493' catUrl="kids-footwear" name="Kids Footwear" onclick="pickCategory(this)" vId="p">Kids Footwear</a>
        </li>
        <li>
            <a class="headerProductCategories" id='502' catId='502' catUrl="musical-instruments" name="Musical Instruments" onclick="pickCategory(this)" vId="p">Musical Instruments</a>
        </li>
        <li>
            <a class="headerProductCategories" id='516' catId='516' catUrl="entertainment" name="Movies & Music" onclick="pickCategory(this)" vId="p">Movies & Music</a>
        </li>
        <li>
            <a class="headerProductCategories" id='524' catId='524' catUrl="boys-clothing" name="Boys Clothing" onclick="pickCategory(this)" vId="p">Boys Clothing</a>
        </li>
        <li>
            <a class="headerProductCategories" id='539' catId='539' catUrl="girls-clothing" name="Girls Clothing" onclick="pickCategory(this)" vId="p">Girls Clothing</a>
        </li>
        <li>
            <a class="headerProductCategories" id='557' catId='557' catUrl="baby-clothing" name="Infant Wear" onclick="pickCategory(this)" vId="p">Infant Wear</a>
        </li>
        <li>
            <a class="headerProductCategories" id='217' catId='217' catUrl="home-kitchen-home-decoratives" name="Home Decoratives" onclick="pickCategory(this)" vId="p">Home Decoratives</a>
        </li>
        <li>
            <a class="headerProductCategories" id='643' catId='643' catUrl="gifts" name="Gifting & Events" onclick="pickCategory(this)" vId="p">Gifting & Events</a>
        </li>
        <li>
            <a class="headerProductCategories" id='691' catId='691' catUrl="women-ethnicwear" name="Women's Ethnic Wear" onclick="pickCategory(this)" vId="p">Women's Ethnic Wear</a>
"""
    
            
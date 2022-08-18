from bs4 import BeautifulSoup
# from bs4 import BeautifulSoup as bs4
import requests
import asyncio 
import time
# import grequests

selected_categories = ['Environment',
 'Business',
 'Tech',
 'Science',
 'Soccer',
 'NFL',
 'Tennis',
 'MLB',
 'NHL',
 'Film',
 'Fashion',
 'Food',
 'Travel']



"""
SOURCE TO SOUP & RETURN
"""
def SOUP(url):
    source =  requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')
    return soup




""" CATEGORY NAMME & SOURCE """
def Categories(base_url, category_tag, category_class ):
    #find caegories in nav item
    category_namelink_dict = {}
    for category in SOUP(base_url).find_all(category_tag, href=True, class_= category_class):
        
        # if the parsed category_name is in selected category
        if selected_categories.count(category.text.strip())>0:
            category_name = category.text.strip()
            category_link = category['href']
            #To skip repeat remove considered catagory from selected            
            selected_categories.remove(category_name)
            # print(category_name)
            # print(category_link)
            category_namelink_dict.update({category_name: category_link})
    return category_namelink_dict

'''
CATEGORY LANDING PAGE  (There next page is present)
'''
def Category_landing_page(category_namelink_dict, all_tag, all_attrs):
    landing_page_dict  = {}
    for i, (category_name, category_link) in enumerate(category_namelink_dict.items()):
        all_todays_story = SOUP(category_link).find(all_tag, attrs=all_attrs)
        if all_todays_story: 
            landing_page = all_todays_story['href']
            # print(f"{i+1}. {category_name}: {landing_page} (ALL)")
            landing_page_dict.update({category_name: landing_page})
    
        else:
            landing_page = category_link
            # print(f" {i+1}. {category_name}: {landing_page}")
            landing_page_dict.update({category_name: landing_page})
    # print(f"Landing page dictionary: {landing_page_dict}")
    return(landing_page_dict)



""" SINGLE NEXT PAGE """
# for category_name, category_page_link in category_namelink_dict.items():
'''
<a class="button button--small button--tertiary pagination__action--static " data-page="2" rel="next" href="https://www.theguardian.com/sport/tennis?page=2" data-link-name="Pagination view next" aria-label=" next page"> <span class="inline-arrow-left inline-icon pagination__icon pagination__icon--next"> 
       <svg width="6" height="12" viewBox="0 0 6 12" class="pagination__icon__svg pagination__icon--next__svg inline-arrow-left__svg inline-icon__svg"> 
        <path d="M6 11.5 1.5 6 6 .5 5.5 0 0 5.75v.5L5.5 12l.5-.5Z"></path> 
       </svg> </span> <span class="u-h">next</span> </a>
'''
def next_page(current_url,next_page_tag, next_page_attr): 
    # parse next page part    
    # next_page_url = SOUP(current_url).find(next_page_tag, class_=next_page_class)['href']
    next_page_url = SOUP(current_url).find(next_page_tag, next_page_attr)['href']

    # call SOU next page ur
    # next_page_soup = SOUP(next_page['href'])
    return next_page_url


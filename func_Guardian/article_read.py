from func import SOUP, Categories, Category_landing_page, next_page
import numpy as np


"""KEYS: CATEGORY NAME URL
"""
# Scrap category name and links 
base_url = "https://www.theguardian.com/international"  
category_tag = "a"
category_class =  "menu-item__title"  
"""-------------------------------"""
   
"""KEYS: CATEGORY LANDING PAGE """         
all_tag = 'a'
all_attrs = {"data-link-name":"all"}
"""-------------------------------"""

"""KEYS: NEXT PAGE  """
next_page_tag  = 'a'
next_page_attr = {"data-link-name":"Pagination view next"}
"""-------------------------------"""


"""
CALL FUNCTION: CATEGORY NAME URL"""
category_namelink_dict = Categories(base_url, category_tag, category_class)
print(category_namelink_dict) 
print("\n")


# # next_page(current_url,next_page_tag, next_page_attr)

"""
CALL FUNCTION: CATEGORY LANDING PAGE """
landing_page_dict = Category_landing_page(category_namelink_dict, all_tag, all_attrs)
print(landing_page_dict)


# landing_page_dict = {'Tech':'https://www.theguardian.com/technology/all', }

ARTICLE_2D = []

for category_name, landing_page in landing_page_dict.items():
    print(landing_page)
    
    COUNT_ARTICLE = 0
    
    while COUNT_ARTICLE < 30:
        try:
            for article_link in SOUP(landing_page).find_all('a', class_="u-faux-block-link__overlay js-headline-text", attrs={"data-link-name":"article"}): 
                print(COUNT_ARTICLE)
                # article link
                article_landing_url = article_link['href']
                # print(article_landing_url)        
                #article soup
                article_soup = SOUP(article_landing_url)
                
                # article title
                article_title = article_soup.find(attrs ={'data-gu-name':"headline"})
                article_subtitle = article_soup.find(attrs={'data-gu-name':"standfirst"})
                article_content = article_soup.find(attrs={'data-gu-name':"body"})
                try:    
                    authors = article_soup.find(attrs={"rel":"author"})            
                except Exception as e:
                    authors = article_soup.find(attrs={"aria-label":"Contributor info"})
                    
                try:
                    article_publication_date_time = article_soup.find('summary')
                except Exception as ex:
                    article_publication_date_time = article_soup.find(class_="dcr-km9fgb")            
                    # article_publication_date_time = np.nan
                                
                if article_title and article_subtitle and article_content and authors and article_publication_date_time:
                    # print(f"Title: {article_title.h1.text.strip()}\n")            
                    # print(f"Subtitle: {article_subtitle.text.strip()}\n")
                    # # print(f"Content: {article_content.text.strip()}\n")
                    # print(f"Author: {authors.text.strip()}\n")
                    # print(f"Date: {article_publication_date_time}\n")
                    # print("\n")
                    
                    ARTICLE = []
                    ARTICLE.append(article_title.h1.text.strip())       #title                     
                    ARTICLE.append(article_subtitle.text.strip())  #subtitle
                    ARTICLE.append(article_content.text.strip())        #title
                    ARTICLE.append(authors.text.strip())            #authors
                    ARTICLE.append(article_publication_date_time.text)  #date
                    ARTICLE.append(article_link['href'])            #url
                    ARTICLE.append(category_name)           # category
                    COUNT_ARTICLE+=1
                    # print(ARTICLE)
                    ARTICLE_2D.append(ARTICLE)
                else: continue
            """
            CALL FUNCTION: NEXT PAGE """
            landing_page = next_page(landing_page,next_page_tag, next_page_attr)
        except Exception as e:
            print(e.__class__)
            break
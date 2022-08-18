from func import SOUP, Categories, next_page


""" CATEGORY PAGE """
# Scrap category name and links 
base_url = "https://www.theguardian.com/international"  
category_tag = "a"
category_class =  "menu-item__title"     
# call func to collect category name and landing urls
category_namelink_dict = Categories(base_url, category_tag, category_class)
print(category_namelink_dict)  


""" NEXT PAGE """
# current_url = 'https://www.theguardian.com/sport/tennis'
next_page_tag  = 'a'
next_page_class = "button button--small button--tertiary pagination__action--static"
next_page_attr = {"data-link-name":"Pagination view next"}
next = next_page(current_url,next_page_tag, next_page_attr)
# print(next)


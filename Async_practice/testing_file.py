from func import SOUP, Categories, Category_landing_page, next_page
import numpy as np

#article soup
article_landing_url = "https://www.theguardian.com/money/2022/aug/13/amazon-waitrose-customer-banned-complaints-returning-too-much"

# article_landing_url = "https://www.theguardian.com/technology/2022/aug/14/can-artificial-intelligence-ever-be-sentient-googles-new-ai-program-is-raising-questions"
# article_landing_url = "https://www.theguardian.com/media/2022/jul/13/tim-westwood-accused-of-sex-with-14-year-old-girl-when-in-his-30s"
article_soup = SOUP(article_landing_url)

article_title = article_soup.find(attrs ={'data-gu-name':"headline"}).h1.text
print(f"Title: {article_title}\n")


# article subtitle
article_subtitle = article_soup.find(attrs={'data-gu-name':"standfirst"}).text
print(f"Subtitle: {article_subtitle}\n")

# article content
article_content = article_soup.find(attrs={'data-gu-name':"body"}).text
# print(f"Content: {article_content}\n")


## article authors
try:    
    authors = article_soup.find(attrs={"rel":"author"}).text
    print(f"Author: {authors}\n")
except Exception as e:
    authors = article_soup.find(attrs={"aria-label":"Contributor info"}).text.strip()
    print(f"Author: {authors}\n")

# article publication date time
try:
    article_publication_date_time = article_soup.find('summary').text
    print(f"Date: {article_publication_date_time}\n")
except Exception as e:
    article_publication_date_time = article_soup.find(class_="dcr-km9fgb") #dcr-km9fgb

    # article_publication_date_time = np.nan
    print(f"Date: {article_publication_date_time.text.strip()}\n")
    

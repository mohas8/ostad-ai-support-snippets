# from bs4 import BeautifulSoup
#
# html_doc = """
# <html>
#   <head><title>My Website</title></head>
#
#
#   <body>
#     <h1>Welcome to My Site</h1>
#     <p class="intro">This is a simple paragraph.</p>
#     <a href="http://example.com/page1">Link 1</a>
#     <a href="http://example.com/page2">Link 2</a>
#
#
#   </body>
# </html>
# """
#
# print(html_doc.strip())  # Print the HTML document without leading/trailing whitespace
#
#
# # soup = BeautifulSoup(html_doc, 'lxml')  # or 'html.parser'
# # print(soup.title)         # <title>My Website</title>
# # print(soup.title.string)  # My Website
# #
# # print(soup.h1.text)  # Welcome to My Site
# #
# # print(soup.find('p'))  # <p class="intro">This is a simple paragraph.</p>
# #
# # links = soup.find_all('a')
# # for link in links:
# #     print(link['href'])  # Extract the href attribute
# #
# # soup.find('p', class_='intro')  # Note: use class_, not class
# #
# # print(soup.get_text())

name = "Ostad\n\n\n\n"

print(name)

clean_name = name.strip()

print(clean_name)
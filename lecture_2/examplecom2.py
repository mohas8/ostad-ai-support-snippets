import requests
from bs4 import BeautifulSoup

url = "https://example.com/"
response = requests.get(url)

# Check if the request was successful
print("Status Code:", response.status_code)
html_content = response.text

# create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Print the entire HTML (for learning/debugging)
print(soup)

# Get the title tag
title_tag = soup.title
print("Title Tag:", title_tag)
print("Title Text:", title_tag.string)

# Get the first <h1> tag
h1_tag = soup.h1
print("H1 Tag:", h1_tag.text)

# Get the first <p> tag
p_tag = soup.p
print("Paragraph:", p_tag.text)

# Find all <p> tags
paragraphs = soup.find_all('p')
for i, p in enumerate(paragraphs):
    print(f"Paragraph {i+1}:", p.text)

# Using .parent, .children, .next_sibling, etc.
h1 = soup.h1
print("Parent of <h1>:", h1.parent.name)

# Strip unwanted whitespace
clean_text = p_tag.get_text(strip=False)
print("Clean Text:", clean_text)

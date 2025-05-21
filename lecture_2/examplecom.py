import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to the website
url = "https://example.com/"
response = requests.get(url)

# Step 2: Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract elements
title = soup.title.text                      # Get page title
heading = soup.h1.text                       # Get the main heading
paragraph = soup.p.text                      # Get the paragraph

# Step 4: Display results
print("Title:", title)
print("Heading:", heading)
print("Paragraph:", paragraph)

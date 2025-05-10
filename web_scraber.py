from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# Fetch the web page content
page = requests.get(url)

# Parse the page with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Find the desired table with the specified class
table = soup.find('table', {'class': 'wikitable sortable'})

# Extract the headers from the table
headers = [header.text.strip() for header in table.find_all('th')]
print(headers)


# Check if the table exists before processing
if table:
    rows = table.find_all('tr')  # Extract all rows within the table
    for row in rows:
        print(row.text.strip())  # Print the text content of each row, stripped of extra whitespace
else:
    print("Table not found!")
 
import pandas as pd

df = pd.DataFrame(columns = headers)    


# Extract the data from the table rows
for row in rows[1:]:                            # Skip the header row
    cols = row.find_all('td')                   # Extract all columns within the row
    cols = [ele.text.strip() for ele in cols]   # Get text and strip whitespace
    df.loc[len(df)] = cols                      # Append the data to the DataFrame

# Print the DataFrame to see the extracted data
print(df)

# Save the DataFrame to a CSV file
df.to_csv(r'C:\Users\m-nag\Desktop\Bruhcode\Scraped CSVs\largest_companies.csv', index=False)
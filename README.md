

```markdown
# Amazon Product Scraper

A Python-based scraper for extracting and cleaning Amazon product data using **Pandas**, **Selenium**, and **BeautifulSoup**.

## Features
- Extracts product details such as names, prices, and links from Amazon.
- Cleans and structures the data into a CSV file for easy analysis.
- Provides a modular, reusable code structure for web scraping projects.

## Installation

### 1. Clone this repository:
```bash
git clone https://github.com/Rayyan-Prog-ML/amazon-product-scraper.git
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the extraction script to scrape product details from Amazon:
```bash
python scripts/extracting_amazon.py
```
This will save the raw HTML files of the products in the `data/` directory.

### 2. Run the collection script to clean and structure the data into a CSV:
```bash
python scripts/collect_Amazon.py
```
This will process the HTML files, extract product names, prices, and links, and save the cleaned data to `outputs/New cleaning Amazonss-Products.csv`.

## Example Output

An example of the cleaned CSV data can be found in the `outputs/` folder, where each row contains the product name, price, and link.

## Python Code Example

Here’s a Python example from the `collect_Amazon.py` script:

```python
# collect_Amazon.py
"""
Script to parse Amazon HTML files and clean data.

Requires:
- BeautifulSoup
- pandas
"""

import os
import pandas as pd
from bs4 import BeautifulSoup

def parse_html_files(data_path):
    """Parses HTML files and extracts product data."""
    data = {"Name": [], "Price": [], "Link": []}
    for file in os.listdir(data_path):
        try:
            with open(f"{data_path}/{file}", 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                # Extract details
                title = soup.find("h2").get_text(strip=True)
                price = soup.find("span", class_="a-price-whole").get_text(strip=True)
                link = f"https://amazon.in{soup.find('a')['href']}"
                data["Name"].append(title)
                data["Price"].append(price.replace(",", ""))
                data["Link"].append(link)
        except Exception as e:
            print(f"Error parsing {file}: {e}")
    return data
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

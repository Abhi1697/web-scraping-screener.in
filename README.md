# All Listed Companies Data Scraper

This repository contains a Python script to scrape data of all market-listed companies in India from [Screener.in](https://www.screener.in/screens/357649/all-listed-companies/) and convert it into a CSV file. The script leverages the **BeautifulSoup** and **requests** libraries for web scraping, and **pandas** for data manipulation and CSV conversion.

## Features
- Scrapes data of all listed companies from the specified Screener.in page.
- Cleans and processes the data to ensure accuracy and consistency.
- Exports the data into a structured CSV file for further use.

## Prerequisites
To run the script, you need:
- **Python 3.x** installed on your system.
- The following Python libraries:
  - `beautifulsoup4`
  - `requests`
  - `pandas`

You can install these dependencies using the command:

```bash
pip install beautifulsoup4 requests pandas
```

## Usage
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the script:
   ```bash
   python MarketListedCompaniesIndia.py
   ```

3. The script will scrape data from [Screener.in](https://www.screener.in/screens/357649/all-listed-companies/) and generate a `data.csv` file in the repository folder.

## Files in the Repository
- `MarketListedCompaniesIndia.py`: Python script for web scraping and CSV conversion.
- `MarketListedCompaniesIndia.csv`: CSV converted file.
- `README.md`: Documentation for the repository.

## How It Works
1. **Web Scraping**: The script uses the `requests` library to fetch the webpage content and `BeautifulSoup` to parse the HTML structure.
2. **Data Extraction**: Relevant information such as company names, market capitalization, and other details is extracted from the webpage.
3. **Data Cleaning and Structuring**: The extracted data is cleaned and organized using `pandas`.
4. **CSV Export**: The processed data is saved as a `data.csv` file.

## Example Output
A sample of the generated CSV file might look like this:

| S.No | Name         | CMP (Rs.) | P/E   | Market Cap (Rs.Cr) | ... |
|------|--------------|-----------|-------|--------------------|-----|
| 1    | Reliance Ind | 2400      | 20.5  | 15,00,000          | ... |
| 2    | TCS          | 3200      | 30.1  | 12,00,000          | ... |

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Disclaimer
The data is scraped from a third-party website ([Screener.in](https://www.screener.in)). Ensure you comply with the website's terms of use before running the script. The author of this repository is not affiliated with Screener.in.

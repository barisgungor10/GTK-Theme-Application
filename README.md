# GNOME Theme Scraper

This script scrapes data from the gnome-look.org website to extract the names of popular GNOME themes.

## Requirements

- Python 3
- requests-html
- BeautifulSoup4

## Installation

1. Install the required packages using pip:


    pip install requests-html beautifulsoup4


2. Clone this repository or download the script file.

## Usage

1. Open a terminal and navigate to the directory where the script is located.

2. Run the script using Python:


python gnome_theme_scraper.py


The script will scrape data from the gnome-look.org website and print a list of popular GNOME theme names along with the total number of themes found.

## Customization

You can customize the script by modifying the `url_list` variable to include additional pages or change the sorting criteria. You can also modify the scraping logic to extract additional information about each theme.

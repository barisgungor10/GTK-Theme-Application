# GTK Theme Application

This repository contains a GTK theme application that allows users to explore and download themes from gnome-look.org. The application is built using the Gtk library and integrates web scraping functionality to fetch theme details. Users can view theme names, descriptions, and images, and download their preferred themes.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Prerequisites

To run the application, you'll need the following prerequisites:

- Python 3.x
- [Gtk library](https://pygobject.readthedocs.io/en/latest/getting_started.html)
- [requests-html](https://requests-html.kennethreitz.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/barisgungor10/GTK-Theme-Application.git
    cd GTK-Theme-Application
    ```

2. Install the required Python packages:

    ```bash
    pip install pygobject requests-html beautifulsoup4
    ```

## Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. The application will open, fetching and displaying theme information from gnome-look.org.

3. Navigate through different theme pages using the page switcher.

4. Click on the "Download" button to initiate the download for a specific theme.

## Contributing

Contributions are welcome! If you encounter any issues or have ideas for enhancements, please feel free to submit pull requests.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

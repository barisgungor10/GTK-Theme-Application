# Import necessary libraries
import urllib
import gi

# Make sure the required version of Gtk is available
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gio
from gi.repository.GdkPixbuf import Pixbuf
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# List of URLs to scrape from
url_list = [
    "https://www.gnome-look.org/browse?cat=135&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=2&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=3&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=4&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=5&ord=rating"
]

# Lists to store scraped data
theme_name_list = []
image_link_list = []
description_link_list = []

# Function to scrape data from the provided URLs
def scraping():
    for url in url_list:
        session = HTMLSession()
        response = session.get(url)
        response.html.render()

        soup = BeautifulSoup(response.html.html, 'html.parser')

        themes = soup.find_all("div", class_="product-browse-list-item container-wide standard")

        for theme in themes:
            theme_name_list.append(theme.find("h2").text)
            img_tag = theme.find("img")
            image_link_list.append(img_tag["src"])
            description_link_list.append(theme.find(class_="description").text)

    print(image_link_list)
    print(theme_name_list)
    print(description_link_list)

# Execute the scraping function
scraping()

# Function to handle download button click
def download_func(widget):
    print(f"Downloaded {widget}")

# Function to handle page switch in the stack
def on_page_switch(stack_switcher, _):
    visible_child_name = stack_switcher.get_stack().get_visible_child_name()
    print(f"Switched to page: {visible_child_name}")

# Class to define the main application window
class ApplicationWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Theme Application")

        self.set_border_width(10)
        self.set_default_size(800, 800)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

        # Create a header bar for the window
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Theme Application"

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        self.stack.set_transition_duration(500)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")
        header_bar.pack_start(box)

        # Define the number of themes per page and calculate the number of pages needed
        themes_per_page = 5  # Number of themes per page
        num_pages = -(-len(theme_name_list) // themes_per_page)  # Ceiling division

        # Loop through each page and populate the stack with theme data
        for page_num in range(num_pages):
            page_box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)
            page_box.set_border_width(10)

            # Populate each page with theme information
            for i in range(themes_per_page):
                index = page_num * themes_per_page + i
                if index >= len(theme_name_list):
                    break

                name = theme_name_list[index]
                image_link = image_link_list[index]
                description = description_link_list[index]

                # Create a horizontal box to hold image and details
                theme_box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.HORIZONTAL)

                # Load and resize the image
                response = urllib.request.urlopen(image_link)
                input_stream = Gio.MemoryInputStream.new_from_data(response.read(), None)
                pixbuf = Pixbuf.new_from_stream(input_stream, None)
                max_image_width = 150
                aspect_ratio = pixbuf.get_width() / pixbuf.get_height()
                scaled_width = min(pixbuf.get_width(), max_image_width)
                scaled_height = int(scaled_width / aspect_ratio)
                scaled_pixbuf = pixbuf.scale_simple(scaled_width, scaled_height, GdkPixbuf.InterpType.BILINEAR)

                # Create an image widget
                image = Gtk.Image.new_from_pixbuf(scaled_pixbuf)
                theme_box.pack_start(image, False, False, 0)

                # Create a vertical box to hold name, description, and download button
                details_box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)

                name_label = Gtk.Label(label=name)
                name_label.set_line_wrap(True)
                details_box.pack_start(name_label, False, False, 0)

                description_label = Gtk.Label(label=description)
                description_label.set_line_wrap(True)
                details_box.pack_start(description_label, False, False, 0)

                theme_box.pack_start(details_box, False, False, 0)

                # Create a horizontal box for the download button
                download_box = Gtk.Box(spacing=5, orientation=Gtk.Orientation.HORIZONTAL)
                download_button = Gtk.Button(label="Download")
                download_button.connect("clicked", download_func)
                download_box.pack_start(download_button, False, False, 0)
                theme_box.pack_start(download_box, False, False, 0)

                page_box.pack_start(theme_box, False, False, 0)

            # Add the populated page box to the stack with a corresponding title
            self.stack.add_titled(page_box, f"{page_num + 1}", f"{page_num + 1}")

        # Create a stack switcher to switch between pages in the stack
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(self.stack)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_box.pack_start(self.stack, True, True, 0)
        main_box.pack_start(stack_switcher, False, True, 0)
        self.add(main_box)

        # Connect the page switch event to the corresponding function
        stack_switcher.connect("notify::visible-child", on_page_switch)

# Create an instance of the ApplicationWindow class, connect the quit event, and show the window
win = ApplicationWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

# Start the Gtk main loop
Gtk.main()

import urllib
import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, GdkPixbuf, Gio
from gi.repository.GdkPixbuf import Pixbuf
from requests_html import HTMLSession
from bs4 import BeautifulSoup

url_list = [
    "https://www.gnome-look.org/browse?cat=135&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=2&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=3&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=4&ord=rating"
]
theme_name_list = []
image_link_list = []
description_link_list = []


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


scraping()


class ApplicationWindow(Gtk.Window):
    def _init_(self):
        Gtk.Window._init_(self, title="Theme Application")

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(500)

        themes_per_page = 5  # Number of themes per page
        num_pages = -(-len(theme_name_list) // themes_per_page)  # Ceiling division

        for page_num in range(num_pages):
            page_box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)
            page_box.set_border_width(10)

            for i in range(themes_per_page):
                index = page_num * themes_per_page + i
                if index >= len(theme_name_list):
                    break

                name = theme_name_list[index]
                image_link = image_link_list[index]
                description = description_link_list[index]

                # Create a horizontal box to hold image and details
                theme_box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.HORIZONTAL)

                # Load the image
                response = urllib.request.urlopen(image_link)
                input_stream = Gio.MemoryInputStream.new_from_data(response.read(), None)
                pixbuf = Pixbuf.new_from_stream(input_stream, None)

                # Resize the image
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

                # Create a horizontal box for the download button
                download_box = Gtk.Box(spacing=5, orientation=Gtk.Orientation.HORIZONTAL)
                download_button = Gtk.Button(label="Download")
                download_button.connect("clicked", self.download_func)
                download_box.pack_start(download_button, False, False, 0)
                details_box.pack_start(download_box, False, False, 0)

                theme_box.pack_start(details_box, True, True, 0)

                page_box.pack_start(theme_box, False, False, 0)

            self.stack.add_titled(page_box, f"page{page_num + 1}", f"Page {page_num + 1}")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(self.stack)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_box.pack_start(stack_switcher, False, True, 0)
        main_box.pack_start(self.stack, True, True, 0)
        self.add(main_box)

        stack_switcher.connect("notify::visible-child", self.on_page_switch)

    def on_page_switch(self, stack_switcher, _):
        visible_child_name = stack_switcher.get_stack().get_visible_child_name()
        print(f"Switched to page: {visible_child_name}")

    def download_func(self, widget):
        print(f"Downloaded {widget}")

win = ApplicationWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

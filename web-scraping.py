import gi
import urllib

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GdkPixbuf
from gi.repository.GdkPixbuf import Pixbuf

from requests_html import HTMLSession
from bs4 import BeautifulSoup

url_list = {
    "https://www.pling.com/browse?cat=135&page=1&ord=rating",
    "https://www.pling.com/browse?cat=135&page=2&ord=rating",
    "https://www.pling.com/browse?cat=135&page=3&ord=rating",
    "https://www.pling.com/browse?cat=135&page=4&ord=rating",
    "https://www.pling.com/browse?cat=135&page=5&ord=rating"
}
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
        ''''
----------------------------------------------------------------
                          ADD LABEL
----------------------------------------------------------------
        label = Gtk.Label()
        label.set_label("TEXT")
        label.set_halign(Gtk.Align.CENTER)
        self.add(label)
----------------------------------------------------------------
                          ADD BUTTON
----------------------------------------------------------------
        button = Gtk.Button(label="Print Something")
        button.connect("clicked",self.writing_func)
        self.add(self.button)
        
    def writing_func():
        print("Something")
----------------------------------------------------------------
                            BOXES
----------------------------------------------------------------
        box = Gtk.Box(spacing = 10)
        self.add(box)

        # Button 1
        button1 = Gtk.Button(label="Button 1")
        button1.connect("clicked",self.writing_func)
        box.pack_start(button1, True, True , 0)
        
        #Button 2
        button2 = Gtk.Button(label="Button 2")
        button2.connect("clicked",self.writing_func),
        box.pack_start(button2, True, True, 0)
        
    def writing_func(self,widget):
        print(f"You clicked {widget.get_label()}")
----------------------------------------------------------------
                          GRIDS
----------------------------------------------------------------
        grid=Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label = "Button 1")
        button1.connect("clicked",writing_func)
        
        button2 = Gtk.Button(label = "Button 2")
        button2.connect("clicked",writing_func)

        grid.attach(button1, 0,0,5,5)
        grid.attach(button2,0,6,5,5)

    def writing_func(self,widget):
        print(f"You clicked {widget.get_label()}")
----------------------------------------------------------------
                          LISTBOX
----------------------------------------------------------------
        self.set_border_width(5)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        row_1 = Gtk.ListBoxRow()
        listbox.add(row_1)

        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 5)
        row_1.add(box_1)

        label_1 = Gtk.Label()
        label_1.set_label("Label 1")
        box_1.pack_start(label_1,True, True, 0)

        button_1 = Gtk.Button(label = "Button 1")
        button_1.connect("clicked", self.writing_func)
        box_1.pack_start(button_1,True,True, 0)

        check_1 = Gtk.CheckButton()
        box_1.pack_start(check_1,True,True,0)

        switch_1 = Gtk.Switch()
        box_1.pack_start(switch_1,True,True,0)

################################################################################################
        row_2 = Gtk.ListBoxRow()
        listbox.add(row_2)

        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 5)
        row_2.add(box_2)

        label_2 = Gtk.Label()
        label_2.set_label("Label 2")
        box_2.pack_start(label_2,True,True,0)

        button_2 = Gtk.Button(label = "Button 2")
        button_2.connect("clicked",self.writing_func)
        box_2.pack_start(button_2,True,True,0)

        check_2 = Gtk.CheckButton()
        box_2.pack_start(check_2, True, True, 0)

        switch_2 = Gtk.Switch()
        box_2.pack_start(switch_2, True, True, 0)

    def writing_func(self,widget):
        print(f"You clicked {widget.get_label()}")
----------------------------------------------------------------
                      sTACK AND STACK SWITCHER            
----------------------------------------------------------------
        self.set_border_width(10)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.add(box)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.OVER_LEFT)
        stack.set_transition_duration(500)

        box_1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        label_1=Gtk.Label()
        label_1.set_label("LABEL 1")
        box_1.pack_start(label_1,True,True,0)

        button_1=Gtk.Button(label="BUTTON 1")
        box_1.pack_start(button_1,True,True,0)
        stack.add_titled(box_1 ,"button_1","Button_1")

        label_2 = Gtk.Label()
        label_2.set_label("Label 2")
        stack.add_titled(label_2 ,"button_2","Button_2")

        button_3=Gtk.Button(label="Button 3")
        stack.add_titled(button_3,"button_3","Button_3")
        stack_switcher= Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

        box.pack_start(stack,True,True,0)
        box.pack_start(stack_switcher, True, True, 0)
----------------------------------------------------------------
                        HEADER BAR
----------------------------------------------------------------
        self.set_border_width(10)
        self.set_default_size(500,500)

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Theme Application"
        self.set_titlebar(header_bar)

        box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(),"linked")

        left_arrow = Gtk.Button()
        left_arrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(left_arrow)

        right_arrow = Gtk.Button()
        right_arrow.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(right_arrow)

        header_bar.pack_start(box)
----------------------------------------------------------------
                          TEXT STYLING
----------------------------------------------------------------
        self.set_border_width(20)
        self.set_default_size(500,500)
        self.set_position(Gtk.WindowPosition.CENTER)

        main_box = Gtk.Box(spacing = 20)
        main_box.set_homogeneous(False)
        self.add(main_box)

        left_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 20)
        left_box.set_homogeneous(False)
        main_box.pack_start(left_box, True,True,0)

        right_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing = 20)
        right_box.set_homogeneous(False)
        main_box.pack_end(right_box, True, True, 0)

        label_1 = Gtk.Label()
        label_1.set_text("THIS IS LEFT JUSTIFIED TEXT")
        label_1.set_line_wrap(False)
        label_1.set_justify(Gtk.Justification.LEFT)            #   Use Gtk.justification.FILL for newspaper
        left_box.pack_start(label_1, True, True, 0)

        label_2 = Gtk.Label()
        label_2.set_text("THIS IS RIGHT JUSTIFIED TEXT")
        label_2.set_line_wrap(False)
        label_2.set_justify(Gtk.Justification.RIGHT)            #   Use Gtk.justification.FILL for newspaper
        left_box.pack_start(label_2, True, True, 0)

        label_3 = Gtk.Label()
        label_3.set_markup("<small> Small Text </small>\n"
                           "<big> Big Text </big>\n"
                           "<b> Bold Text </b>\n"
                           "<i> Italic Text </i>\n"
                           "<a href = 'https://chat.openai.com/' title = 'CLICK HERE' > Chat GPT </a>")
        label_3.set_line_wrap(True)
        right_box.pack_start(label_3, True, True, 0)

        label_4 = Gtk.Label()
        label_4.set_text("THIS IS RIGHT JUSTIFIED TEXT")
        label_4.set_line_wrap(True)
        label_4.set_justify(Gtk.Justification.RIGHT)  # Use Gtk.justification.FILL for newspaper
        right_box.pack_start(label_4, True, True, 0)
----------------------------------------------------------------
                          USER INPUT
----------------------------------------------------------------
'''
        self.set_border_width(10)
        self.set_default_size(height=900,width=800)
        self.set_position(Gtk.WindowPosition.CENTER)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(main_box)

        for i in range(3):
            grid = Gtk.Grid(column_spacing = 6)
            main_box.pack_start(grid, True, True, 0)

            response = urllib.request.urlopen(image_link_list[i])
            input_stream = Gio.MemoryInputStream.new_from_data(response.read(), None)
            pixbuf = Pixbuf.new_from_stream(input_stream, None)
            image = Gtk.Image()
            image.set_halign(True)
            resized_pixbuf = pixbuf.scale_simple(200, 150, GdkPixbuf.InterpType.BILINEAR)

            image.set_from_pixbuf(resized_pixbuf)
            grid.attach(image, 0, i, 1, 1)

            name = Gtk.Label(label=theme_name_list[i])
            name.set_line_wrap(True)
            grid.attach(name, 1, i, 1, 1)

            description = Gtk.Label(label=description_link_list[i])
            description.set_line_wrap(True)
            description.set_size_request(300, -1)
            grid.attach(description, 2, i, 1, 1)

            download_button = Gtk.Button(label="Download")
            download_button.connect("clicked", self.download_func)
            download_button.set_size_request(80, -1)
            grid.attach(download_button, 3, i, 1, 1)

    def download_func(self):
        print("Downloaded")


window = (ApplicationWindow())
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

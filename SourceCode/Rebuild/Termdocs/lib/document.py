class Document:
    path = ""
    swap_path = ""
    position = 0
    offset = 0
    lines = []
    line_numbering = True
    line_spacing = 0
    line_spacing_string = ""
    tab_width = 0
    tab_string = ""
    tab_replacement = False

    def __init__(self):
        pass

    def to_string(self):
        print("Path: " + self.path)
        print("Swap: " + self.swap_path)
        print("Position: " + str(self.position))
        print("Offset: " + str(self.offset))
        print("Line Spacing: " + str(self.line_spacing))
        print("Tab Width: " + str(self.tab_width))
        print("Tab Replacement: " + self.tab_replacement_string)
     
    def set_path(self, new_path):
        self.path = new_path

    def set_swap_path(self, new_swap_path):
        self.swap_path = new_swap_path

    def set_offset(self, new_offset):
        self.offset = new_offset
         
    def set_lines(self, new_lines):
        self.lines = new_lines
    def set_position(self, new_position):
        self.position = new_position

    def set_line_spacing(self, new_line_spacing):
        self.line_spacing = new_line_spacing

    def set_line_spacing_string(self, new_line_spacing_string):
        self.line_spacing_string = new_line_spacing_string

    def set_tab_width(self, new_tab_width):
        self.tab_width = new_tab_width

    def set_tab_string(self, new_tab_string):
        self.tab_string = new_tab_string


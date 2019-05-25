from DocumentAssets.document import Document
from DocumentAssets.document_reader import DocumentReader
from DocumentAssets.document_writer import DocumentWriter
from DocumentAssets.document_printer import DocumentPrinter
from input_tester import InputTester
from user_input import UserInput

import os

class DocumentController:
    def __init__(self):
        self.document = Document()
        self.reader = DocumentReader()
        self.writer = DocumentWriter()
        self.printer = DocumentPrinter()
        self.input_tester = InputTester()
        self.input = UserInput()

    def change_path(self, new_path):
        result = False
        test_path = self.input_tester.valid_path(new_path)
        if test_path:
            self.document.set_path( new_path )
            result = True
        return result

    def create_swap_path(self):
        result = False
        new_swap_path = self.document.path + "~swap"
        test_swap_path = self.input_tester.valid_swap(new_swap_path)
        if test_swap_path:
            self.document.set_swap_path( new_swap_path )
            result = True
        return result
            
    def delete_swap_file(self):
        result = False
        swap_path = self.document.swap_path
        test_swap_exists = self.input_tester.valid_path( swap_path )
        if test_swap_exists:
            os.remove( swap_path )
            result = True
        return result

    def swap_exists(self):
        result = False
        continue_result = self.input.swap_exists()
        if continue_result == "y":
            new_swap_path = self.document.path + "~swap"
            count = 0
            while self.input_tester.valid_path(new_swap_path):
                new_swap_path = new_swap_path + str(count)
                count += 1
            result = True
        return result

    def change_position(self, new_position):
        result = False
        test_int = self.input_tester.integer( new_position )
        if test_int:
            new_position = int(new_position)
            test_position = self.input_tester.in_bounds( new_position, self.document )
            if test_position:
                self.document.set_position( new_position )
                result = True
        return result

    def increment_position(self):
        new_position = self.document.position + 1
        test_position = self.input_tester.in_bounds( new_position, self.document )
        if test_position:
            self.document.set_position( new_position )
        else:
            self.document.set_position( 0 )

    def decrement_position(self):
        new_position = self.document.position - 1
        test_position = self.input_tester.in_bounds( new_position, self.document )
        if test_position:
            self.document.set_position( new_position )
        else:
            new_position = len( self.document.lines ) - 1
            self.document.set_position( new_position )

    def change_offset(self, new_offset):
        result = False
        test_int = self.input_tester.integer( new_offset )
        if test_int:
            new_offset = int(new_offset)
            test_bounds = self.input_tester.in_bounds( new_offset, self.document )
            if test_bounds:
                self.document.set_offset( new_offset )
                result = True
        return result
         
    def load_lines(self, path):
        result = False
        test_path = self.input_tester.valid_path( path )
        if test_path:
            lines = self.reader.read_document( path )
            if lines != []:
                self.document.set_lines( lines )
                result = True
        return result

    def load_lines_current_path(self):
        return self.load_lines( self.document.path )

    def load_lines_swap_path(self):
        return self.load_lines( self.document.swap_path )

    def save_lines(self, path, lines):
        result = False
        write_success = self.writer.write( path, lines )
        if write_success:
            result = True
        return result

    def save_lines_current_path(self):
        return self.save_lines( self.document.path, self.document.lines )

    def save_lines_swap_path(self):
        return self.save_lines( self.document.swap_path, self.document.lines )

    def print_selection(self, with_lines, lines, start, end, spacing_string ):
        end_in_bounds = self.input_tester.in_bounds( end )
        start_in_bounds = self.input_tester.in_bounds( start )
        if not end_in_bounds:
            end = 0
        if not start_in_bounds:
            start = 0
        if with_lines:
            self.printer.with_numbers( lines, start, end, spacing_string )
        else:
            self.printer.without_numbers( lines, start, end, spacing_string )

    def print_document(self):
        with_lines = True
        document = self.document
        end = document.position - document.offset
        self.print_selection( True, document.lines, document.position, end, document.spacing_string )



from lib.document_controller import DocumentController

def main():
    controller = DocumentController()
    clean(controller)
    controller = sets_path(controller)
    controller = sets_swap(controller)

    controller = loads_lines(controller)

    controller = creates_swap_file(controller)
    controller = deletes_swap(controller)

    controller = writes_lines(controller)

    controller = changes_offset(controller)
    controller = offset_less_than_lines_length(controller)
    controller = offset_greater_than_equal_zero(controller)

    controller = changes_position(controller)
    controller = position_can_not_be_set_past_length_of_lines(controller)
    controller = position_can_not_be_set_less_than_zero(controller)

    controller = increments_position(controller)
    controller = increment_past_lines_length_sets_position_to_zero(controller)

    controller = decrement_past_zero_sets_position_to_lines_last_index(controller)
    controller = decrements_position(controller)

    clean(controller)

def sets_path(controller):
    test_path = "JUNK"
    controller.change_path(test_path)
    assert controller.document.path == test_path
    return controller


def sets_swap(controller):
    test_swap = "JUNK~swap"
    controller.create_swap_path()
    assert controller.document.swap_path == test_swap
    return controller

def loads_lines(controller):
    test_lines = []
    assert controller.document.path == "JUNK"
    controller.load_lines_current_path()
    assert controller.document.lines != test_lines
    return controller

def creates_swap_file(controller):
    swap_path = controller.document.swap_path
    assert controller.input_tester.valid_path(swap_path) == False
    assert controller.document.lines != []
    controller.save_lines_swap_path()
    assert controller.input_tester.valid_path(swap_path) == True
    return controller

def deletes_swap(controller):
    swap_path = controller.document.swap_path
    controller.delete_swap_file()
    assert controller.input_tester.valid_path(swap_path) == False
    controller.save_lines_swap_path()
    return controller

def writes_lines(controller):
    lines = controller.document.lines
    controller.load_lines(controller.document.swap_path)
    assert lines == controller.document.lines
    return controller

def changes_offset(controller):
    start_offset = 0
    new_offset = 10
    current_offset = controller.document.offset
    assert current_offset == start_offset
    controller.change_offset( new_offset )
    current_offset = controller.document.offset
    assert current_offset == new_offset
    return controller

def changes_position(controller):
    start_position = 0
    new_position = 10
    assert controller.document.position == start_position
    controller.change_position( new_position )
    assert controller.document.position == new_position
    controller.change_position( start_position )
    return controller

def increments_position(controller):
    start_position = 0
    new_position = 1
    assert controller.document.position == start_position
    controller.increment_position()
    assert controller.document.position == new_position
    controller.document.set_position( 0 )
    return controller

def decrements_position(controller):
    start_position = 0
    assert controller.document.position == start_position
    controller.document.set_position( 1 )
    controller.decrement_position()
    assert controller.document.position == start_position
    return controller

def decrement_past_zero_sets_position_to_lines_last_index(controller):
    start_position = 0
    end_position = len(controller.document.lines) - 1
    assert controller.document.position == start_position
    controller.decrement_position()
    assert controller.document.position == end_position
    controller.document.position = 0
    return controller

def increment_past_lines_length_sets_position_to_zero(controller):
    start_position = len(controller.document.lines) - 1
    end_position = 0
    controller.document.set_position( start_position )
    assert controller.document.position == start_position
    controller.increment_position()
    assert controller.document.position == end_position
    return controller

def position_can_not_be_set_past_length_of_lines(controller):
    start_position = 0
    test_position = len(controller.document.lines)
    controller.change_position( test_position )
    assert controller.document.position == start_position
    return controller

def position_can_not_be_set_less_than_zero(controller):
    start_position = 0
    test_position = -1
    controller.change_position( test_position )
    assert controller.document.position == start_position
    return controller

def offset_less_than_lines_length(controller):
    starting_offset = 0
    test_offset = len(controller.document.lines)
    controller.document.offset = starting_offset
    assert controller.document.offset == starting_offset
    controller.change_offset( test_offset )
    assert controller.document.offset == starting_offset
    return controller

def offset_greater_than_equal_zero(controller):
    starting_offset = 0
    test_offset = -1
    controller.document.offset = starting_offset
    assert controller.document.offset == starting_offset
    controller.change_offset( test_offset )
    assert controller.document.offset == starting_offset
    return controller

def clean(controller):
    test_swap = "JUNK~swap"
    if controller.input_tester.valid_path( test_swap ):
        controller.document.swap_path = test_swap
        controller.delete_swap_file()

main()

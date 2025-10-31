from Topology_Creator import *
import dearpygui.dearpygui as dpg
from Tutorial import *
from File_Handling import *
from Tutorial import Tutorial_Begin

def Get_Viewport_Size():# Returns the current viewport size
    viewport_width = dpg.get_viewport_width()
    viewport_height = dpg.get_viewport_height()
    return viewport_width, viewport_height

def Main_Window(window_width, window_height):# Creates the intro window with buttons for picking the way that the user wants to start the program
    with dpg.window(label="Main Window", tag="main_window", width=window_width, height=window_height, no_resize=True, no_collapse=True, no_move=True, no_close=True) as main_window:
        with dpg.group():
            Menu_Buttons(Button_Data(), window_width, window_height, 4)
        dpg.set_primary_window("main_window", True)



def Button_Data():# Returns a list of button labels and their corresponding callback functions
    return [
            ("New File", lambda:New_File_Run()),#function from New_File.py
            ("Load File", lambda: Load_File()),#function from File_Handling.py
            ("Tutorial", lambda: Tutorial_Begin()),#function from Tutorial.py
        ]

def Menu_Buttons(button_data, window_width, window_height, vertical_spacing):
    button_width = window_width // len(button_data)
    button_height = int(window_height / (vertical_spacing * 4))
    spacing = int((window_height - (len(button_data) * button_height)) // (len(button_data) + 1))
    x_position = (window_width - button_width) // 2

    for i, (label, callback) in enumerate(button_data):
        y_position = int((i + 1) * spacing + i * button_height)
        dpg.add_button(label=label, width=button_width, height=button_height, pos=(x_position, y_position), callback=callback)

def Setup_Viewport():
    dpg.create_context()
    dpg.create_context()
    dpg.create_viewport(title='TopologyCreator', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    

def Start_Program():
    Setup_Viewport()
    viewport_width, viewport_height = Get_Viewport_Size()
    Main_Window(viewport_width, viewport_height)
    dpg.start_dearpygui()


dpg.destroy_context()

import dearpygui.dearpygui as dpg
from Topology_Creator import *
from Main_Menu import *

def Tutorial_Begin():
    dpg.hide_item("main_window")  # Do not delete the main window unless you are replacing it
    with dpg.window(label="Tutorial",tag="tutorial_window",width=800,height=600,no_resize=True,no_collapse=True,no_move=True,no_close=True,pos=(600,0)):
        Tutorial_Begin_Populate()

def Tutorial_Begin_Populate():
    dpg.add_text("Welcome to the Tutorial!")
    dpg.add_text("This is a simple introduction to the features of the program.")
    dpg.add_button(label="Start Tutorial", callback=Tutorial_Step_1)
    dpg.add_button(label="Exit Tutorial", callback=lambda: Finish_Tutorial())

def Tutorial_Step_1():
    dpg.delete_item("tutorial_window")
    with dpg.window(label="Tutorial Step 1", tag="tutorial_step_1", width=800, height=600, no_resize=True, no_collapse=True, no_move=True, no_close=True,pos=(600,0)):
        dpg.add_text("This is the first step of the tutorial.")
        #talk about the Menu Hotbar, make the hotbar and present each button by letting each button open a new window with information about the button
        dpg.add_text("Here you can learn about the Menu Hotbar.")
        dpg.add_text("The Menu Hotbar is located at the top of the window and contains buttons for different actions.")
        dpg.add_text("Click on a button to learn more about it.")
        dpg.add_button(label="Next", callback=Tutorial_Step_2)
        dpg.add_button(label="Back to Main Menu", callback=lambda: Finish_Tutorial())
    Menu_buttons_selection = [
        ("Hardware", lambda: Hardware_Selection_Explanation()),
        ("Edit", lambda: Edit_Explanation()),
        ("Save", lambda: Save_Explanation()),]
    with dpg.window(label="Menus", width=500, height=100, pos=(0, 0), no_close=True, no_resize=True, no_move=True, no_collapse=True, no_title_bar=True,tag="Menus"):
        Menu_Buttons(Menu_buttons_selection, 500, 100, 10)

def Hardware_Selection_Explanation():
    with dpg.window(label="Hardware Selection", tag="hardware_selection_window", width=400, height=300, no_resize=True, no_collapse=True, no_move=True, no_close=True, pos=(600,100)):
        dpg.add_text("This opens Hardware Selection window.", wrap=380)
        dpg.add_text("Here you can select the hardware you want to add.", wrap=380)
        dpg.add_text("When selecting a hardware to add to the topology the information about the hardware is also presented in the hardware information window.", wrap=380)
        dpg.add_button(label="Close", callback=lambda: dpg.delete_item("hardware_selection_window"))

def Edit_Explanation():
    with dpg.window(label="Edit Menu", tag="edit_menu_window", width=400, height=300, no_resize=True, no_collapse=True, no_move=True, no_close=True,pos=(600,0)):
        dpg.add_text("This is opens Edit topology window.")
        dpg.add_text("Here you can edit the topology you are working on by selecting devices then adding or removing connections.",wrap = 380)
        dpg.add_button(label="Close", callback=lambda: dpg.delete_item("edit_menu_window"))

def Save_Explanation():
    with dpg.window(label="Save Menu", tag="save_menu_window", width=400, height=300, no_resize=True, no_collapse=True, no_move=True, no_close=True):
        dpg.add_text("This is the Save Menu window.")
        dpg.add_text("Here you can save your current topology to return to later by inputing the name you wish to save as .",wrap = 380)
        dpg.add_text("When saving you must be careful as if the name already exists you will overwrite the existing file.",wrap = 380)
        dpg.add_button(label="Close", callback=lambda: dpg.delete_item("save_menu_window"))





def Tutorial_Step_2():
    dpg.delete_item("tutorial_step_1")
    with dpg.window(label="Tutorial Step 2", tag="tutorial_step_2", width=400, height=500, no_resize=True, no_collapse=True, no_move=True, no_close=True,pos=(600,150)):
        dpg.add_text("This is the second step of the tutorial.")
        dpg.add_text("Here you can learn about the different Hardware.")
        dpg.add_text("Click on a hardware button to learn more about it.")
        Globalise_Hardware_Selection()
        Hardware_Presentation()
        dpg.add_button(label="Next", callback=Tutorial_Step_3)
        dpg.add_button(label ="Return to Main Menu", callback=lambda: Finish_Tutorial())




def Globalise_Hardware_Selection():
    global Hardware_Selection
    Hardware_Selection = {
    "Access Point": {"Description": "An access point is a device that allows wireless devices to connect to a wired network using Wi-Fi."},
    "Firewall": {"Description": "A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on security rules created by the network administrator."},
    "Router": {"Description": "A router is a networking device that forwards data packets between computer networks."},
    "Server": {"Description": "In computing, a server is a piece of computer hardware or software that provides functionality for other programs or devices, called clients."},
    "Switch": {"Description": "A switch is networking hardware that connects devices on a computer network by using packet switching to receive and forward data to the destination device."},
    "Unspecified device": {"Description": "Unspecified device"}
}

def Hardware_Presentation():
    with dpg.window(label="Hardware Selection", width=200, height=400, pos=(0, 100), no_close=True, no_resize=True, no_title_bar=False,no_move=True,tag="Hardware_Selection_window",):
        for i, hardware in enumerate(Hardware_Selection.keys()):
            unique_id = f"{hardware}"
            dpg.add_button(label=hardware, tag=unique_id, pos=(0, 50 * (i + 1)), width=200, height=50, callback=lambda h=hardware: Info_Window(h))
def Info_Window(hardware):
    if dpg.does_item_exist("Hardware_Info_Window"):
        dpg.delete_item("Hardware_Info_Window")
    with dpg.window(label="Hardware Info", width=600, height=100, pos=(500, 0), no_close=True, no_resize=True, no_title_bar=False, no_move=True):
        dpg.add_text(f"Information about {hardware}:")
        dpg.add_text(Hardware_Selection[hardware]["Description"], wrap=580)
        
def Tutorial_Step_3():
    del globals()["Hardware_Selection"]
    dpg.delete_item("tutorial_step_2")
    dpg.delete_item("Hardware_Selection_window")
    dpg.delete_item("Hardware_Info_Window")
    with dpg.window(label="Tutorial Step 3", tag="tutorial_step_3", width=500, height=300, no_resize=True, no_collapse=True, no_move=True, no_close=True,pos=(600,450)):
        dpg.add_text("This is the third step of the tutorial.")
        dpg.add_text("Here you learn how to add hardware to the topology.")
        dpg.add_text("Once you click on a hardware button a window will open confirming whether you want to add the hardware to the topology,Try adding some now.", wrap=480)
        dpg.add_button(label="Next", callback=lambda: Tutorial_Step_4())
        dpg.add_button(label ="Return to Main Menu", callback=lambda: Finish_Tutorial())
        setup_variables_and_constants()
        Hardware_Selection_Setup()
    

def Tutorial_Step_4():
    dpg.delete_item("tutorial_step_3")
    with dpg.window(label="Tutorial Step 4", tag="tutorial_step_4", width=700, height=300, no_resize=True, no_collapse=True, no_move=True, no_close=True,pos=(600,450)):
        dpg.add_text("This is the fourth step of the tutorial.")
        dpg.add_text("Here you learn how to edit the topology.")
        dpg.add_text("You can add or remove connections between devices.", wrap=600)
        dpg.add_text("select a device in the drop down of the edit window , then  you would proceed by selecting if you wish to create or remove a connection.", wrap=600)
        dpg.add_button(label="End", callback=lambda: Finish_Tutorial())
        Fake_Adjacency_Hotbar_Editor()
        
        # Fake Adjacency_Hotbar_Editor for tutorial purposes
def Fake_Adjacency_Hotbar_Editor():
    with dpg.window(label="Adjacency Hotbar Editor",width=300, height=400, pos=(200, 100), no_resize=True, no_close=True, no_title_bar=False, no_move=True, tag="Adjacency_Hotbar_Editor"):
            dpg.add_text("Edit Hardware Properties")
            dpg.add_button(label="Add Connection")
            dpg.add_button(label="Remove Connection")
            dpg.add_text("Hardware Properties:")
            dpg.add_text(f"Name: example hardware")
            dpg.add_text(f"Type: example")  # Display the type of the hardware object
            dpg.add_text(f"Available Ports: 100")
            dpg.add_text(f"Total Ports: 100")
            dpg.add_text(f"ID: ExampleID123")  # Example ID, replace with actual ID if available}")
            dpg.add_button(label="Close", callback=lambda: dpg.delete_item("Edit_Hardware_Window"))  # Close the edit window        

def Finish_Tutorial():#deletes all the windows in the viewport and returns to the main menu
    if dpg.does_item_exist("tutorial_step_1"):
        dpg.delete_item("tutorial_step_1")
    if dpg.does_item_exist("tutorial_step_2"):
        dpg.delete_item("tutorial_step_2")
    if dpg.does_item_exist("tutorial_step_3"):
        dpg.delete_item("tutorial_step_3")
    if dpg.does_item_exist("tutorial_step_4"):
        dpg.delete_item("tutorial_step_4")
    dpg.delete_item("tutorial_window")
    dpg.delete_item("Hardware_Selection_window")
    dpg.delete_item("Hardware_Info_Window")
    dpg.delete_item("Adjacency_Hotbar_Editor")
    dpg.delete_item("Edit_Hardware_Window")
    dpg.delete_item("Hardware_Info_Window")
    dpg.delete_item("Adjacency_Hotbar")
    dpg.delete_item("Menus")  
    dpg.show_item("main_window")  # Hide the main window to return to the main menu
    if dpg.does_item_exist("New_Hardware"):
        dpg.delete_item("New_Hardware")

def close_variables_and_constants():
    del globals()["Adjacency_List"]
    del globals()["Adjacency_Hardware_List"]
    del globals()["Hardware_Name_List"]
    del globals()["loaded"]




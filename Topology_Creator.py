
import dearpygui.dearpygui as dpg
import Adjacency_Storage as adj_store
import Hardware_Objects as hw_obj
from File_Handling import *
from Nodes import *




def Menu_Buttons(button_data, window_width, window_height, vertical_spacing):#does the layout
    button_width = (window_width - (len(button_data) + 1) * vertical_spacing) // len(button_data)  
    button_height = window_height // 2  
    y_position = (window_height - button_height) // 2  

    for i, (label, callback) in enumerate(button_data):
        x_position = vertical_spacing + i * (button_width + vertical_spacing) 
        dpg.add_button(label=label, width=button_width, height=button_height, pos=(x_position, y_position), callback=callback)

def Menus_Setup(): 
    with dpg.window(label="Menus", width=500, height=100, pos=(0, 0), no_close=True, no_resize=True, no_move=True, no_collapse=True, no_title_bar=True,tag="Selection_Menus"):
        Menu_Buttons(Menu_buttons_selection(), 500, 100, 10)

def Menu_buttons_selection():
    Menu_buttons_selection = [
        ("Hardware", lambda: Hardware_Selection_Setup()),
        ("Edit", lambda: Adjacency_Hotbar_Editor()),
        ("Save", lambda: File_Details(Collate_Variables())),
        ("Main Menu", lambda: Return_To_Main_Menu()),
        ("Visualize", lambda: create_visual_representation(Adjacency_List)),
        ]
    return Menu_buttons_selection
def Hardware_Selection_Setup():
    if dpg.does_item_exist("Hardware_Selection_window"):
        dpg.delete_item("Hardware_Selection_window")
    else:
        Hardware_Selection_Window()

def Hardware_Selection_Window():
    with dpg.window(label="Hardware Selection", width=200, height=400, pos=(0, 100), no_close=True, no_resize=True, no_title_bar=False,no_move=True,tag="Hardware_Selection_window",):
        Hardware_Selection_Buttons()

def Hardware_Selection_Buttons():
    Hardware_Selection = Get_Hardware_Selection()
    for i, hardware in enumerate(Hardware_Selection.keys()):#this loops through the dictionary by using the index and the key
        unique_id = f"{hardware}"
        dpg.add_button(label=hardware, tag=unique_id, pos=(0, 50 * (i + 1)), width=200, height=50, callback=lambda h=hardware: Hardware_Selection_Buttons_Functions(h))

def Hardware_Selection_Buttons_Functions(hardware):
    if dpg.does_item_exist("New_Hardware"):
        dpg.delete_item("New_Hardware")
    if dpg.does_item_exist("Hardware_Info_Window"):
        dpg.delete_item("Hardware_Info_Window")
    Hardware_Selection_Info_Window(hardware)
    if not dpg.does_item_exist("Adjacency_Hotbar"):
        Adjacency_Hotbar_Setup()
    else:
        Update_Adjacency_Hotbar()
    Add_Hardware_To_Adjacency_List(hardware)

def Hardware_Selection_Info_Window(hardware):
    info_window_tag = "Hardware_Info_Window"
    if not dpg.does_item_exist(info_window_tag):
        with dpg.window(label="Hardware Info", width=600, height=100, pos=(500, 0), no_close=True, no_resize=True, no_title_bar=False, no_move=True, tag=info_window_tag):
            dpg.add_text(f"Information about {hardware}:", wrap=580, tag="Hardware_Info_Text")
            Hardware_Selection = Get_Hardware_Selection()
            info = list(Hardware_Selection[hardware])[0]  
            dpg.add_text(info, wrap=580, tag="Hardware_Info_Details")
    else:
        dpg.set_value("Hardware_Info_Text", f"Information about {hardware}:")
        info = list(Hardware_Selection[hardware])[0]  # 
        dpg.set_value("Hardware_Info_Details", info)


def Check_Hardware_To_Add(Hardware_Type,ports,Hardware_ID):
    if Hardware_Type == "Access Point":
        Hardware_Name_List.append(hw_obj.Access_Point(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
    elif Hardware_Type == "Firewall":
        Hardware_Name_List.append(hw_obj.Firewall(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
    elif Hardware_Type == "Router":
        Hardware_Name_List.append(hw_obj.Router(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
    elif Hardware_Type == "Server":
        Hardware_Name_List.append(hw_obj.Server(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
    elif Hardware_Type == "Switch":
        Hardware_Name_List.append(hw_obj.Switch(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
    elif Hardware_Type == "Unspecified device":
        Hardware_Name_List.append(hw_obj.Unspecified_device(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID, Available_Ports=ports, Total_Ports=ports))



def Add_Hardware_To_Adjacency_List(Hardware_Type):
    Access_Point_ID = len(Hardware_Name_List) + 1
    Hardware_Name = (Hardware_Type + "_" + str(Access_Point_ID))  
    if Hardware_Type != "Unspecified device":
        Not_Unspecified_To_Adjacency_List(Hardware_Type,Hardware_Name)
    elif Hardware_Type == "Unspecified device":#if the hardware type is unspecified device, then create a window to add the hardware with a slider for total ports
        Unspecified_To_Adjacency_List(Hardware_Type,Hardware_Name)

def Not_Unspecified_To_Adjacency_List(Hardware_Type,Hardware_Name):
    with dpg.window(label="New_Hardware", width=300, height=400, pos=(200, 100), no_resize=True, no_title_bar=True, no_move=True, tag="New_Hardware"):
            dpg.add_text(Hardware_Type +" Name:")
            dpg.add_text(Hardware_Name)
            dpg.add_button(label="Add " + Hardware_Type, callback=lambda: [Hardware_Into_List(Hardware_Type,0,Hardware_Name), dpg.delete_item("New_Hardware")])  
            dpg.add_button(label="Cancel", callback=lambda: dpg.delete_item("New_Hardware")) 

def Unspecified_To_Adjacency_List(Hardware_Type,Hardware_Name):
    Access_Point_ID = len(Hardware_Name_List) + 1
    with dpg.window(label="New_Unspecified_Device", width=300, height=400, pos=(200, 100), no_resize=True, no_title_bar=True, no_move=True, tag="New_Hardware"):
            dpg.add_text("Unspecified Device Name:")
            dpg.add_text(Hardware_Name)
            slider_tag = f"Unspecified_Device_Total_Ports_{Access_Point_ID}"
            dpg.add_slider_int(label="Total Ports", default_value=10, min_value=1, max_value=100, tag=slider_tag)
            dpg.add_button(label="Add Unspecified Device", callback=lambda: [Hardware_Into_List(Hardware_Type, dpg.get_value(slider_tag),Hardware_Name), dpg.delete_item("New_Hardware")])  # Pass the value of the slider and close window
            dpg.add_button(label="Cancel", callback=lambda: dpg.delete_item("New_Hardware"))  

def Hardware_Into_List(Hardware_Type,Ports,Hardware_Name):
        Check_Hardware_To_Add(Hardware_Type,Ports,Hardware_Name)  
        Adjacency_Hardware_List.append(Hardware_Name)
        Adjacency_List.Add_Node(Hardware_Name)
        Update_Adjacency_Hotbar()



def Update_Adjacency_Hotbar():
    if dpg.does_item_exist("Adjacency_Hotbar"):
        dpg.delete_item("Adjacency_Hotbar")
    with dpg.window(label="Adjacency List", width=600, height=400, pos=(500, 100), no_resize=True, no_close=True, no_title_bar=False, no_move=True, no_collapse=True, tag="Adjacency_Hotbar",horizontal_scrollbar=True):
        dpg.add_text(Adjacency_List.__str__())

def Adjacency_Hotbar_Setup():
    global Adjacency_List
    Adjacency_List = adj_store.WeightedUndirectedAdjacencyList(Adjacency_Hardware_List)
    with dpg.window(label="Adjacency List", width=600, height=400, pos=(500, 100), no_resize=True, no_close=True, no_title_bar=False, no_move=True, no_collapse=True, tag="Adjacency_Hotbar"):
        Adjacency_text = Adjacency_List.__str__()
        dpg.add_text(Adjacency_text)



def Populate_Hotbar_Editor():
    dpg.add_text("Select Hardware:")
    dpg.add_combo(label = "", items=Adjacency_List.Get_Nodes(), width=180, tag="hardware_combo")
    dpg.add_button(label="Edit Hardware", callback=lambda: Edit_Hardware(dpg.get_value("hardware_combo")))
    dpg.add_text("Warning: Removing hardware will delete all connections associated with it.")
    dpg.add_button(label="Remove Selected Hardware", callback=lambda: [Adjacency_List.Remove_Node(dpg.get_value("hardware_combo")), Update_Adjacency_Hotbar(), dpg.delete_item("Adjacency_Hotbar_Editor")])
    dpg.add_button(label="Close", callback=lambda: dpg.delete_item("Adjacency_Hotbar_Editor"))

def Adjacency_Hotbar_Editor():
    try:
        if dpg.does_item_exist("Adjacency_Hotbar_Editor"):
            dpg.delete_item("Adjacency_Hotbar_Editor")
        else:
            with dpg.window(label="Adjacency Hotbar Editor", width=300, height=400, pos=(200, 100), no_resize=True, no_close=True, no_title_bar=False, no_move=True, tag="Adjacency_Hotbar_Editor"):
                Populate_Hotbar_Editor()
    except:
        dpg.delete_item("Adjacency_Hotbar_Editor")
        with dpg.window(label="Error", width=300, height=200, pos=(250, 200), no_resize=True, no_title_bar=True, no_move=True, tag="Error Popup"):
            dpg.add_text("No hardware in the topology to edit.")
            dpg.add_button(label="Close", callback=lambda: dpg.delete_item("Error Popup"))





def Edit_Hardware(Hardware_Name):  # Ensure Hardware_Name is defined

    def Refresh_Edit_Window():
        if dpg.does_item_exist("Edit_Hardware_Window"):
            dpg.delete_item("Edit_Hardware_Window")
        Edit_Hardware(Hardware_Name)

    def Check_Hardware_To_Add_Connection(Hardware_Name,Connected_Hardware,type_val):
        Hardware_Number = int(Hardware_Name.split("_")[-1]) 
        Connected_Hardware_Number = int(Connected_Hardware.split("_")[-1]) 

        if Hardware_Name_List[Hardware_Number - 1].Get_Available_Ports() > 0 and Hardware_Name_List[Connected_Hardware_Number - 1].Get_Available_Ports() > 0:
            Hardware_Name_List[Hardware_Number - 1].Use_Port()  
            Hardware_Name_List[Connected_Hardware_Number - 1].Use_Port()  
            Adjacency_List.Add_Edge(Hardware_Name, Connected_Hardware, type_val)
            Update_Adjacency_Hotbar() 
            dpg.delete_item("Add_Connection_Window") 
        else:
            with dpg.popup("Error Popup"):
                dpg.add_text("Not enough available ports to add connection.")
                dpg.add_button(label="Close", callback=lambda: [dpg.delete_item("Error Popup"), dpg.delete_item("Add_Connection_Window")])


    def Check_Hardware_To_Remove_Connection(Hardware_Name,Connected_Hardware):
        Hardware_Number = int(Hardware_Name.split("_")[-1])  
        Connected_Hardware_Number = int(Connected_Hardware.split("_")[-1])  #
        if Hardware_Name_List[Hardware_Number - 1].Get_Available_Ports() != Hardware_Name_List[Hardware_Number - 1].Get_Total_Ports() and Hardware_Name_List[Connected_Hardware_Number - 1].Get_Available_Ports() != Hardware_Name_List[Connected_Hardware_Number - 1].Get_Total_Ports():
            Hardware_Name_List[Hardware_Number - 1].Free_Port()
            Hardware_Name_List[Connected_Hardware_Number - 1].Free_Port()
            Adjacency_List.Remove_Edge(Hardware_Name, Connected_Hardware)
            Update_Adjacency_Hotbar()
        else:
            with dpg.popup("Error Popup"):
                dpg.add_text("Cannot remove connection, ports are already free.")
                dpg.add_button(label="Close", callback=lambda: dpg.delete_item("Error Popup"))

    def Add_Connection(Hardware_Name):
        with dpg.window(label=("Add Connection to ", Hardware_Name), width=300, height=400, pos=(200, 100), no_resize=True, no_title_bar=True, no_move=True,tag="Add_Connection_Window"):
            dpg.add_text("Add Connection")
            dpg.add_text(f"Add a connection to {Hardware_Name}")
            combo_tag = f"connect_to_{Hardware_Name}"
            radio_tag = f"connection_type_{Hardware_Name}"
            dpg.add_combo(label="Connecting to:", items=Adjacency_List.Get_Nodes_Not_Connected(Hardware_Name), width=180, tag=combo_tag)
            dpg.add_combo(label="Connection Type:",items=["Wired", "Wireless"],width = 180, tag=radio_tag)

            def Confirm_Connection_Callback():#callback - a callback function is a function that is passed as an argument to another function and is executed after some kind of event
                selected_hardware = dpg.get_value(combo_tag)
                connection_type = dpg.get_value(radio_tag)
                type_val = None
                if connection_type == "Wired":
                    type_val = 1
                elif connection_type == "Wireless":
                    type_val = 2
                if selected_hardware and type_val is not None:
                    Check_Hardware_To_Add_Connection(Hardware_Name, selected_hardware,type_val) 
                    Refresh_Edit_Window()

            dpg.add_button(label="Confirm Connection", callback=lambda:Correct_Connection_Check(dpg.get_value(combo_tag),Hardware_Name))
            dpg.add_button(label="Cancel", callback=lambda: dpg.delete_item("Add_Connection_Window"))
            

        def Correct_Connection_Check(Selected_hardware,Hardware_name):
            stop = False
            selected_hardware_Type = Selected_hardware.split("_")[0]  
            hardware_Type = Hardware_name.split("_")[0]  
            if hardware_Type == "Access Point" and selected_hardware_Type not in ["Router", "Switch", "unspecified device"]:
                with dpg.window(label="Error", width=300, height=200, pos=(250, 200), no_resize=True, no_title_bar=True, no_move=True, tag="Error Popup"):
                    dpg.add_text("Access Points can only connect to Switches, Routers and unspecified devices.",wrap=280)
                    stop = True
                    dpg.add_button(label="Close", callback=lambda: [dpg.delete_item("Error Popup"),dpg.delete_item("Add_Connection_Window")])
            elif hardware_Type == "Firewall" and selected_hardware_Type not in ["Router", "Switch", "Server"]:
                with dpg.window(label="Error", width=300, height=200, pos=(250, 200), no_resize=True, no_title_bar=True, no_move=True, tag="Error Popup"):
                    dpg.add_text("Firewalls can only connect to Routers or Switches or servers.",wrap=280)
                    stop = True
                    dpg.add_button(label="Close", callback=lambda: [dpg.delete_item("Error Popup"),dpg.delete_item("Add_Connection_Window")])
            elif hardware_Type == "Router" and selected_hardware_Type not in ["Router", "Switch", "Firewall"]:
                with dpg.window(label="Error", width=300, height=200, pos=(250, 200), no_resize=True, no_title_bar=True, no_move=True, tag="Error Popup"):
                    dpg.add_text("Routers can only connect to other Routers, Switches or Firewalls.",wrap=280)
                    stop = True
                    dpg.add_button(label="Close", callback=lambda: [dpg.delete_item("Error Popup"),dpg.delete_item("Add_Connection_Window")])
            elif hardware_Type == "Server" and selected_hardware_Type not in ["Switch", "Firewall"]:
                with dpg.window(label="Error", width=300, height=200, pos=(250, 200), no_resize=True, no_title_bar=True, no_move=True, tag="Error Popup"):
                    dpg.add_text("Servers can only connect to Switches or Firewalls .",wrap=280)
                    stop = True
                    dpg.add_button(label="Close", callback=lambda: [dpg.delete_item("Error Popup"),dpg.delete_item("Add_Connection_Window")])
            elif hardware_Type == "Switch" and selected_hardware_Type not in ["Router", "Access Point", "Server", "Firewall", "unspecified device"]:
                with dpg.window(label="Error", width=300, height=200, pos=(250, 200), no_resize=True, no_title_bar=True, no_move=True, tag="Error Popup"):
                    dpg.add_text("Switches can only connect to Routers or Access Points or Servers or Firewalls or Unspecified devices.",wrap=280)
                    stop = True
                    dpg.add_button(label="Close", callback=lambda: [dpg.delete_item("Error Popup"),dpg.delete_item("Add_Connection_Window")])
            elif hardware_Type == "Unspecified device":
                pass
            if stop == True:
                return
            Confirm_Connection_Callback()

    def Remove_Connection(Hardware_Name):
        with dpg.window(label=("Removing connection from ", Hardware_Name), width=300, height=400, pos=(200, 100), no_resize=True, no_title_bar=True, no_move=True, tag="Remove_Connection_Window"):
            dpg.add_text("Remove Connection")
            dpg.add_text(f"Remove a connection from {Hardware_Name}")
            combo_tag = f"remove_connection_combo_{Hardware_Name}"
            dpg.add_combo(label="Removing from:", items=Adjacency_List.Get_Edges(Hardware_Name), width=180, tag=combo_tag)

            def confirm_removal_callback():
                selected_hardware = dpg.get_value(combo_tag)
                if selected_hardware:
                    Check_Hardware_To_Remove_Connection(Hardware_Name, selected_hardware)
                    Refresh_Edit_Window()
            dpg.add_button(label="Confirm Removal", callback=confirm_removal_callback)
            dpg.add_button(label="Cancel", callback=lambda: dpg.delete_item("Remove_Connection_Window"))

    if dpg.does_item_exist("Edit_Hardware_Window"):
        dpg.delete_item("Edit_Hardware_Window")
    else:
        
        Hardware_Number = int(Hardware_Name.split("_")[-1])
        Hardware_Type = Hardware_Name.split("_")[0]
        with dpg.window(label=("Edit ",Hardware_Name), width=300, height=400, pos=(200, 100), no_resize=True, no_title_bar=True, no_move=True, tag="Edit_Hardware_Window"):
            dpg.add_text("Edit Hardware Properties")
            dpg.add_button(label="Add Connection", callback=lambda: Add_Connection(Hardware_Name))
            dpg.add_button(label="Remove Connection", callback=lambda: Remove_Connection(Hardware_Name))
            dpg.add_text("Hardware Properties:")
            dpg.add_text(f"Name: {Hardware_Name}")
            dpg.add_text(f"Type: {Hardware_Type}")  
            dpg.add_text(f"Available Ports: {Hardware_Name_List[Hardware_Number - 1].Get_Available_Ports() }")
            dpg.add_text(f"Total Ports: {Hardware_Name_List[Hardware_Number - 1].Get_Total_Ports() }")
            dpg.add_text(f"ID: {Hardware_Name_List[Hardware_Number - 1].Get_Hardware_ID() }")
            dpg.add_button(label="Close", callback=lambda: dpg.delete_item("Edit_Hardware_Window"))  

def Get_Ports(node_name):
    Hardware_Number = int(node_name.split("_")[-1])  # 
    return Hardware_Name_List[Hardware_Number - 1].Get_Total_Ports()

def setup_variables_and_constants():
    global Hardware_Name_List, Adjacency_Hardware_List,loaded
    Hardware_Name_List = []
    Adjacency_Hardware_List = []
    loaded = False
    


def New_File_Run():
    dpg.hide_item("main_window")
    setup_variables_and_constants()
    Menus_Setup()

def Get_Hardware_Selection():
    return{
        "Access Point": {"An access point is a device that allows wireless devices to connect to a wired network using Wi-Fi."},
        "Firewall": {"A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on security rules created by the network administrator."},
        "Router": {"A router is a networking device that forwards data packets between computer networks."},
        "Server": {"In computing, a server is a piece of computer hardware or software that provides functionality for other programs or devices, called clients."},
        "Switch": {"A switch is networking hardware that connects devices on a computer network by using packet switching to receive and forward data to the destination device."},
        "Unspecified device": {"Unspecified device"}}


def Return_To_Main_Menu():#deletes all of the windows in the viewport and runs the new file
    with dpg.window(label="Confirm Return", width=800, height=600, pos=(0, 0), no_resize=True, no_close=True, no_title_bar=True, no_move=True,tag="Confirm Return"):
        dpg.add_text("Are you sure you want to return to the main menu?")
        dpg.add_text("This will delete all unsaved changes.")
        dpg.add_text("Click Yes to return to the main menu or No to stay in the current window.")
        dpg.add_button(label="Yes", callback=lambda: (Confirmed_Return_To_Main_Menu()))
        dpg.add_button(label="No", callback=lambda: dpg.delete_item("Confirm Return"))
    
    def Confirmed_Return_To_Main_Menu():
        Clear_New_File_Viewport()
        dpg.show_item("main_window")
    

def Collate_Variables():
    try:
        variables = {
            "Adjacency_List": Adjacency_List.To_List_Of_Lists(),  # Convert the adjacency list to a list of lists
        }
        return variables
    except:
        with dpg.window(label="Error", width=300, height=200, pos=(250, 200), no_resize=True, no_title_bar=True, no_move=True, tag="Error Popup"):
            dpg.add_text("Nothing in the topology to save.")
            dpg.add_button(label="Close", callback=lambda: dpg.delete_item("Error Popup"))
            return None

def Clear_New_File_Viewport():
    # Delete all relevant windows if they exist
    for tag in [
        "Confirm Return", "Selection_Menus", "Hardware_Selection_window", "Adjacency_Hotbar","Adjacency_Hotbar_Editor", "Edit_Hardware_Window", "Hardware_Info","New_Hardware", "Add_Connection_Window", "Remove_Connection_Window", "Hardware_Info_Window",]:
        if dpg.does_item_exist(tag):
            dpg.delete_item(tag)
    global Hardware_Name_List, Adjacency_Hardware_List, Adjacency_List
    Hardware_Name_List.clear()
    Adjacency_Hardware_List.clear()
    if 'Adjacency_List' in globals():
        del Adjacency_List

def Loaded_Setup(variables):
    global Hardware_Name_List, Adjacency_Hardware_List, Adjacency_List
    Adjacency_List = variables[0]
    Adjacency_Hardware_List = variables[1]
    Hardware_Name_List = variables[2]
    Menus_Setup()
    Update_Adjacency_Hotbar()


def File_Details(variables):
    if variables is None:
        return
    with dpg.window(label="Save File", tag="save_file_window", width=450, height=200, no_resize=True, no_collapse=True, no_move=True, no_close=True):
        dpg.add_text("If the file name already exists it will overwrite the existing file.",wrap=350)
        dpg.add_text("Enter the name of the file to save:")
        dpg.add_input_text(label="File Name", tag="file_name_input", default_value="New_Topology")
        dpg.add_button(label="Save", callback=lambda: Check_File(dpg.get_value("file_name_input"), variables))
        dpg.add_button(label="Cancel", callback=lambda: dpg.delete_item("save_file_window"))



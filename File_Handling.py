
import ast
import dearpygui.dearpygui as dpg
import os
import Topology_Creator as nf
import Hardware_Objects as hw
import Adjacency_Storage as adj_store


def Globalise_Current_File_Location(file_name):
    global current_file
    current_file = file_name


def Convert_Dict_To_String(variable_dict):
    variable_string = ""
    for key, value in variable_dict.items():
        variable_string += f"{key}: {value}\n"
    return variable_string

def Check_File(file_name, variables):
    file_name = file_name +".txt"  # Ensure the file name has a .txt extension
    if "." in dpg.get_value("file_name_input"):
            with dpg.popup("Error", modal=True):
                dpg.add_text("Please do not include file extensions in the file name.")
                dpg.add_button(label="OK", callback=lambda: dpg.delete_item("Error"))
    elif dpg.get_value("file_name_input") == Get_Current_File():##these elifs are not working
        Confirm_Overwrite(dpg.get_value("file_name_input"),variables)
        
    elif (dpg.get_value("file_name_input")+".txt") in os.listdir("NEA/Saved_Topologies"):
        Confirm_Overwrite(dpg.get_value("file_name_input"),variables)
    else:
        Save_As(variables, file_name)


def Save_As(variables, File_Name):  # uses x to create a new file. all files will be stored in the storage file(savedTopologies folder that will come with the program.
    File_Path ="NEA/Saved_Topologies"
    with open(os.path.join(File_Path,File_Name), "w") as f:
        f.write(Convert_Dict_To_String(variables))
        f.close()
    Globalise_Current_File_Location(File_Name)
    dpg.delete_item("save_file_window")

def Get_Current_File(): 
    if 'current_file' in globals():
        return current_file
    else:
        return None


def Update_Dictionary(File_Name,variables):
    File_Path ="NEA/Saved_Topologies"
    variables_string = Convert_Dict_To_String(variables)
    with open(os.path.join(File_Path,File_Name), "w") as f:
        f.write(variables_string)
        f.close()
    Globalise_Current_File_Location(File_Name)

def Confirm_Overwrite(file_Name,variables):
    with dpg.window(label="Confirm Overwrite", tag="confirm_save_window", width=300, height=200):
        dpg.add_text(f"The file '{file_Name}' already exists or the input file name is invalid. Do you want to overwrite it?")
        dpg.add_button(label="Yes", callback=lambda: Overwrite_File(file_Name,variables))
        dpg.add_button(label="No", callback=lambda: dpg.delete_item("confirm_save_window"))

def Overwrite_File(file_Name,variables):
    try:
        Update_Dictionary(file_Name,variables)
        dpg.delete_item("confirm_save_window")
    except Exception as e:
        with dpg.popup("Error", modal=True):
            dpg.add_text(f"An error occurred while saving the file: {e}")
            dpg.add_button(label="OK", callback=lambda: dpg.delete_item("Error"))
        dpg.delete_item("confirm_save_window")





def Load_File_Text():
    dpg.delete_item("confirm_load_window")
    with dpg.window(label="Load File", tag="load_file_window", width=400, height=200, no_resize=True, no_collapse=True, no_move=True, no_close=True):
        dpg.add_text("Enter the name of the file to load:")
        dpg.add_combo(label="File Name", tag="file_name_input_load", items=Get_Files_In_Directory("NEA/Saved_Topologies"))
        dpg.add_button(label="Load", callback=lambda: Load_Contents(dpg.get_value("file_name_input_load")))

def Get_Files_In_Directory(directory):
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        return []

def Load_Contents(file_name):
    dpg.delete_item("load_file_window")
    with open(os.path.join("NEA/Saved_Topologies",file_name),"r") as f:
        file_content = f.read()
        f.close()
    Convert_String_To_Globals(file_content)


def Convert_String_To_List(file_content):
    variable_dict = {}
    lines = Clean_Txt(file_content)
    for line in lines:
        if ": " in line:
            key, value = line.split(": ", 1)
            variable_dict[key.strip()] = ast.literal_eval(value.strip())
    return variable_dict

def Clean_Txt(file_content):
    if not isinstance(file_content, str):
        file_content = str(file_content)
    lines = file_content.split("\n")
    lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines and strip whitespace
    return lines

def Variable_Dict_To_Globals(variable_dict):
    global dictionary
    dictionary = variable_dict  # Store the entire dictionary globally for reference
    list_of_lists = dictionary.get("Adjacency_List")
    if list_of_lists is not None:
        Globalise_Variables(list_of_lists)  # Use .get to avoid KeyError if "Adjacency_List" is not present
    

def Convert_String_To_Globals(file_content):
    variable_dict = Convert_String_To_List(file_content)
    Variable_Dict_To_Globals(variable_dict)
    
    
# Call the function to continue loading the file after converting the string to globals

def Load_File():
    dpg.hide_item("main_window")
    Confirm_Load()


def Globalise_Variables(list_of_lists):
    global Adjacency_List ,Adjacency_Hardware_List, Hardware_Name_List
    Adjacency_Hardware_List = Get_Stored_Nodes(list_of_lists)
    Adjacency_List = adj_store.WeightedUndirectedAdjacencyList(Adjacency_Hardware_List)
    Hardware_Name_List=Hardware_Name_List_Load(list_of_lists)
    Connect_Nodes_From_List(list_of_lists)
    Continue_Load()


def Hardware_Name_List_Load(Adjacency_List):
    global Hardware_Name_List
    Hardware_Name_List = []
    for sublist in Adjacency_List:
        Hardware_ID = str(sublist[0])
        connections_used = len(sublist[1])
        hardware_type = Hardware_ID.split("_")[0]
        if hardware_type != "Unspecified device":
            Check_Hardware_To_Load(hardware_type,Hardware_ID)
            Load_Used_Ports(connections_used)
        else:
            total_ports = sublist[3]
            Hardware_Name_List.append(hw.Unspecified_device(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID,Total_Ports=total_ports,Available_Ports=total_ports))
            Load_Used_Ports(connections_used)

def Load_Used_Ports(used_ports):
    Hardware_Number = len(Hardware_Name_List) - 1
    for i in range(used_ports):
        Hardware_Name_List[Hardware_Number].Use_Port()

def Check_Hardware_To_Load(Hardware_Type,Hardware_ID):
    if Hardware_Type == "Access Point":
        Hardware_Name_List.append(hw.Access_Point(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
    elif Hardware_Type == "Firewall":
        Hardware_Name_List.append(hw.Firewall(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
    elif Hardware_Type == "Router":
        Hardware_Name_List.append(hw.Router(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
    elif Hardware_Type == "Server":
        Hardware_Name_List.append(hw.Server(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
    elif Hardware_Type == "Switch":
        Hardware_Name_List.append(hw.Switch(len(Hardware_Name_List) + 1, Hardware_Name=Hardware_ID))
                


def Get_Stored_Nodes(list_of_lists):
    stored_list = []
    for sublist in list_of_lists:
        stored_list.append(str(sublist[0]))
    return stored_list  
    

def Connect_Nodes_From_List(list_of_lists):
    for sublist in list_of_lists:
        node1 = str(sublist[0])
        for i in range(len(sublist[1])):
            node2 = str(sublist[1][i])
            weight = int(sublist[2][i])
            Adjacency_List.Add_Edge(node1, node2, weight)




def Confirm_Load():
    with dpg.window(label="Confirm Load", tag="confirm_load_window", width=300, height=200):
        dpg.add_text("Are you sure you want to load a file? This will overwrite the current session.",wrap = 250 )
        dpg.add_button(label="Yes", callback=lambda: Convert_String_To_Globals(Load_File_Text()))
        dpg.add_button(label="No", callback=lambda: Cancel_Load())

def Continue_Load():
    global loaded
    loaded = True
    variables = [Adjacency_List,Adjacency_Hardware_List,Hardware_Name_List]
    nf.Loaded_Setup(variables)


def Cancel_Load():
    dpg.delete_item("confirm_load_window")
    dpg.show_item("main_window")

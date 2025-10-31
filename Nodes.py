import dearpygui.dearpygui as dpg

def Load_Adjacency_List(adjacency_List):
    Add_nodes_from_Adjacency_List(adjacency_List)
    Connect_nodes_from_Adjacency_List(adjacency_List)

def no_connection():
    pass
def Connect_nodes_from_Adjacency_List(adjacency_list):
    nodes = adjacency_list.Get_Nodes()
    for node in nodes:
        connect_nodes = adjacency_list.Get_Connected_Nodes(node)
        for connect_node in connect_nodes:
            if node < connect_node:  # Prevent duplicate links
                dpg.add_node_link(f"{node}_in", f"{connect_node}_in",)

def Add_nodes_from_Adjacency_List(adjacency_list):
    nodes = adjacency_list.Get_Nodes()
    length = len(nodes)
    index = 0
    for node in nodes:
        index += 1
        # Arrange nodes in a grid for clear visualization, avoiding overlap with connections
        spacing_x = 250  # Increased spacing to reduce overlap
        spacing_y = 180
        grid_cols = 4  # Fewer columns for more vertical space
        pos_y = (index // 5) * spacing_y + 50
        pos_x = (index % 5) * spacing_x + 50
        dpg.add_node(label=node, tag=node, pos=[pos_x, pos_y])
        with dpg.node_attribute(label="In", tag=f"{node}_in", parent=node):
            dpg.add_text("Port")

def Reset_Visuals(adjacency_list):
    nodes = adjacency_list.Get_Nodes()
    try:
        for node in nodes:
            dpg.delete_item(node)
        if dpg.does_item_exist("Node_Editor"):
            dpg.delete_item("Node_Editor")
        if dpg.does_item_exist("Node_Tests_Window"):
            dpg.delete_item("Node_Tests_Window")
    except:
        if dpg.does_item_exist("Node_Editor"):
            dpg.delete_item("Node_Editor")
        if dpg.does_item_exist("Node_Tests_Window"):
            dpg.delete_item("Node_Tests_Window")

def create_visual_representation(adjacency_list):
    if dpg.does_item_exist("Node_Tests_Window"):
        dpg.delete_item("Node_Tests_Window")
    else:
        with dpg.window(label="Node Tests", width=800, height=800,tag="Node_Tests_Window",no_close=True):
            dpg.add_button(label="Close", callback=lambda: Reset_Visuals(adjacency_list))
            with dpg.node_editor(minimap=True, minimap_location=2, callback=lambda: no_connection, tag="Node_Editor"):
                Load_Adjacency_List(adjacency_list)

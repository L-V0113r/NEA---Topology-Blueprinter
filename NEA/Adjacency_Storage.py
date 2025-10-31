import Topology_Creator as nf

class WeightedUndirectedAdjacencyList:
    def __init__(self, _Node_Names):
        if not isinstance(_Node_Names, list) or not all(isinstance(Name, str) for Name in _Node_Names):
            raise ValueError("Node names must be a list of strings.")
        self._Node_Names = list(_Node_Names)
        self._Node_Index = {Name: Index for Index, Name in enumerate(self._Node_Names)}#maps node names to their indices
        self._Index_To_Name = {Index: Name for Name, Index in self._Node_Index.items()}#maps indices to their node names
        self._Adjacency_List = {Name: [] for Name in self._Node_Names}#maps node names to a list of tuples (neighbor, weight) neighbor is the connected node name, weight is the edge weight

    def Add_Node(self, Node_Name):
        if not isinstance(Node_Name, str):
            raise TypeError("Node name must be a string.")
        if Node_Name in self._Node_Index:
            raise ValueError("Node already exists.")
        self._Node_Names.append(Node_Name)
        self._Node_Index[Node_Name] = len(self._Node_Names) - 1
        self._Index_To_Name[self._Node_Index[Node_Name]] = Node_Name
        self._Adjacency_List[Node_Name] = []

    def Remove_Node(self, Node_Name):
        if not isinstance(Node_Name, str):
            raise TypeError("Node name must be a string.")
        # Remove all edges to this node
        neighbour_list = self._Adjacency_List[Node_Name][:]
        for neighbor, _ in neighbour_list:
            self.Remove_Edge(Node_Name, neighbor)#remove edges first

        del self._Adjacency_List[Node_Name]
        self._Node_Names.remove(Node_Name)
        del self._Node_Index[Node_Name]#recalibrates the index withe the node removed
        self._Node_Index = {name: i for i, name in enumerate(self._Node_Names)}
        self._Index_To_Name = {i: name for name, i in self._Node_Index.items()}

    def To_List_Of_Lists(self):
        Result = []
        for Node_Name, Neighbors in self._Adjacency_List.items():
            Node_Type = Node_Name.split("_")[0]#splits before the underscore
            Connections = [Neighbor[0] for Neighbor in Neighbors]
            Weights = [Neighbor[1] for Neighbor in Neighbors]
            if Node_Type != "Unspecified device":
                Result.append([Node_Name, Connections, Weights])
            else:
                try:
                    Ports = nf.Get_Ports(Node_Name)
                    Result.append([Node_Name, Connections, Weights, Ports])
                except Exception:
                    Result.append([Node_Name, Connections, Weights, []])
        return Result

    def Add_Edge(self, Node_1, Node_2, Weight):
        if not isinstance(Node_1, str) or not isinstance(Node_2, str):
            raise TypeError("Node names must be strings.")
        if not isinstance(Weight, int):
            raise TypeError("Edge weight must be an integer.")
        if Node_1 not in self._Node_Index or Node_2 not in self._Node_Index:
            raise ValueError("Both nodes must be in the graph.")
        if Weight not in [1, 2]:
            raise ValueError("Edge weight must be 1 or 2.")
        if any(Neighbor == Node_2 for Neighbor, _ in self._Adjacency_List[Node_1]):
            return
        self._Adjacency_List[Node_1].append((Node_2, Weight))
        self._Adjacency_List[Node_2].append((Node_1, Weight))

    def Remove_Edge(self, Node_1, Node_2):
        if not isinstance(Node_1, str) or not isinstance(Node_2, str):
            raise TypeError("Node names must be strings.")
        if Node_1 not in self._Node_Index or Node_2 not in self._Node_Index:
            raise ValueError("Both nodes must be in the graph.")
        self._Adjacency_List[Node_1] = [Neighbor for Neighbor in self._Adjacency_List[Node_1] if Neighbor[0] != Node_2]
        self._Adjacency_List[Node_2] = [Neighbor for Neighbor in self._Adjacency_List[Node_2] if Neighbor[0] != Node_1]

    def Get_Nodes(self):
        return self._Node_Names

    def Get_Other_Nodes(self, Node_Name):
        return [Name for Name in self._Node_Names if Name != Node_Name]
    
    def Get_Connected_Nodes(self, Node_Name):
        if not isinstance(Node_Name, str):
            raise TypeError("Node name must be a string.")
        if Node_Name not in self._Node_Index:
            raise ValueError("Node does not exist.")
        return [Neighbor for Neighbor, _ in self._Adjacency_List[Node_Name]]

    def Get_Nodes_Not_Connected(self, Node_Name):
        if not isinstance(Node_Name, str):
            raise TypeError("Node name must be a string.")
        if Node_Name not in self._Node_Index:
            raise ValueError("Node does not exist.")
        Connected_Nodes = {Neighbor for Neighbor, _ in self._Adjacency_List[Node_Name]}
        return [Name for Name in self._Node_Names if Name != Node_Name and Name not in Connected_Nodes]

    def Get_Other_Connected_Nodes(self, Node_Name):
        if not isinstance(Node_Name, str):
            raise TypeError("Node name must be a string.")
        if Node_Name not in self._Node_Index:
            raise ValueError("Node does not exist.")
        Connected_Nodes = {Neighbor for Neighbor, _ in self._Adjacency_List[Node_Name]}
        return [Name for Name in Connected_Nodes if Name != Node_Name]

    def Get_Edges(self, Node_Name):
        if not isinstance(Node_Name, str):
            raise TypeError("Node name must be a string.")
        if Node_Name not in self._Node_Index:
            raise ValueError("Node does not exist.")
        return [Neighbor for Neighbor, _ in self._Adjacency_List[Node_Name]]

    def __str__(self):
        list_of_lists = self.To_List_Of_Lists()
        result = ""
        for sublist in list_of_lists:
            connections = ", ".join(str(item) for item in sublist[1])
        
            result += f"{sublist[0]} : {connections}\n"
        return result
            

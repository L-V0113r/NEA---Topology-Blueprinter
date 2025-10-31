class Hardware:
    def __init__(self,_Hardware_ID:int,_Hardware_Type,_Hardware_Name :str):
        self._Hardware_ID = _Hardware_ID
        self._Hardware_Type = _Hardware_Type
        self._Hardware_Name = _Hardware_Name
        

    def Get_Hardware_Name(self):#this method returns the name of the hardware
        try:
            return self._Hardware_Name
        except AttributeError:
            return "Hardware Name not found"

        
    def Get_Hardware_Type(self):#this method returns the type of hardware, for example, router, switch, server etc,It gets it from the Hardware_Type object
        try:
            return self._Hardware_Type
        except AttributeError:
            return "Hardware Type not found"
    
    def Get_Hardware_ID(self):#this method returns the ID of the hardware
        try:
            return self._Hardware_ID
        except AttributeError:
            return "Hardware ID not found"
    
    def Get_Hardware_Info(self):#this method returns the information about the hardware
        try:
            return self._Hardware_Type.Hardware_Info
        except AttributeError:
            return "Hardware Info not found"

    def Get_Available_Ports(self):#this method returns the number of ports available on the hardware,
        try:
            return self._Hardware_Type.Hardware_Ports.Numb_Ports_Available
        except AttributeError:
            return 0

    def Get_Total_Ports(self):#this method returns the total number of ports on the hardware,
        try:
            return self._Hardware_Type.Hardware_Ports.Numb_Ports_Available
        except AttributeError:
            return "No Ports Available"
    
    def Use_Port(self):#this method is used to use a port on the hardware
        try:
            if self._Hardware_Type.Hardware_Ports.Numb_Ports_Available > 0:
                self._Hardware_Type.Hardware_Ports.Numb_Ports_Available -= 1
            else:
                return "No Ports Available"
        except AttributeError:
            return "No Ports Available"
    
    def Free_Port(self):#this method is used to free a port on the hardware
        try:
            if self._Hardware_Type.Hardware_Ports.Numb_Ports_Available < self.Hardware_Type.Hardware_Ports.Numb_Ports_Available:
                self._Hardware_Type.Hardware_Ports.Numb_Ports_Available += 1
            else:
                return "No Ports Available"
        except AttributeError:
            return "No Ports Available"
    
    def create_wired_connection(self,Connection1,Connection2):#this method is used to create a wired connection between two hardware objects
        Wired_Connection1 = Wired_Connection(Connection1,Connection2)
        Wired_Connection1.Create_Connection()
    
    def create_wireless_connection(self,Connection1,Connection2):#this method is used to create a wireless connection between two hardware objects
        Wireless_Connection1 = Wireless_Connection(Connection1,Connection2)
        Wireless_Connection1.Create_Connection()
    
    def remove_wired_connection(self,Connection1,Connection2):
        Wired_Connection1 = Wired_Connection(Connection1,Connection2)
        Wired_Connection1.Remove_Connection()
    
    def remove_wireless_connection(self,Connection1,Connection2):
        Wireless_Connection1 = Wireless_Connection(Connection1,Connection2)
        Wireless_Connection1.Remove_Connection()


class Hardware_Type():#this class is used to store the information about the hardware
    def __init__(self,_Hardware_Type,_Hardware_Info,Hardware_Ports):
        self._Hardware_Type = str(_Hardware_Type)
        self._Hardware_Info = str(_Hardware_Info)
        self.Hardware_Ports = Hardware_Ports

    def Get_Hardware_Type(self):#this method returns the type of hardware
        try:
            return self._Hardware_Type
        except AttributeError:
            return "Hardware Type not found"

    def Get_Hardware_Info(self):#this method returns the information about the hardware
        try:
            return self._Hardware_Info
        except AttributeError:
            return "Hardware Info not found"
        
    def Get_Hardware_Ports(self):#this method returns the Hardware_Ports object
        try:
            return self.Hardware_Ports
        except AttributeError:
            return "Hardware Ports not found"


#Hardware Type collates the information about the hardware, for example, what it does, what it is used for etc, and the number of ports available and the total number of ports
class Hardware_Ports():#this class is used to store the number of ports available and the total number of ports on the hardware
    def __init__(self,Numb_of_Ports,Numb_Ports_Available):
        self.Numb_of_Ports = Numb_of_Ports
        self.Numb_Ports_Available = Numb_Ports_Available



class Router(Hardware):
    def __init__(self,Hardware_ID,Hardware_Name):
        Hardware_Info_Router = "A router is a networking device that forwards data packets between computer networks."
        Hardware_Type_Router = Hardware_Type("Router",Hardware_Info_Router,Hardware_Ports(255,255))#this creates a Hardware_Type object using other objects so all the information is stored in one object
        super().__init__(Hardware_ID,  Hardware_Type_Router,Hardware_Name)

    


class Firewall(Hardware):
    def __init__(self,Hardware_ID,Hardware_Name):#one connection to switch and one to isp(cable to outside)  need make only those connections possible for firewall
        Hardware_Info_Firewall = "A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on security rules created by the network administrator."
        Hardware_Type_Firewall = Hardware_Type("Firewall",Hardware_Info_Firewall, Hardware_Ports(2,2))
        super().__init__(Hardware_ID,  Hardware_Type_Firewall,Hardware_Name)
    


class Switch(Hardware):
    def __init__(self,Hardware_ID,Hardware_Name):
        Hardware_Info_Switch = "A network switch is networking hardware that connects devices on a computer network by using packet switching to receive and forward data to the destination device."
        Hardware_Type_Switch = Hardware_Type("Switch",Hardware_Info_Switch,Hardware_Ports(48,48))
        super().__init__(Hardware_ID,  Hardware_Type_Switch,Hardware_Name)




class Server(Hardware):
    def __init__(self,Hardware_ID,Hardware_Name):
        Hardware_Info_Server = "In computing, a server is a piece of computer hardware or software that provides functionality for other programs or devices, called clients."
        Hardware_Type_Server = Hardware_Type("Server",Hardware_Info_Server,Hardware_Ports(1000,1000))
        super().__init__(Hardware_ID,  Hardware_Type_Server,Hardware_Name)

    



class Unspecified_device(Hardware):
    def __init__(self,Hardware_ID,Hardware_Name,Total_Ports,Available_Ports):
        Hardware_Info_Unspecified_device = "Unspecified device"
        Hardware_Ports_Unspecified_device = Hardware_Ports(Total_Ports,Available_Ports)#user changes number of ports
        Hardware_Type_Unspecified_device = Hardware_Type("Unspecified device",Hardware_Info_Unspecified_device,Hardware_Ports_Unspecified_device)
        super().__init__(Hardware_ID,  Hardware_Type_Unspecified_device,Hardware_Name)

class Access_Point(Hardware):
    def __init__(self,Hardware_ID,Hardware_Name):
        Hardware_Info_Access_Point = "An access point is a device that allows wireless devices to connect to a wired network using Wi-Fi."
        Hardware_Ports_Access_Point = Hardware_Ports(255,255)
        Hardware_Type_Access_Point = Hardware_Type("Access Point",Hardware_Info_Access_Point,Hardware_Ports_Access_Point)
        super().__init__(Hardware_ID,  Hardware_Type_Access_Point,Hardware_Name)


#the above classes are the children of the Hardware class, they inherit the methods and attributes of the Hardware class and use the Hardware_Type and Hardware_Ports classes to get the information about the hardware and the ports available and the total number of ports


class Connections:#this class is used to create a connection between two hardware objects, it uses the Connection_Type object to get the type of connection and the Connection_Info object to get the information about the connection
    def __init__(self,Connection1,Connection2,Connection_Type):#check all functions before ending
        self._Connection1 = Connection1
        self._Connection2 = Connection2
        self.__delattr__Connection_Type = Connection_Type

    def Get_Connection_Type(self):##this method returns the type of connection,
        try:
            return self.Connection_Type.Connection_Type
        except AttributeError:
            return "Connection Type not found"

    def Get_Connected_Hardware(self):##this method returns the names of the hardware that are connected by this connection
        try:
            return self.Connection1.Hardware_Name,self.Connection2.Hardware_Name
        except AttributeError:
            return "Hardware not found"

    def Get_Connection_Info(self):
        try:
            return self.Connection_Type.Connection_Info
        except AttributeError:
            return "Connection Info not found"

    def Create_Connection(self):#this method is used to create a connection between two hardware objects
        try:
            if self.Connection1.Get_Available_Ports() > 0 and self.Connection2.Get_Available_Ports() > 0:#Need to create these functions,linking to hardware and connections together,Hardware(port availability etc)
                self.Connection1.Use_Port()
                self.Connection2.Use_Port()
            else:
                return "No Ports Available"
        except AttributeError:
            return "No Ports Available"

    def Remove_Connection(self):
        try:
            self.Connection1.Free_Port()
            self.Connection2.Free_Port()
        except AttributeError:
            return "No Ports Available"


class Connection_details():
    def __init__(self,Connection_Type,Connection_Info):
        self._Connection_Type = Connection_Type
        self._Connection_Info = Connection_Info

class Wired_Connection(Connections):
    def __init__(self, Connection1, Connection2):
        Wired_Connection_Info = "A wired connection is a connection that uses cables to connect devices, for example, Ethernet."
        Wired_Connection_Type = Connection_details("Wired Connection", Wired_Connection_Info)
        super().__init__(Connection1, Connection2, Wired_Connection_Type)

class Wireless_Connection(Connections):
    def __init__(self, Connection1, Connection2):
        Wireless_Connection_Info = "A wireless connection is a connection that uses radio waves to connect devices, for example, Wi-Fi."
        Wireless_Connection_Type = Connection_details("Wireless Connection", Wireless_Connection_Info)
        super().__init__(Connection1, Connection2, Wireless_Connection_Type)

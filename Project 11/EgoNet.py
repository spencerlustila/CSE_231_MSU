import Circle

class EgoNet:
    def __init__(self,ego,ego_net_features):
        self.__ego = ego #Represents the Ego node for the EgoNet. type - Node object
        self.__social_network = {} # Represents the social network graph. type - dict where key = Node object 			        and value = list of Node objects key is connected to
        self.__social_network[ego] = set() # Represents the social network graph. type - dict where key = Node object 			        and value = list of Node objects key is connected to
        self.__alter_node_count = 0 # Represents the total number of alter nodes connected to our Ego
        self.__circles = {} #Represents the circles formed in our EgoNet. type - dict where key = circle name		      and value = list of Node objects in the circle
        self.__ego_net_features = ego_net_features # Represents the features for our Ego Net. type - dict where key = feature			           position in feature file (type - int) and value = tuple of feature name and			          feature id. This does not contain Feature objects but just strings. 


    def get_alter_node(self,node_id):
        network = self.__social_network #gets the network from the self
        for i in network.keys(): #loop that runs through the network keys
            id_num = i.get_id() #gets the id from the key
            if id_num == node_id: #checks if the id is the same as the node id
                return(i) #returns the key
        return None #returns none
        
    def get_ego(self):
        return self.__ego #returns the ego from the self
    
    def get_circle_names(self):
        circle_names = [] #list of circle names
        for i in self.__circles.keys(): #loop that runs through the circle keys
            circle_names.append(i) #adds the name to the list
        return circle_names #returns the list

    def get_circle(self, circle_name):
        return self.__circles.get(circle_name) #gets the informatoin of the circle from the self
    
    def get_alters(self):
        nodes = set() #variable for the nodes set
        values = self.__social_network.get(self.__ego) #gets the values from the social network of the ego net
        for i in values: #loop that runs through the values of the social network
            nodes.add(i) #adds the value to the node set
        return nodes #returns the node set

    def get_alter_node_count(self):
        network = self.__social_network #gets the social network
        for i in network.keys(): #runs through the kets of the network
            if i.get_id() == self.__ego.get_id(): #checks if the id is the is the same as the ego id
                return len(network.get(i)) #gets the length of all the nodes

    def get_ego_net_features(self):
        return self.__ego_net_features #gets the feature information and returns

    def get_ego_net_feature(self, feature):
        return self.__ego_net_features[feature] #returns a specific feature and returns it

    def get_feature_pos(self, feature_name, feature_id):
        result = (feature_name, feature_id) #creates a tuple of the name and id
        features = self.__ego_net_features #gets the features
        for i in features: #loops through the features
            if features.get(i) == result: #checks if the feature is the same as the result
                return i #returns the feature
        return None #returns none
    
    def get_alter_connections(self, alter):
        return self.__social_network.get(alter) #gets the alter node from the social network
    
    def add_circle(self, circle_name, alters):
        self.__circles[circle_name] = Circle.Circle(circle_name, alters) #creates the circle and adds it to the circle dict
    
    def add_connection_between_alters(self,alter1,alter2):
        if self.__social_network.get(alter1) == None: #checks if the alter is in the network
            self.__social_network[alter1] = set() #adds the alter to the network
            self.__social_network[alter1].add(self.__ego) #connects it to the ego
            self.__social_network[alter1].add(alter2) #connects the other alter to it
        else:
            self.__social_network[alter1].add(alter2) #connects the other alter to the alter
        if self.__social_network.get(alter2) == None: #checks if the alter is in the network
            self.__social_network[alter2] = set() #adds the alter to the network
            self.__social_network[alter2].add(self.__ego) #connects it to the ego
            self.__social_network[alter2].add(alter1) #connects the other alter to it
        else:
            self.__social_network[alter2].add(alter1) #connects the other alter to the alter

    def add_alter_node(self, alter):
        self.__social_network[self.__ego].add(alter) #adds the alter to the social network of the ego
        if self.__social_network.get(alter) == None: #checks if the node is in the social network
            self.__social_network[alter] = set() #adds it and sets the value as a set
            self.__social_network[alter].add(self.__ego) #connects the new alter to the ego
            friend_count = self.__alter_node_count #gets the friend count
            friend_count += 1 #increases the friend count
            self.__alter_node_count = friend_count #updates the friend count
        else:
            self.__social_network[alter].add(self.__ego) #connects the alter to the ego

    def __eq__(self,other):
        '''True if all attributes are equal.'''
        return (self.__ego == other.__ego)\
            and (self.__social_network == other.__social_network) \
            and (self.__alter_node_count == other.__alter_node_count) \
            and (self.__circles == other.__circles) \
            and (self.__ego_net_features == other.__ego_net_features)
            
    def __str__(self):
        '''Returns a string representation for printing.'''
        st = f"Ego: {self.__ego}\n"
        st+= f"Social Network: {self.__social_network}\n"
        st+= f"Circles: {self.__circles}"
        return st

    __repr__ = __str__

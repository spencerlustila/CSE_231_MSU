##############################################################################
# CSE 231 proj11
#
# Algorithm 
#   Program for Displaying and Calculating the Ego nets of users based on
#       files
#   Calculates the size of Ego Nets
#   Calculates the EI of the EI Index
#   Calculates the Efficiency of the Ego Net
#   Finds the similar features of the Ego Nets
##############################################################################

from EgoNet import EgoNet
from Node import Node
from Feature import Feature
from Circle import Circle
from operator import itemgetter

def get_ego_net_files():
    y1 = "_ego_features.txt"
    y2 = "_ego_net_features.txt"
    y3 = "_alters_features.txt"
    y4 = "_ego_net_connections.txt"
    y5 = "_circles.txt"
    x = input("Enter user id to generate EgoNet: ")
    while True:
        try:
            fp1 = open(x+y1)
            fp2 = open(x+y2)
            fp3 = open(x+y3)
            fp4 = open(x+y4)
            fp5 = open(x+y5)

            return (int(x),fp1,fp2,fp3,fp4,fp5)

        except FileNotFoundError:
            print("File not found for ego_id: ",x)
            x = input("Enter user id to generate EgoNet: ")

def get_ego_net_features(fp):
    """

    Creats a dictionary of the features of the Ego Net

    fp: The file containing the ego net info

    Returns:  The dictionary with ints as keys, and the values are the features

    """
    ego_net_features_dict = {} #dictionary that will be returned
    for i in fp: #loop that will get the key from the file
        split_line = i.split() #splits the line by the spaces
        key ="" #sets the key to an empty string
        for n in i: #loop that runs through the elemtns of the line
            if n == " ": #checks if the element is a space
                break #loops the for loop
            else: #the element is not a space
                key += n #adds the number to the key
        key = int(key) #converts the str to int
        new_line = i[2:] #makes the rest of the line a new variable
        new_line = new_line.strip() #takes off the estra spaces and new line elements from line
        split_line = new_line.split(";") #splits the line by the semi-colon
        feature = split_line[-1] #gets the feature number from the list
        feature_split = feature.split() #splits the list
        feature_id = feature_split[-1] #get the id
        split_line.pop() #removes the id from the list
        feature_name = "" #variable for the feature name
        if split_line[-1].lower() == "id": #checks if the last element is an id
            split_line.pop() #removes the id from the list
            feature_name = "_".join(split_line) #combines the rest of the list as a string with a hyphen
        else: #the last element of the list is an id
            feature_name = "_".join(split_line) #joins the list into a string with a hyphen
        ego_net_features_dict[key] = (feature_name, (feature_id)) #adds the files to the dictionary
    return ego_net_features_dict #returns the dictionary

def add_ego_net_features_to_ego(ego, ego_feature_file, ego_net_features):
    '''Reads a one-line file of features for the ego node'''
    #print(ego_feature_file)
    line_list = ego_feature_file.readline().split()    # read one line
    #print(line_list)
    #print(ego_net_features)
    # i is the index, digit is the value
    for i,digit in enumerate(line_list):
        # in order to add a feature we must create a Feature instance
        #print(i)
        #print(digit)
        ego.add_feature(i,Feature(ego_net_features[i][1], ego_net_features[i][0],int(digit)))
    return ego
    
def add_alters_to_ego_net(ego_net,alter_features_file,ego_net_features):
    """

    Adds the alternet nodes to the ego net

    ego_net:             The ego net from the add ego net features to ego function
    alter_features_file: file with id, and the true false values for the features
    ego_net_features:    The ego net from get_ego_net_features

    Returns:  The the altered ego net

    """

    for i in alter_features_file: #loop that runs thourhg the file with the new alters
        split_line = i.split() #splits the line into a list
        for n,j in enumerate(split_line): #loop for running though the elements of the string
            split_line[n] = (j) #sets the values to what they were
        id_num = split_line.pop(0) #removes the id from the list
        node = Node(int(id_num), len(split_line)) #creates a node variable
        for i, digit in enumerate(split_line): #loop for running through the list
            node.add_feature(i,Feature(ego_net_features[i][1], ego_net_features[i][0],int(digit))) #adds the features to the node
        ego_net.add_alter_node(node) #adds the alternate node to the ego node
    return ego_net #returns the ego net

def add_connections_to_ego_net(ego_net,connections_file):
    """

    Connects the ego alters based on the file

    ego_net:          The ego net from the add ego net features to ego function
    connections_file: the file of alter connections

    Returns:  The updated ego net

    """
    for i in connections_file: #loop that runs through all the lines of the connect file
        split_line = i.split() #takes the line and splits it into a list
        alter1 = ego_net.get_alter_node(int(split_line[0])) #sets the alter connect variable
        alter2 = ego_net.get_alter_node(int(split_line[1])) #sets the alter connect variable
        ego_net.add_connection_between_alters(alter1,alter2) #connects the nodes
    return ego_net #returns the ego net

def add_circles_to_ego_net(ego_net,circles_file):
    """

    Adds the circles to the ego net based on the circles file

    ego_net:      The ego net from the add ego features to ego function
    circles_file: the file containing the different circles the nodes are a part of

    Returns:  The updated ego node

    """
    for i in circles_file: #loop that runs through the circles file
        split_line = i.split() #splits the line into a list
        name = split_line.pop(0) #pops the name of the list
        alters_set = set() #set for the alters
        for n in split_line: #loop that runs through the elements of the list
            j = ego_net.get_alter_node(int(n)) #gets the node for the ego net
            alters_set.add(j) #adds the node to the set
        ego_net.add_circle(name, alters_set) #adds the circles to the ego net
    return ego_net #returns the ego net

def calculate_circle_similarity(ego_net,circle_name):
    """

    Creats a dictionary of of the circle

    ego_net:     The ego net from the add ego features to ego function
    circle_name: the name of the circle that needs to be put into the dictionary

    Returns:  The dictionary the dictionary of the cirlce

    """
    circle_similarity = {} #dictionary that will be filled with circle info
    features = ego_net.get_ego_net_features() #gets the features of the ego net
    for key, value in features.items(): #loop for running through the features
        circle_similarity[key] = 0 #adds the key to the dictionary
    cir = ego_net.get_circle(circle_name) #collects the circle variable
    alters = cir.get_alters() #gets the alters from the circle
    for i in alters: #loop that runs through the alters
        feat = i.get_features() #gets the features fro mthe alters
        for n,ch in enumerate(feat): #loop that runs through the features
            value = circle_similarity.get(n) #gets the value of the dictionary
            if ch.get_feature_value() == None: #checks if the value is empty
                pass #passes
            else: #the value is not empty
                value += ch.get_feature_value() #adds the feature info to the value
            circle_similarity[n] = value #changes the value of the dictionary
    return circle_similarity #returns the circle similarity dictionary

def calculate_ego_E_I_index(ego_net,feature_name,feature_id):
    """

    Calculates the EI Index

    ego_net:      The ego net from the add ego features to ego function
    feature_name: the feature to analyze
    feature_id:   the id of the feature

    Returns:  the number of the EI index

    """
    feature_index = ego_net.get_feature_pos(feature_name, feature_id) #gets the position of the feature
    alters = ego_net.get_alters() #gets the alters from the ego net
    i = 0 #variable to hold the feature value
    for n in alters: #loop to run through the alters
        feature_value = n.get_feature_value(feature_index) #gets the feautre value from the index
        i += feature_value #adds the feature value to the variable i
    e = ego_net.get_alter_node_count() - i #calculates the e
    return (e-i)/(e+i) #calculates and returns the ei value

def calculate_ego_net_effective_size(ego_net):
    """

    Calculates the effective size of the ego net

    ego_net: The ego net from the add ego features to ego function

    Returns:  Returns the effective size

    """
    count = ego_net.get_alter_node_count() #gets the count
    print(count)
    connections = 0 #connections variable
    alters = ego_net.get_alters() #gets the alters
    print(alters)
    for i in alters: #loop that runs through the alters
        connections += ((len(ego_net.get_alter_connections(i))-1)/1) #calculates the connections
    return count - (connections/count) #calculates and returns the effective size

def calculate_ego_net_efficiency(ego_net):
    """

    Calculates the efficiency of the ego net

    ego_net: The ego net from the add ego features to ego function

    Returns:  The efficiency of the ego net

    """
    effective_size = calculate_ego_net_effective_size(ego_net) #gets the effective size of the ego net
    count = ego_net.get_alter_node_count() #gets the count of the ego net
    return effective_size/count #calculates the efficiency

def print_choices():
    print("Choices for Ego Net calculation: ")
    print("1 - Top 5 similar features in a circle")
    print("2 - Calculate effective size of Ego Net")
    print("3 - Calculate circle E/I index")
    print("4 - Calculate Ego Net efficiency")
    print("q/Q - Quit ")

def main():
    ego_id,ego_feature_file,ego_net_features_file,alter_features_file,connections_file,circles_file=get_ego_net_files()
    ego_net_features = get_ego_net_features(ego_net_features_file)

    ego = Node(ego_id,len(ego_net_features))

    ego = add_ego_net_features_to_ego(ego,ego_feature_file,ego_net_features)

    FacebookNet = EgoNet(ego,ego_net_features)

    FacebookNet = add_alters_to_ego_net(FacebookNet,alter_features_file,ego_net_features)

    FacebookNet = add_connections_to_ego_net(FacebookNet,connections_file)

    FacebookNet = add_circles_to_ego_net(FacebookNet,circles_file)

    while True:
        print_choices()
        choice = input("Enter choice: ").strip()
        circle_names = FacebookNet.get_circle_names()
        if choice == "1":
            circle_name = input("Enter circle name to calculate similarity: ")
            circle_size = (FacebookNet.get_circle(circle_name).get_circle_size())

            if circle_name in circle_names:
                similarity_dict = calculate_circle_similarity(FacebookNet,circle_name)
            else:
                print("Circle name not in Ego Net's circles. Please try again!")
                continue
            similarity_dict = dict(sorted(similarity_dict.items(),key=itemgetter(1),reverse=True)[:5])

            for feature_pos in similarity_dict:
                feature_name_id = FacebookNet.get_ego_net_feature(feature_pos)
                feature_similarity = (similarity_dict[feature_pos])/(circle_size)
                print(f"Feature: {feature_name_id}")
                print(f"Feature Similarity in {circle_name}: {feature_similarity} \n")
            print()
        elif choice == '2':
            print(f"Effective size of the Ego Net is: {calculate_ego_net_effective_size(FacebookNet)}")
            print()
        elif choice == '3':
            feature_name = input("Enter feature name to calculate E/I index: ")
            feature_id = (input(f"Enter id for {feature_name} to calculate E/I index: "))
            e_i_index = calculate_ego_E_I_index(FacebookNet,feature_name,feature_id)
            if e_i_index < 0:
                print(f"Ego is more homophilic for {feature_name}_{feature_id} with an E/I index of {e_i_index}")
                print()
            else:
                print(f"Ego is more heterophilic for {feature_name}_{feature_id} with an E/I index of {e_i_index}")
                print()

        elif choice == '4':
            ego_net_efficiency = calculate_ego_net_efficiency(FacebookNet)
            print("The efficiency of the Ego Net is: {:.2f}%".format(100*ego_net_efficiency))
            print()

        elif choice in 'qQ':
            break
        else:
            print("Incorrect Choice. Please try again.")
            continue
    ego_feature_file.close()
    ego_net_features_file.close()
    alter_features_file.close()
    connections_file.close()

if __name__ == "__main__":
   main()

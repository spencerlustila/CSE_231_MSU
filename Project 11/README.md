# Project Title

Project 11

## Description

Utilizing Python, develop a program for displaying and calculating the Ego nets of users of Facebook based on provided files

### Function Descriptions

* **`get_ego_net_features(fp)`**
  * Creates a dictionary of the features of the Ego Net
  * fp: The file containing the ego net info
  * Returns:  The dictionary with ints as keys, and the values are the features
    
* **`add_ego_net_features_to_ego(ego, ego_feature_file, ego_net_features)`**
  * Reads a one-line file of features for the ego node
    
* **`add_alters_to_ego_net(ego_net,alter_features_file,ego_net_features)`**
  * Adds the alternet nodes to the ego net
  * `ego_net`:             The ego net from the add ego net features to ego function
  * `alter_features_file`: file with id, and the true false values for the features
  * `ego_net_features`:    The ego net from get_ego_net_features
  * Returns:  The the altered ego net
    
* **`add_connections_to_ego_net(ego_net,connections_file)`**
  * Connects the ego alters based on the file
  * ego_net:          The ego net from the add ego net features to ego function
  * connections_file: the file of alter connections
  * Returns:  The updated ego net
    
* **`add_circles_to_ego_net(ego_net,circles_file)`**
  * Adds the circles to the ego net based on the circles file
  * `ego_net`:      The ego net from the add ego features to ego function
  * `circles_file`: the file containing the different circles the nodes are a part of
  * Returns:  The updated ego node
    
* **`calculate_circle_similarity(ego_net,circle_name)`**
  * Creates a dictionary of of the circle
  * `ego_net`:     The ego net from the add ego features to ego function
  * `circle_name`: the name of the circle that needs to be put into the dictionary
  * Returns:  The dictionary the dictionary of the circle
    
* **`calculate_ego_E_I_index(ego_net,feature_name,feature_id)`**
  * Calculates the EI Index
  * `ego_net`:      The ego net from the add ego features to ego function
  * `feature_name`: the feature to analyze
  * `feature_id`:   the id of the feature
  * Returns:  the number of the EI index
    
* **`calculate_ego_net_effective_size(ego_net)`**
  * Calculates the effective size of the ego net
  * `ego_net`: The ego net from the add ego features to ego function
  * Returns:  Returns the effective size
    
* **`calculate_ego_net_efficiency(ego_net)`**
  * Calculates the efficiency of the ego net
  * `ego_net`: The ego net from the add ego features to ego function
  * Returns:  The efficiency of the ego net

## Author

Ankit Hegde : ankithegde@hotmail.com

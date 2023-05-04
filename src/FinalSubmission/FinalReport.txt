Abstract:
    This document presents a comprehensive overview of the AI components and features implemented in a project. The project involved 
    the development of an intelligent system to run a game that utilized AI components to enhance the game’s features. The following 
    topics are discussed in detail:
        1.	List of AI components in the project: This section provides a detailed description of the AI components used in the 
            project. The components include reflex learning agents, reinforcement learning, and utilizing a fitness function.
        2.	Problems Solved with the components: This section describes the problems solved by the AI components. The problems 
            range from data analysis and prediction to decision making and optimization.
        3.	Implemented features for the final submission of this project: This section lists the features implemented for the 
            final submission of the project. The implemented features include the added lose conditions, the movement restrictions, 
            and the attempt on connecting the GA system.
        4.	Individual AI feature implemented: This section describes the individual AI features implemented in the project which was 
            Dijksta’s algorithm. This includes what it does, what it improves in the game, and how it was implemented.
        5.	Instructions for running/testing these features: This section provides detailed instructions for running and testing the 
            implemented features.
        6.	ChatGPT's involvement with the project: This section explains the involvement of ChatGPT in the project. The section also 
            discusses the challenges and benefits of using ChatGPT in the project.
    Overall, this document provides a comprehensive overview of the AI components and features implemented in a project. It is intended 
    to help understand the progress made and the knowledge I’ve learned in the course that was used when implementing these features.

List of AI components in the project:


Problems solved with them components:


Implemented features for the final submission of this project:
    1.  Added lose conditon for both losing a fight against a bandit and for running out of gold.
    2.  Added a toll system that subtracts gold from the player's inventory each time they travel to a city (only works as intended
        when moving along the best route, if not moving along that route, the gold subtracted will be from the best path's toll costs).
    3.  Both pygame_human_player and pygame_ai_player will only move along paths to neighboring cities.
    4.  An attempt was made at implementing the GA system; however, it was not successful and instead of regenerating the map created
        in agent_enviroment it would only create and recreate the map from ga_cities. This is likely due to the functions in ga_cities
        being specifically associated with it's own map and would require further modifications in order to work with agent_enviroment's
        map.

Individual AI feature implemented:
    For this project, I implemented Dijkstra's algorithm to the pygame_ai_player's movement system and the pygame_human_player's 
    recommended action system. This both serves as an asset for the AI, allowing it to take the most efficient path to the destination
    city and prevents it from moving to random citys that do not have paths connecting them to the current city. As for the human side
    of the game, if pygame_human_player is used it will act similar to how many open world games utilize quest markers and paths to
    reach said markers, guiding the player along the most efficient route to their destination but not forcing them to take it. Currently
    the best path to take is only calculated once; however, with some modifications it can be calculated every time the player or AI
    visits a new city. This would act more similar to modern day systems such as quest trackers or even GPS devices. The functions for
    Dijkstra's algorithm were created in both pygame_ai_player and pygame_human_player through the Graph class (used for creating the
    game map of all of the cities and their edge values) and the functions recommendedAction, dijkstra_algorithm, print_result,
    translate_routes, and create_graph. These some of these functions and classes orginated from
    https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html and were modified or create to be compatible
    with the functions and variables we had already had such as the translate_routes function converting the coordinate tuples in routes
    with the city names so that the Graph class and its functions could properly understand and utilize our data. 

Instructions for running/testing these features:
    The file that should be run for testing is agent_enviroment. If you wish to test the AI with Dijkstra algorithm then be sure to
    use player = PyGameAIPlayer() on line 108 and use recommendedAction on line 133, commenting out player = PyGameAIPlayer() on line
    107 and select_action on line 132. If you with to instead manually test the forced movement features and part of Dijkstra's algorithm
    then be sure to do the opposite.

ChatGPT's involvement with the project:
    At first I utilized ChatGPT for creating the Dijkstra's algorithm; however, I found that either I wasn't giving the AI enough
    information to allow it to create the exact algorithm I needed or the AI was unable to create something as complex without being
    able to actively run code on its own. Regardless of the reason, I instead sought help with creating Dijkstra's algorithm from other
    sources due to my own time constraints and instead relied on ChatGPT to ocassionally creating smaller code segments that I could
    modify much quicker which includes the translate_routes function or lines 19-26 in pygame_human_player to determine what the
    neighboring cities were. ChatGPT was also used to assist in quickly creating an abstract for this project report when given the
    general topic for each part of the report. The given abstract was slightly modified to be less general and include more specifics
    related to the project.

Appendix:
    ChatGPT conversations:
        Creating the translate_routes function:
            Prompt:
            In python, I want to replace each tuple within a list with a string associated to that tuple. For example, I want to 
            replace [((40, 6), (416, 199))] with ['CityA','CityB']. How would I do this?

            Reply:
            You can create a dictionary where the keys are the tuples, and the values are the corresponding strings. Then you can 
            loop through the list and use the dictionary to replace each tuple with the associated string. Here's an example code:

                # create the dictionary
                city_dict = { (40, 6): 'CityA', (416, 199): 'CityB' }

                # the original list
                original_list = [((40, 6), (416, 199))]

                # replace each tuple with the associated string
                new_list = []
                for tup in original_list:
                    new_tup = []
                    for item in tup:
                        new_tup.append(city_dict[item])
                    new_list.append(new_tup)

                print(new_list) # output: [['CityA', 'CityB']]
            
            In this code, city_dict is the dictionary that maps the tuples to their corresponding strings. original_list is the 
            original list that contains tuples. The loop iterates through each tuple in the list, then iterates through each item 
            in the tuple, replaces the item with its associated string using the city_dict, and appends the string to a new list 
            new_tup. Finally, the new list new_list is created by appending the new tuples to it, which contain the strings instead 
            of the original tuples.
        
        Determining what the neighboring cities were:
            Prompt:
            When given a list of tuples that contain strings in the form of [("CityA","CityB"),("CityB","CityC")] and a specific 
            string, I want a list of the strings that are in a tuple with the given string. For example, if I provide the 
            list [("CityA","CityB"),("CityB","CityC"), ("CityC","CityD")] and the string "CityB", the returned list will 
            be ["CityA", "CityC"]. Create a python function that accomplishes this

            Reply:
            You can create a Python function to accomplish this task by iterating through the list of tuples and checking if the 
            given string is present in each tuple. If the string is present in a tuple, you can add the other string in that tuple 
            to a result list.

                Here's an implementation of this function:

                def find_cities(lst, target):
                    result = []
                    for cities in lst:
                        if target in cities:
                            result.append(cities[0] if cities[1] == target else cities[1])
                    return result

            Here, lst is the list of tuples and target is the specific string we are looking for. We initialize an empty list called 
            result to store the strings that are in a tuple with the given string. We then iterate through each tuple in the list 
            and check if target is present in that tuple using the in operator. If it is, we use a conditional statement to check 
            which of the two strings in the tuple is not the target string, and add that string to the result list. Finally, we 
            return the result list which contains the strings that are in a tuple with the given string.

        Create an abstract for this document:
            Prompt:
            Give me an example of an abstract for a document talking about these topics:
            1. List of AI components in the project
            2. Problems Solved with the components
            3. Implemented features for the final submission of this project
            4. Individual AI feature implemented
            5. Instructions for running/testing these features
            6. ChatGPT's involvement with the project

            Reply:
            Here is an example of an abstract for a document that covers the topics you listed:

            Title: AI Components and Features Implemented in a Project

            This document presents a comprehensive overview of the artificial intelligence (AI) components and features implemented 
            in a project. The project involved the development of an intelligent system to solve various problems related to a 
            specific domain. The following topics are discussed in detail:

            List of AI components in the project: This section provides a detailed description of the AI components used in the 
            project. The components include machine learning models, natural language processing algorithms, and decision-making 
            systems.

            Problems Solved with the components: This section describes the problems solved by the AI components. The problems 
            range from data analysis and prediction to decision making and optimization.

            Implemented features for the final submission of this project: This section lists the features implemented for the 
            final submission of the project. The features include data preprocessing, model training, and performance evaluation.

            Individual AI feature implemented: This section describes the individual AI features implemented in the project. The 
            features include sentiment analysis, recommendation systems, and clustering algorithms.

            Instructions for running/testing these features: This section provides detailed instructions for running and testing 
            the implemented features. The instructions include software requirements, data preparation, and step-by-step guides 
            for running the features.

            ChatGPT's involvement with the project: This section explains the involvement of ChatGPT in the project. ChatGPT was
            used as a conversational interface to interact with the system. The section also discusses the challenges and benefits 
            of using ChatGPT in the project.

            Overall, this document provides a comprehensive overview of the AI components and features implemented in a project. 
            It is intended for researchers and practitioners interested in developing intelligent systems for solving real-world 
            problems.
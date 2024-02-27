#This is a script to recommend a place to eat based off a user input name or food type
from restaurantData import *

#Reusing the Node and LnkedList classes built in previous exercises, this will form data structures we will be working with
#I might split this part off into separate files for simplicity sake later on
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value
    
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            string_list += str(current_node.value) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.next_node = next_node.get_next_node()
                    current_node = None
                else:
                    current_node = next_node

#*** Initialize the data ***
#All data that will be used here is kept in restaurantData.py for easy access
#This will build a Linked List of all the available types of cuisines.                
def build_cuisines_list():
    cuisines = LinkedList()
    for cuisine in types:
        cuisines.insert_beginning(cuisine)
    return cuisines

#This will build a list of lists where each type of cuisine (Asian, Mexican, Italian etc) will have a list of matching resturants associated.
def build_restaurants_list():
    restaurants = LinkedList()
    for cuisine in types:
        matching_restaurants = LinkedList()
        for restaurant in restaurant_data:
            if restaurant[0] == cuisine:
                matching_restaurants.insert_beginning(restaurant)
        restaurants.insert_beginning(matching_restaurants)
    return restaurants

cuisine_list = build_cuisines_list()
restaurant_list = build_restaurants_list()
selected_food = ""

#User interaction
print('What would you like to eat? Please enter a type of food: ')
user_input = str(input()).lower()

#Makes sure the user has input a valid type of food
hits = []
cuisine_list_head_node = cuisine_list.get_head_node()
while cuisine_list_head_node is not None:
    if str(cuisine_list_head_node.get_value()) == user_input:
        hits.append(cuisine_list_head_node.get_value())
    cuisine_list_head_node = cuisine_list_head_node.get_next_node()
    selected_food = user_input

print('Selected food type: ' + selected_food)

restaurant_list_head_node = restaurant_list.get_head_node()
while restaurant_list_head_node.get_next_node() is not None:
    sublist_head = restaurant_list_head_node.get_value().get_head_node()
    if sublist_head.get_value()[0] == selected_food:
        while sublist_head.get_next_node() is not None:
            print("--------------------------")
            print("Name: " + sublist_head.get_value()[1])
            print("Price: " + sublist_head.get_value()[2] + "/5")
            print("Rating: " + sublist_head.get_value()[3] + "/5")
            print("Address: " + sublist_head.get_value()[4])
            print("--------------------------\n")
            sublist_head = sublist_head.get_next_node()
    restaurant_list_head_node = restaurant_list_head_node.get_next_node()
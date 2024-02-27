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

#This will build a list of lists where each type of cuisine (Asian, Mexican, Italian etc) wioll have a list of matching resturants associated.
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


def welcome():
    print('What would you like to eat? Please enter a type of food: ')
    return


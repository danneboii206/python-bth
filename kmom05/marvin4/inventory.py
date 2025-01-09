'''
Functions for the inventory part of main.py
'''

def pick(bag,item,index=None):
    '''
    Adds elements to list by either appending or inserting in a specific index
    '''
    if index is not None:
        intdex = int(index)
        if intdex <= len(bag):
            bag.insert(intdex, item)
            print(f"Added {item} in index {index}")
        else:
            print(f"Error : Index {index} out of range")
    else:
        bag.append(item)
        print(f"Added {item}")
    return bag

def inventory(bag):
    '''
    Shows elements and amounts in list
    '''
    amount = len(bag)
    print(f"Bag includes {amount} elements, with the items being {bag}")
    return bag

def drop(bag, item):
    '''
    Removes element from list
    '''
    try:
        bag.remove(item)
        print(f"Successfully dropped {item}")
        return bag
    except ValueError:
        print(f"Error : {item} non existant")
        return bag

def swap(bag, item1, item2):
    '''
    Swaps an element for another element in respective index
    '''
    try:
        index1 = bag.index(item1)
        index2 = bag.index(item2)
        if index1 < index2:
            bag.pop(index1)
            bag.pop(index2 - 1)
            bag.insert(index1, item2)
            bag.insert(index2, item1)
            print(f"Swapped {item1} and {item2}")
        else:
            bag.pop(index2)
            bag.pop(index1 - 1)
            bag.insert(index2, item1)
            bag.insert(index1, item2)
            print(f"Swapped {item1} and {item2}")
        return bag
    except ValueError:
        if item1 not in bag and item2 not in bag:
            print(f"Error : {item1} and {item2} not in inventory")
        elif item1 not in bag:
            print(f"Error : {item1} not in inventory")
        else:
            print(f"Error : {item2} not in inventory")
        return bag

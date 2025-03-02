#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = [] 
        node = self.head 

        while node is not None:  

            items.append(node.data)  
            node = node.next 

        return items  

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
            Running time: O(n) because we must visit each node once."""

        count = 0
        node = self.head

        while node is not None:

            count += 1
            node = node.next

        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
            Running time: O(1) because we have direct access to the tail."""

        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        
        else: 
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) because we only update head reference."""

        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, matcher):
        """Return an item from this linked list if it is present.
            Best case running time: 0(1) if the item is at the head.
            Worst case running time: 0(n) if the item is at the tail or not found."""
        
        node = self.head

        while node is not None:
            print(f'Checkingnode: {node.data}, Matcher type: {type(matcher)}')
            if callable(matcher) and matcher(node.data):
                return node.data
            
            node = node.next

        return None

    def replace(self, old_item, new_item):
        """Replace an existing item with a new item in this linked list."""

        node = self.head
        
        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return
            node = node.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
            Best case running time: 0(1) if the item is at the head.
            Worst case running time: 0(n) if the item is at the tail or not found."""

        if self.is_empty():

            raise ValueError('Item not found: {}'.format(item))
        
        if self.head.data == item:
            
            self.head = self.head.next
            if self.head is None:
                self.tail = None

            return
        
        prev = None
        node = self.head
        while node is not None:
            if node.data == item:
                if node == self.tail:
                    self.tail = prev

                prev.next = node.next
                return
            
            prev = node
            node = node.next

        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
            Running time: O(n), where n is the total number of key-value pairs in the table."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
            Running time: O(n), where n is the total number of key-value pairs."""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n), where n is the total number of key-value pairs."""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
            Running time: O(n) where n is the total number of key-value pairs."""
        
        total_length = 0
        for bucket in self.buckets:
            total_length += len(bucket)

        return total_length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) on average, 0(n) in worst case due to collisions."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for stored_key, _ in bucket.items():
            if stored_key == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
            Running time: O(1) on average, 0(n) in worst case."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for stored_key, value in bucket.items():
            if stored_key == key:
                return value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
            Running time: O(1) on average, 0(n) in worst case due to collisions."""
        
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for stored_key, stored_value in bucket.items():
            
            if stored_key == key:
                bucket.delete(stored_key)
                bucket.append(key, value)
                return
        
        bucket.append(key, value)
        

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
            Running time: O(1) on average, 0(n) in worst case due to collisions."""
        
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        for stored_key, _ in bucket.items():
            if stored_key == key:
                bucket.delete(stored_key)
                return
        
        raise KeyError('Key not found: {}'.format(key))



def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()

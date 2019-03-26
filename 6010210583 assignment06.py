import random
import string
def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
class SinglyLinkedList(object):
    """Singly Linked List Class"""

    class Node(object):
        """A nested storage class representing list nodes."""
        def __init__(self,item, next=None):
            """Instantiaties a Node with default next of Node"""
            self.data = item
            self.next = next

    def __init__(self):
        """Constructs an empty list"""
        self._head = None

    def insertBegin(self, item):
        """Adds a new item to the beginning (head) of the list."""

        if self._head is None:
            self._head = SinglyLinkedList.Node(item)
        else:
            newNode = SinglyLinkedList.Node(item)
            newNode.next = self._head
            self._head = newNode

    def visitNode(self):
        curNode = self._head
        while curNode is not None: 
            print curNode.data,
            curNode = curNode.next
    def q(self):
        curNode = self._head
        while curNode is not None:
            if curNode.data == 'a':
                curNode.data = 'None'
            print curNode.data,
            curNode = curNode.next
if __name__ == '__main__':
   charlist = randomString(10)
   a = SinglyLinkedList()
   for i in charlist :
       a.insertBegin(i)
   a.visitNode()
   print ("\n")
   a.q()
#Russalan Malinee
#6010210583  

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    map1={}
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head==None:
            return None
        deeplistcurr=self.clone(head)
        curr=head
        while curr!=None:
            deeplistcurr.random=self.clone(curr.random)
            deeplistcurr.next=self.clone(curr.next)
            curr=curr.next
            deeplistcurr=deeplistcurr.next
        return self.map1[head]
        
    def clone(self,node):
        #map looks like {"node1":node1deepcopy, "node2":node2deepcopy}
        
        #if curr.next or curr.random is already in map1 we take out the deepcopy value corresponding to them and let the deeplistcu
        if node in self.map1:
            return self.map1[node]
        if node:
            newNode=Node(node.val,node.next,node.random)
            self.map1[node]=newNode
            return newNode

                
            
        

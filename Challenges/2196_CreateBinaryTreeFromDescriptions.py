# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        Map = {}
        children = set()
        for desc in descriptions:
            if desc[0] not in Map:
                Map[desc[0]] = {}
            if desc[2]:
                Map[desc[0]]['l'] = desc[1]
                children.add(desc[1])
            else:
                Map[desc[0]]['r'] = desc[1]
                children.add(desc[1])
        for key in list(Map.keys()):
            if 'node' not in Map[key]:
                Map[key]['node'] = TreeNode(val = key)
            if 'l' in Map[key]:     
                # check if l is not in Map
                if Map[key]['l'] not in Map:
                    # add l to Map, add attribute 'node' and create node
                    Map[Map[key]['l']] = {'node': TreeNode(val = Map[key]['l'])}
                else: # else l is in Map
                    # check if it does not have 'node'
                    if 'node' not in Map[Map[key]['l']]:
                        # create 'node' for it
                        Map[Map[key]['l']]['node'] = TreeNode(val = Map[key]['l'])
                # connect key.l to this node
                Map[key]['node'].left = Map[Map[key]['l']]['node']
            if 'r' in Map[key]:  
                if Map[key]['r'] not in Map:
                    Map[Map[key]['r']] = {'node': TreeNode(val = Map[key]['r'])}
                else:
                    if 'node' not in Map[Map[key]['r']]:
                        Map[Map[key]['r']]['node'] = TreeNode(val = Map[key]['r'])
                Map[key]['node'].right = Map[Map[key]['r']]['node']
        head = (set(Map.keys()) - children).pop()
        return Map[head]['node']

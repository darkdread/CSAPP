from typing import List

class Node():

  def __init__(self, value):
    self.value = value

def getDirectionOfPrevNode(node: Node) -> int:
  if (hasattr(node, "prev")):
    if (hasattr(node.prev, "left") and node.prev.left == node):
      return 0
    elif (hasattr(node.prev, "right") and node.prev.right == node):
      return 1
  return -1

def getRootNode(node: Node) -> Node:
  curr = node
  while(True):
    if hasattr(curr, "prev"):
      direction = getDirectionOfPrevNode(curr)
      curr = curr.prev
      if not hasattr(curr, "prev"):
        return curr
      if (getDirectionOfPrevNode(curr) != direction):
        return curr
    else:
      return curr

def getClosestNode(root: Node, value: int) -> Node:
  curr = root
  while(True):
    if (value < curr.value):
      if (hasattr(curr, "left")):
        curr = curr.left
        continue
    if (value > curr.value):
      if (hasattr(curr, "right")):
        curr = curr.right
        continue
    return curr


def isNodeValid(nodes: List[Node], node: Node, prevNode: Node, left: bool) -> bool:
  currentNode = prevNode
  rootNode = getRootNode(currentNode)
  closestNode = getClosestNode(rootNode, node.value)
  if (left):
    if (closestNode != prevNode):
      return False
    closestNode.left = node
  else:
    if (closestNode.value < getRootNode(rootNode).value and node.value > getRootNode(rootNode).value):
      getRootNode(rootNode).right = node
      node.prev = getRootNode(rootNode)
      return True
    else:
      closestNode.right = node
  
  node.prev = closestNode
  return True

def isValid(a: List[int]) -> bool:
  nodes: List[Node] = []
  for i in range(len(a)):
    node = Node(a[i])
    nodes.append(node)

    if (i == 0):
      continue

    prevNode = nodes[i - 1]
    if prevNode.value > node.value:
      if not isNodeValid(nodes, node, prevNode, True):
        return "NO"
    elif prevNode.value < node.value:
      if not isNodeValid(nodes, node, prevNode, False):
        return "NO"

    print(f"node:{node.value}, rootNode:{getRootNode(node).value}, closestNode:{node.prev.value}")

  return "YES"

# test1
print(isValid([30,10,9,15,13,17,31,32]))
# test2
print(isValid([30,10,9,15,13,17,31,32,40,35,45]))
# test3
print(isValid([30,35,29]))
# test4
print(isValid([10,3,2,7,5,6,15,20,10,25]))
def reverse(linked_list):
    prev = None
    current_node = linked_list.head
    while current_node:
      tmp = current_node.next
      current_node.next = prev
      prev = current_node
      current_node = tmp
    return LinkedList(prev)

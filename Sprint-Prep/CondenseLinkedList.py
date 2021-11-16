def condense_linked_list(node):
    single = set() #unordered list
    cur = node
    prev = None # may need to init as node

    while cur:
        temp = cur.next

        if cur.value in single:
            # print("single", single)
            cur = temp
            prev.next = cur
        else:
            single.add(cur.value) 
            prev = cur
            cur = cur.next
        
    return node
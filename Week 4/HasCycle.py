def has_cycle(head):
    end = head
    start = head
    while start and start.next:
        end = end.next
        start = start.next.next
        if(end == start):
            return 1
    return 0

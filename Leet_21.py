# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0) 
        head = result 

        carryTen = False
        
        while l1 != None and l2 != None:
            number = l1.val + l2.val
            if number >= 10:
                if carryTen == True:
                    number += 1 
                head.next = ListNode(number % 10) 
                carryTen = True
            else:
                if carryTen == True:
                    number += 1 
                    if number >= 10:
                        head.next = ListNode(number % 10) 
                        carryTen = True
                    else:
                        head.next = ListNode(number)
                        carryTen = False
                else:
                    head.next = ListNode(number)
                    carryTen = False
            l1 = l1.next
            l2 = l2.next
            head = head.next
            
        while l1 != None:
            if carryTen == False:
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
            else:
                number = l1.val + 1 
                if number >= 10:
                    head.next = ListNode(number%10)
                    carryTen = True
                    head = head.next
                    l1 = l1.next 

                else:
                    head.next = ListNode(number)
                    l1 = l1.next
                    head = head.next
                    carryTen = False
    
        while l2 != None:
            if carryTen == False:
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
            else:
                number = l2.val + 1 
                if number >= 10:
                    head.next = ListNode(number%10)
                    carryTen = True
                    head = head.next
                    l2 = l2.next 

                else:
                    head.next = ListNode(number)
                    l2 = l2.next
                    head = head.next
                    carryTen = False

                
        if carryTen == True:
            head.next = ListNode(1)
            head = head.next 
        
        return result.next

            

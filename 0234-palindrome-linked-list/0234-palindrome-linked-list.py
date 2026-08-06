# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=head
        stack=[]
        length=0
        while curr:
            print(curr.val)
            length+=1
            curr=curr.next
        count=0
        curr=head
        while curr:
            print('aa')
            if length%2==0:
                print(0)
                if count<length//2:
                    print("-")
                    stack.append(curr.val)
                else:
                    m=stack.pop()
                    if m!=curr.val:
                        return False
            else:
                if count<length//2:
                    stack.append(curr.val)
                elif count>length//2:
                    m=stack.pop()
                    if m!=curr.val:
                        return False
            count+=1
            curr=curr.next
        return True


        
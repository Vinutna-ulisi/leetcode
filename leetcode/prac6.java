SWAPPING NODES IN A LINKED LIST
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode first = head;
        
        
        for (int i = 1; i < k; i++) {
            first = first.next;
        }
        
        ListNode kthFromStart = first;
        ListNode second = head;
        
      
        while (first.next != null) {
            first = first.next;
            second = second.next;
        }
        
     
        int temp = kthFromStart.val;
        kthFromStart.val = second.val;
        second.val = temp;
        
        return head;
    }
}
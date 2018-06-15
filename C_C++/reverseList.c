struct ListNode{
        int val;
        struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* new_head = NULL;
    struct ListNode* old_next = NULL;
    if(head == NULL)
        return NULL;
    while(head != NULL)
    {
        old_next = head->next;
        head->next = new_head;
        new_head = head;
        head = old_next;
    }
    return new_head;
}
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if no cycle found, 1 if found a cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *cur, *check;

    cur = list;
    check = list;
    do {
        cur = cur->next;
        check = check->next->next;
        if (cur == check)
            return (1);
    } while (cur != NULL && check != NULL && check->next != NULL);
    return (0);
}
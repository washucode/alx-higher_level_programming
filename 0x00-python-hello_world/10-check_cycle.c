#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if no cycle found, 1 if found a cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *behind, *ahead;

    behind = list;
    ahead = list;
    do {
        behind = behind->next;
        ahead = ahead->next->next;
        if (behind == ahead)
            return (1);
    } while (behind != NULL && ahead != NULL  && ahead->next != NULL);
    return (0);
}
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if no cycle found, 1 if found a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *behind = list, *ahead = list;

	if(!list)
		return (0);
	while (behind  && ahead   && ahead->next) {
		behind = behind->next;
		ahead = ahead->next->next;
		if (behind == ahead)
			return (1);
	} 
	return (0);
}
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @i: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int i)
{
	listint_t *new_node, *cur_node;
	
	cur_node = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = i;
	new_node->next = NULL;
	if (*head == NULL)
		*head = new_node;
	else
	{
		while (cur_node->next != NULL)
			cur_node = cur_node->next;
		cur_node->next = new_node;
	}
	return (new_node);	
}

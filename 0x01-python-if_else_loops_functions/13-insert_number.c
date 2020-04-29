#include "lists.h"
/**
*insert_node - print number
*@head: header of list
*@number: integer
*Return: listint_t
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *nodo = NULL, *prev = NULL;

	if (*head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	nodo = *head;

	for ( ; nodo && nodo->n < number; )
	{
		prev = nodo;
		nodo = nodo->next;
	}
	new->next = nodo;

	if (prev == NULL)
		*head = new;
	else
		prev->next = new;
	return (new);
}

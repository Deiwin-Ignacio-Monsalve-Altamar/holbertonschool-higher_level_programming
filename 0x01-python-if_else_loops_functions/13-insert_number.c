#include "lists.h"
/**
*insert_node - print number
*@head: header of list
*@number: integer
*Return: listint_t
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *nodo;

	nodo = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (0);
	new->n = number;

	if (!*head)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	while (nodo != NULL)
	{
		if (number < nodo->n)
		{
			new->next = nodo;
			*head = new;
			return (new);
		}

		if (number <= nodo->next->n)
		{
			new->next = nodo->next;
			nodo->next = new;
			return (new);
		}

		nodo = nodo->next;
	}
	new->next = NULL;
	nodo->next = new;
	return (new);
}

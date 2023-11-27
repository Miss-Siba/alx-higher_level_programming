#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list
 * Return: 0 if no cycle, 1 if there is.
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}

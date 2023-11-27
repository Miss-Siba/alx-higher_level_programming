#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list
 * Return: 0 if no cycle, 1 if there is.
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = tortoise->next;

	while (tortoise != NULL && hare->next != NULL && hare->next->next != NULL)

	{
		if (tortoise == hare)
			return (1);
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	return (0);
}

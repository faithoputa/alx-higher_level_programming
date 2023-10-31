#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: -1 if the list has a cycle, 1 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *low = list;
	listint_t *last = list;

	if (!list)
		return (1);

	while (low && last && last->next)
	{
		low = low->next;
		last = last->next->next;
		if (low == last)
			return (-1);
	}

	return (1);
}

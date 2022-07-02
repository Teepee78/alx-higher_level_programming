#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_node_beginning - adds a node at the beginning of a singly linked list
 * @head: singly linked list
 * @n: number
 * Return: updated list
 */
listint_t *add_node_beginning(listint_t **head, int n)
{
	listint_t *new_node;

	/* create new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		exit(98);
	new_node->n = n;

	new_node->next = *head;
	*head = new_node;

	return (*head);
}

/**
 * reverse_list - reverses a singly linked list
 * @head: singly linked list
 * Return: reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *reversed, *singly_list = *head;

	/* create first node */
	reversed = malloc(sizeof(listint_t));
	if (reversed == NULL)
		exit(99);
	reversed->next = NULL;
	reversed->n = singly_list->n;

	/* add each element of the singly list to the beginning of reversed list */
	singly_list = singly_list->next;
	while (singly_list->next != NULL)
	{
		reversed = add_node_beginning(&reversed, singly_list->n);
		singly_list = singly_list->next;
	}

	/* add last element */
	reversed = add_node_beginning(&reversed, singly_list->n);

	return (reversed);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: singly linked list
 * Return: returns 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed, *temp, *singly_list = *head;

	/* check if list is empty */
	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);

	/* reverse list */
	reversed = reverse_list(head);
	temp = reversed;

	/* iterate through both lists and compare the values */
	while (singly_list->next != NULL && reversed->next != NULL)
	{
		/* compare values */
		if (reversed->n != singly_list->n)
		{
			free_listint(temp);
			return (0);
		}
		/* go to next nodes */
		reversed = reversed->next;
		singly_list = singly_list->next;
	}
	free_listint(temp);
	return (1);
}

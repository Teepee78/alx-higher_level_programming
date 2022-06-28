#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - inserts a number in a sorted singly linked list
 * @head: singly linked list
 * @number: number to be inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *temp;
    listint_t *list = *head;

    /* make new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;

    /* traverse head */
    while (list->next != NULL)
    {
        /* check if list->n is greater than number */
        if (list->n < number)
        {
            /* store present node */
            temp = list;

            list = list->next;
        }
        else
        {
            new_node->next = list;
            temp->next = new_node;
            break;
        }
    }
    return (new_node);
}

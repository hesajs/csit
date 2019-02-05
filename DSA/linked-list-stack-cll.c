/*
    Program to implement stack as Circular Linked List, CLL.
*/

#include<stdio.h>
#include<stdlib.h>

typedef struct nodes {
    int info;
    struct nodes* next;
} Node;

Node* start = NULL; // Points to the fist element of linked list.
Node* last = NULL;  // Points to the last element of linked list.

// Print all the elements of linked list in forward direction.
void Print(Node* node) {
    Node* temp = (Node*) malloc(sizeof(Node));
    temp = start;
    while(temp != last) {
        printf("%d, ", temp->info);
        temp = temp->next;
    }
    if(temp != NULL) printf("%d\n", temp->info);
}

// Insert the element in the end of linked list.
void Insert(Node** node, int element) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->info = element;
    if(start == NULL) {
        newNode->next = newNode;
        start = newNode;
        last = newNode;
    }
    else {
        last->next = newNode;
        last = newNode;
        last->next = start;
    }
    *node = newNode;
}

// Deletes the last element of linke list.
void Delete(Node* node) {
    Node* temp = (Node*) malloc(sizeof(Node));
    temp = start;
    if(start == NULL) return;
    else if (start == last) {
        free(temp);
        start=last=NULL;
    }
    else {
        while(temp->next != last) temp = temp->next;
        last = temp;
        temp->next = start;
        node = last;
    }
}

int main() {
    Node* head = (Node*) malloc(sizeof(Node));
    int input, option, n;
    short int flag;
    do {
        system("clear");	// system("cls"); uncomment for Windows.
    	printf("\n=-=-=-=-=-=-=-=- Choose one option -=-=-=-=-=-=-=-=\n");
    	printf("\n1) Insert\n2) Display\n3) Delete\n4) Exit\n> ");
    	scanf("%d", &option);
    
    	switch(option) {
    		case 1:
    			printf("\nEnter the number of elements: ");
    			scanf("%d", &n);
    			for(int i=0; i<n; i++) {
    				printf("\n> ");
    				scanf("%d", &input);
    				Insert(&head, input);
    			}
    			break;
    			
    		case 2:
    			printf("\n\nLinked List elements are: \n");
    			Print(head);
    			break;
    
    		case 3:
    			Delete(head);
    			break;
    
    		default:
    			system("clear");	// system("cls"); uncomment it for Windows.
    			flag=1;
    			break;
    	}
		while(getchar() != '\n');	// Just to clear the newline.
		printf("\nPress any key!\n");
		getchar();

    } while(option <4);
    return 0;
}
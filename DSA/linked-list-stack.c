/*
	Linked List program which implements stack principle, FILO, First In Last Out.
*/
#include<stdio.h>
#include<stdlib.h>

typedef struct nodes {
	int data;
	struct nodes *next;
}Node;

// Insert an elemnent at the end of the link list.
void Insert(Node** node, int element) {
	Node* newNode = (Node*) malloc(sizeof(Node));
	newNode->data = element;
	newNode->next = NULL;
	if(*node == NULL) *node = newNode;
	else {
		Node* temp = *node;
		while(temp->next != NULL) temp = temp->next;
		temp->next = newNode;
	}
}

// Delete the last element of the of linked list.
void Delete(Node* node) {
	Node* temp = node;
	if(node==NULL) {
		printf("Void Deletion!\n");
	} else if(node->next==NULL) {
		printf("Deleted item: %d\n", node->data);
		node=NULL;
		free(temp);
	} else {
		temp = node;
		while(temp->next->next != NULL) temp=temp->next;
		printf("Deleted item: %d\n", temp->next->data);
		free(temp->next);
		temp->next=NULL;
		node = temp;
	}
}

// Print all the elements in forward direction of the linked list. 
void Print(Node* node) {
	if(node == NULL) return;
	printf("%d ", node->data);
	Print(node->next);
}

int main() {
	Node* head = NULL;
	int n, input, option;	
	short int flag=0;
	do {
		system("clear");	// system("cls"); uncomment for Windows.
		printf("\n=-=-=-=-=-=-=-=- Choose one option -=-=-=-=-=-=-=-=\n");
		printf("\n1) Insert\n2) Traverse\n3) Delete\n4) Exit\n> ");
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
		printf("\nGo to Menu (Y/n): ");
		while(getchar() != '\n');	// Just to clear the newline.
	} while(getchar() != 'n');
	return 0;
}

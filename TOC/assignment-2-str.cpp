// Write a program for printing string over some set of alphabet

#include<stdio.h>

int main() {
	// char_def variable is set of character.
	char  char_def[2], x;
	int input; 

	printf("\n\n+=+=+=+=+=+=+= Enter the character at a time +=+=+=+=+=+=+=\n\n");

	printf("Number of set characters: ");
	scanf("%d", &input);
	for(int i=0; i<input; i++) {
		printf("Enter %d set character: ", (i+1));
		scanf(" %c", &char_def[i]);
	}

	printf("\nEnter the number of characters: ");
	scanf(" %d", &input);
	
	char final_ans[input];
	
	for(int i=0; i<input; i++) {
		do {
			printf("\nEnter the character: ");
			scanf(" %c", &x);
			if (!(x == char_def[0] || x == char_def[1])) 
				printf("Invalid character!\nTry again!\n");
		} while (!(x == char_def[0] || x == char_def[1]));
		final_ans[i] = x;
	}
	
	// printing the reuslts 
	for(int i=0; i<input; i++) printf("%c ", final_ans[i]);
	printf("\n\n");
	return 0;
}

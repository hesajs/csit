// Write a program for printing number over some set of number. 

#include<stdio.h>

int main() {
	int input, x;
	// set of number.
	int char_def[2] = {0,3};

	printf("\nEnter the number of number: ");
	scanf("%d", &input);
	
	int final_ans[input];
	
	printf("\n\n+=+=+=+=+=+=+= Enter the number at a time +=+=+=+=+=+=+=\n\n");
	for(int i=0; i<input; i++) {
		do {
			printf("\nEnter the number: ");
			scanf("%d", &x);
			if (!(x == char_def[0] || x == char_def[1])) 
				printf("Invalid number!\nTry again!\n");
		} while (!(x == char_def[0] || x == char_def[1]));
		final_ans[i] = x;
	}
	
	for(int i=0; i<input; i++) printf("%d ", final_ans[i]);
	
	return 0;
}

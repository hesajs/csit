// Write a program for DFA that accepts all the string ending with 3 a's over {a,b}

#include<stdio.h>
#include<string.h>
#define MAX 50

int is_valid(char arr[]) {
	for(int i=0; i < strlen(arr); i++) {
		if(arr[i] != 'a' && arr[i] != 'b' && arr[i] != '\n') return 0;
	}
	return 1;
}
int main() {
	char input[MAX];
	int input_len;
	printf("\nEnter the string over {a, b}: ");
	fgets(input, MAX, stdin);

	if (is_valid(input)) {
		input_len = strlen(input);
		if (input_len >= 3) {
			// Start subtracting from second last position because the last 
			// position contains the new line, '\n', 
			if (input[input_len-2] == 'a' && 
			input[input_len-3] == 'a' && input[input_len-4] == 'a') {
				printf("\nString Accepted! ");	
			} else {
				printf("\nString Rejected! ");
			}
		}
	} else {
		printf("\nInvalid Input! ");
	}


	// displays the input.
	for(int i=0; i < strlen(input); i++){
		printf("%c", input[i]);
	}
	printf("\n");
	return 0;
}

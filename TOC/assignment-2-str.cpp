// Write a program for printing string over some set of alphabet

#include<stdio.h>

// check_char() function checks wheather the 
// parameter 'value' contains on parameter 'arr' or not
int check_char(char arr[], int size_arr, char value) {
	for(int i=0; i < size_arr; i++) {
		if(value == arr[i])
			return 1;	
	}
	return 0;
}

int main() {
	char  x;
	int input, input_set, flag=1;

	printf("\n\n+=+=+=+=+=+=+= Enter the character at a time +=+=+=+=+=+=+=\n\n");

	printf("Number of set characters: ");
	scanf("%d", &input_set);

	// char_def variable is set of character(alphabet).
	char char_def[input_set];

	for(int i=0; i<input_set; i++) {
		printf("Enter %d set character: ", (i+1));
		scanf(" %c", &char_def[i]);
	}

	printf("\nEnter the number of characters: ");
	scanf(" %d", &input);
	
	// final_ans array contains the input string.
	char final_ans[input];
	
	for(int i=0; i<input; i++) {
		do {
			flag = 0;
			printf("\nEnter the character: ");
			scanf(" %c", &x);
			for(int j=0; j<input_set; j++){
				if (x != char_def[j]) {
					flag++;
				}
			}
			if(flag==input_set)
				printf("Invalid character!\n");
		} while (!(check_char(char_def, input_set, x)));
		final_ans[i] = x;
	}
	
	// printing the reuslts 
	printf("\nThe final string is : ");
	for(int i=0; i<input; i++) printf("%c ", final_ans[i]);
	printf("\n\n");

	return 0;
}

// Implementation of Shortest Job First.

#include<stdio.h>
#define MAX 50

int process_no;

void swap(int *x, int *y) {
	int temp;
	temp = *x;
	*x = *y;
	*y = temp;
}

void swap_char(char *x, char *y) {
	char temp;
	temp = *x;
	*x = *y;
	*y = temp;
}

void sort(char pid[], int a[], int b[], const int option) {
	for(int i=1; i<process_no-1; i++) {
		for(int j=1; j<process_no-i-1; i++) {
			// Sorting the process, bt: brust time, in ascending order.
			if(option == 1) {
				// if(bt[i] > bt[i+1]) 
				if(a[i] > a[i+1]) {
					swap(&a[i], &a[i+1]);
					swap(&b[i], &b[i+1]);
					swap_char(&pid[i], &pid[i+1]);
				}
			} 
			// Sorting the jobs by process ID.
			else {
				if(pid[i] > pid[i+1]) {
					swap(&a[i], &a[i+1]);
					swap(&b[i], &b[i+1]);
					swap_char(&pid[i], &pid[i+1]);
				}
			}
		}
	}
}

void display(char pid[], int tat[], int wt[]) {
	float awt=0.0;
	printf("\n\nPID\t\tTAT\t\tWT\n");
	for(int i=0; i<process_no; i++) {
		printf("%c\t\t%d\t\t%d\n", pid[i], tat[i], wt[i]);
		awt += wt[i];
	}
	awt /= process_no;
	printf("\nAverage WT (AWT): %.2f\n", awt);
}

int main() {
	int at[MAX], bt[MAX], wt[MAX], tat[MAX], ct[MAX];
	char pid[MAX];

	// taking input
	printf("\nNumber of processes: ");
	scanf("%d", &process_no);
	for(int i=0; i<process_no; i++) {
		printf("\nEnter the Process ID (PID) of process #%d: ", (i+1));
		scanf(" %c", &pid[i]);
		printf("Enter the Arrival Time(AT) of process #%d: ", (i+1));
		scanf("%d", &at[i]);
		printf("Enter the Brust Time(BT) of process #%d: ", (i+1));
		scanf("%d", &bt[i]);
	}

	sort(pid, bt, at, 1);
	
	// Calculating Completion Time(CT) of each process.
	ct[0] = bt[0];
	for(int i=1; i<process_no; i++) 
		ct[i] = ct[i-1] +bt[i];
	
	// Calculating TAT.
	for(int i=0; i<process_no; i++) 
		tat[i] = ct[i] - at[i];
	
	// Calculating WT.
	for(int i=0; i<process_no; i++) 
		wt[i] = tat[i] - bt[i];

	sort(pid, tat, wt, 0);
	display(pid, tat, wt);
	
	return 0;
}

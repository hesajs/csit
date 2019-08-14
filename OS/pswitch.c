#include<unistd.h>
#include<stdio.h>

int main() {
	int pid;
	pid = fork();
	if(pid==0) {
		for(;;)
			printf("C");
	} else if(pid>0) {
		for(;;)
			printf("P");
	}
}

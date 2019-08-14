#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void *func(void *para) {
	printf("This is the thread\n");
}

int main() {
	pthread_t id;
	pthread_create(&id, NULL, &func, NULL);
	printf("This is main thread\n");
	pthread_join(id, NULL);
	return 0;
}

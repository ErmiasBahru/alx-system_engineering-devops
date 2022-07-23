#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * main - create 5 zombie processes
 *
 * Return: void
 */

int main(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();
        if (child_pid == 0)
        {
            printf("Zombie process created, PID: %i\n", getpid());
            exit(0);
        }
    }

    while (0)
    {
        sleep(1);
    }
    return (0);
}
#include <stdio.h>
#include <stdlib.h>
/* between 1-100 correct is 42 */

int ans = 42;
int guess;

int main()
{
    printf("Hello, Welcome to the Guessing Game!\nPlease take a guess between 1-100\n");
do {
    printf("Enter a guess between 1 and 100: ");
    scanf("%d", &guess);

    if (guess != ans)
    {
        printf("Incorrect, Try again\n");
    }
    else
    {
        printf("Correct!");
    }
    }
    while (guess != ans);

    return 0;
}

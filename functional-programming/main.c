// #include <stdio.h>
// int main()
// {
//     int number;
//     printf("Enter an integer: ");
//     scanf("%d", &number);

//     // True if the remainder is 020
//     if (number < 1 && number > 100)
//     {
//         printf("enter valid number");
//     }
//     else
//     {
//     }

//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>

int main()
{
    srand(time(NULL));
    char totalChars[] = "abcdefghijklmnopqrstuvwxyz0123456789";
    int nchars = strlen(totalChars);
    while (true)
    {
        int length;
        printf("Length: ");
        scanf("%d", &length);
        if (length >= 1 && length <= 100)
        {
            int i;
            for (i = 0; i < length; i++)
            {
                printf("%c", totalChars[(int)((rand() / ((double)RAND_MAX + 1)) * nchars)]);
            }
            puts("");
        }
        else
        {
            printf("input valid number");
        }
    }
}
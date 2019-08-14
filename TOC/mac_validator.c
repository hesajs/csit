// Write a program that validates the 48 bit MAC address

#include <stdio.h>
#include <ctype.h>

int main()
{
    char mac_address[50];
    int j = 0, flag = 0;

    printf("\nEnter the mac_address: ");
    scanf("%[^\n]", mac_address);

    while (mac_address[j])
    {
        if (mac_address[j] >= 65 && mac_address[j] <= 90)
        {
            mac_address[j] = tolower(mac_address[j]);
        }

        if ((mac_address[j] >= 97 && mac_address[j] <= 102) ||
            (mac_address[j] >= '0' && mac_address[j] <= '9'))
        {
            flag = 1;
        }
        else
        {
            flag = 0;
            break;
        }
        j++;
        if (j > 12)
        {
            flag = 0;
            break;
        }
    }
    if (flag)
    {
        printf("\nValid MAC address\n");
    }
    else
        printf("\nInvalid MAC address\n");
}
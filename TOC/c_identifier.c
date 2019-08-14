// Write program to check valid C-identifiers

#include <stdio.h>
#include <string.h>
#define MAX 32

int isKeyword(char arr[])
{
    // C language 32 keywords.
    char keywords[32][10] = {
        "auto", "double", "int", "struct",
        "break", "else", "long", "switch",
        "case", "enum", "register", "typedef",
        "const", "extern", "return", "union",
        "char", "float", "short", "unsigned",
        "continue", "for", "signed", "volatile",
        "default", "goto", "sizeof", "void",
        "do", "if", "static", "while"};

    // if the input string matches with keyword
    for (int i = 0; i < 32; i++)
        if (strcmp(keywords[i], arr) == 0)
            return 1;
    // else if input string does not match
    return 0;
}

int isValidIdentifier(char arr[])
{
    int flag = 0;

    // return false if the string is C keyword
    if (isKeyword(arr))
        return 0;

    // checking whether the first letter contains special symbol or not.
    if ((arr[0] >= 'a' && arr[0] <= 'z') ||
        (arr[0] >= 'A' && arr[0] <= 'Z') || arr[0] == '_')
        flag = 1;
    else
        return 0;

    // checking rest of the letters of string follows the C-identifier rule
    for (int i = 1; i < strlen(arr); i++)
    {
        if ((arr[i] >= 'a' && arr[i] <= 'z') || arr[i] == '_' ||
            (arr[i] >= 'A' && arr[i] <= 'Z') || (arr[i] >= '0' && arr[i] <= '9'))
            flag = 1;
        else
            return 0;
    }
    if (flag)
        return 1;
    return 0;
}

int main()
{
    char input[MAX];

    printf("Enter any string: ");
    scanf("%[^\n]", input);

    if (isValidIdentifier(input))
        printf("\nValid C-identifier.\n");
    else
        printf("\nInvalid C-identifier.\n");
}
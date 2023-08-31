#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <windows.h>
unsigned char tape[1000000];
int p, tp, stack[1000000], matches[1000000];
struct node {
    char c;
    int num;
}opt[1000000];
inline void push(int x) {
    stack[tp++] = x;
}
inline int pop() {
    if (tp) return stack[--tp];
    else exit((puts("Unmatched ]"), 1));
}
int main(int argc, char* argv[])
{
    srand(GetTickCount());
    FILE* f = fopen(argv[1], "r");
    int q = 0; // Length of optimized representation
    while (!feof(f)) {
        if (!feof(f)) {
            char c = fgetc(f);
            if (c != '+' && c != '-' && c != '>' && c != '<' && c != ',' && c != '.' && c != '[' && c != ']'&&c!='?') continue;
            if (q && (c == '+' || c == '-' || c == '>' || c == '<') && opt[q - 1].c == c) {
                opt[q - 1].num++;
            }
            else {
                opt[q++].c = c;
                opt[q - 1].num = 1;
            }
        }
    }
    for (int i = 0; i < q; i++) {
        if (opt[i].c == '[') push(i);
        if (opt[i].c == ']') {
            int result = pop();
            matches[result] = i;
            matches[i] = result;
        }
    }
    if (tp) return puts("Unmatched ["), 1;
    int ip = 0;
    while (ip < q) {
        switch (opt[ip].c) {
        case '+': {
            tape[p] += opt[ip].num;
            break;
        }
        case '-': {
            tape[p] -= opt[ip].num;
            break;
        }
        case '>': {
            p += opt[ip].num;
            break;
        }
        case '<': {
            p -= opt[ip].num;
            break;
        }
        case ',': {
            tape[p] = getchar();
            break;
        }
        case '.': {
            putchar(tape[p]);
            break;
        }
        case '[': {
            if (!tape[p]) {
                ip = matches[ip];
            }
            break;
        }
        case ']': {
            if (tape[p]) {
                ip = matches[ip];
            }
            break;
        }
        case '?': {
            tape[p] = rand() & 255;
            break;
        }
        }
        ++ip;
    }
    return 0;
}


#include <iostream>
#include <fstream>
int main(int argc,char *argv[])
{
    std::ifstream f(argv[1]);
    char c;
    int x=0;
    while (f.get(c)) {
        if (c == 'i') x++;
        if (c == 'd') x--;
        if (c == 's') x *= x;
        if (c == 'o') std::cout << x << ' ';
        if (x < 0 || x == 256) x = 0;
    }
    return 0;
}

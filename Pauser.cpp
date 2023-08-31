#include<iostream>
#include<chrono>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<conio.h>
#ifndef _MSC_VER
#define sprintf_s sprintf
#define _getch getch
#endif
using namespace std;
using namespace std::chrono;
char cmd[1000000];
int main(int argc, char** argv) {
    cout << setprecision(7);
    if (argc < 3) {
        cerr << "Usage:Pauser <interpreter> <filename> <arguments>" << endl;
        cout << "Press any key to continue...";
        _getch();
        return 1;
    }
    for (int i = 1; i < argc; i++) sprintf_s(cmd, "%s %s", cmd, argv[i]);
    high_resolution_clock::time_point t1, t2;
    t1 = high_resolution_clock::now();
    int ret = system(cmd);
    t2 = high_resolution_clock::now();
    duration<long long, nano> d = t2 - t1;
    puts("");
    for (int i = 1; i <= 32; i++) putchar('-');
    puts("");
    cout << "Process exited in " << d.count() / 1e9 << " secs with return value " << ret << endl;
    cout << "Press any key to continue...";
    _getch();
    return 0;
}
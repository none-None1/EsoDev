#include <iostream>
#include <string>
#include <fstream>
std::string cmd;
char accumulator;
int main(int argc,char *argv[])
{
    std::ifstream f(argv[1]);
    std::getline(f, cmd);
    if (cmd != "Start epidemic") {
        std::cerr << "Program must start with Start epidemic";
        return 1;
    }
    while (cmd!="Delevop vaccine") {
        if (f.eof()) continue;
        std::getline(f, cmd);
        if (cmd == "Infect person") ++accumulator;
        if (cmd == "Deinfect person") --accumulator;
        if (cmd == "Bulk infect") accumulator = std::cin.get();
        if (cmd == "Bulk deinfect") accumulator = bool(accumulator);
        if (cmd == "Check number of infections") putchar(accumulator);
        if (cmd == "Skip next if no one infected" && !accumulator) std::getline(f, cmd),cmd="";
    }
    return 0;
}

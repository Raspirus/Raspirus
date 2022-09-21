#include <string>
#include <iostream>
#include <filesystem>
#include "File.cpp"

using namespace std;

int main() {
    string path = "/path/to/directory";
    for (const auto & entry : filesystem::directory_iterator(path)) {
        File file(entry.path().string());
        cout << path << "-> HASH: " << file.getHash() << endl;
    }
}
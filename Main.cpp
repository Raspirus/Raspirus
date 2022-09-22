#include <string>
#include <iostream>
#include <filesystem>
#include "class/File.cpp"

using namespace std;

int main() {
    string path;
    cout << "Insert path: ";
    cin >> path;
    for (const auto & entry : filesystem::directory_iterator(path)) {
        File file(entry.path().string());
        cout << path << "-> HASH: " << file.getHash() << endl;
    }
}
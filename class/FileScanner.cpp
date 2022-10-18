#include <iostream> 
#include <vector>
#include <filesystem>
#include "File.cpp"

using namespace std; 
/*
 * This class takes an array of files and scans their hashes for viruses
 * It takes the hashes to compare to from a file.
 * TODO: Incomplete class -> add Exceptions!
*/

class FileScanner {
    private:
        vector<File> unscannedList, cleanFiles, dirtyFiles;
        string path;

    public:
        FileScanner(string folder_path) {
            this->path = folder_path;
            listFiles();
        }

        void listFiles() {
            // Algorithm to put all files at a destination into an array
            for (const auto & entry : filesystem::directory_iterator(this->path)) {
                this->unscannedList.push_back((File(entry.path().string())));
                // Should list all files inside directory and sub-directory
                std::cout << entry.path() << std::endl;
            }
        } 

        void scanFiles() {
            // Compare each Hash of a file with the hash in a list
        }
        
        vector<File> getUnscannedFiles() {
            return this->unscannedList;
        }
        vector<File> getCleanFiles() {
            return this->cleanFiles;
        }
        vector<File> getDirtyFiles() {
            return this->dirtyFiles;
        }
};
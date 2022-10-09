#include <iostream> 
#include <vector>
#include "FileRetriever.cpp"

using namespace std; 
/*
 * This class takes an array of files and scans their hashes for viruses
 * It takes the hashes to compare to from a file.
 * TODO: Incomplete class -> add Exceptions!
*/

class FileScanner {
    private:
        vector<File> unscannedList, cleanFiles, dirtyFiles;

    public:
        FileScanner(string folder_path) {
            FileRetriever fr = FileRetriever(folder_path);
            this->unscannedList = fr.getFileList();
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
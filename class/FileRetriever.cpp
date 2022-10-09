#include <iostream> 
#include <vector>
#include <filesystem>
#include "File.cpp"

using namespace std; 
/*
 * This class has the main job of retreieving all files at a specific path.
 * The files then need to be saved in an array for later scanning.
 * TODO: Incomplete class -> add Exceptions!
*/
class FileRetriever {
    private:
        vector<File> fileList;
        string path;

        void listFiles() {
            // Algorithm to put all files at a destination into an array
            for (const auto & entry : filesystem::directory_iterator(path)) {
                this->addFile(File(entry.path().string()));
                // Should list all files inside directory and sub-directory
                std::cout << entry.path() << std::endl;
            }
        }        
    
    public:
        FileRetriever(string file_path) {
            ifstream ifile;
            ifile.open(file_path);
            this->path = file_path;
        }

        void addFile(File file) {
            this->fileList.push_back(file);
        }
        void removeFile(int index) {
            this->fileList.erase(fileList.begin() + index);
        }
        File getFile(int index) {
            return this->fileList.at(index);
        }
        vector<File> getFileList() {
            return this->fileList;
        }
};
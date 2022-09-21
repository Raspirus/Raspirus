#include <string> // Adds string support
#include <filesystem> // Adds path support
#include <iostream> // For cout to work
#include <fstream> // For file reading and manipulation

using namespace std;

/*
 * This class contains all the extracted information of a file.
 * Specifically:
 * - Name of the file, with extension
 * - Path of the file, full path: "G:/docus/tables/..." (with file name)
 * - MD5hash sum to compare with database
 */

class File {
    private:
        string name, path, md5hash;

        // Executes given CMD commands -> Used to create MD5 hashes
        string exec(const char* cmd) {
            array<char, 128> buffer;
            string result;
            shared_ptr<FILE> pipe(popen(cmd, "r"), pclose);
            if (!pipe) 
                throw runtime_error("popen() failed!");
            while (!feof(pipe.get())) {
                if (fgets(buffer.data(), 128, pipe.get()) != nullptr)
                    result += buffer.data();
            }
            return result;
        }

    public:

        File(string file_path) {
            ifstream ifile;
            ifile.open(file_path);
            setPath(file_path);
            setName(file_path);
            setHash(file_path);
        };

        // Extracts name from given path and sets it to the class
        void setName(string path) {
            filesystem::path p(path);
            // Exctracts filename and extension from the path and converts it back to a string
            this->name = p.filename().string();
            // DEBUG: Write out the file name
            cout << "filename and extension: " << p.filename() << endl;
        };

        /*
         * Returns the name of the file with extension
         * @return name of file with extension
         */
        string getName() {
            return this->name;
        };

        /*
         * Extracts the md5hash value from a file by using the given path
         * and sets it as the var value
         */
        void setHash(string path) {
            string md5sum = exec(("md5sum " + path).c_str()).substr(0, 32);
            this->md5hash = md5sum;
        };

        /*
         * Retrieves the saved hash from the file
         * @return md5hash or null
         */
        string getHash() {
            return this->md5hash;
        };

        /*
         * Sets the path to a file
         */
        void setPath(string path) {
            this->path = path;
        };

        /*
         * Retrieves the saved path
         * @return The previously set path, or null
         */
        string getPath() {
            return this->path;
        };

};
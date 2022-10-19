from backend.FileScanner import FileScanner


def main():
    path_to_check = "C:/Users/benbe/Documents/Coding/WebProjects"
    path_to_signatures = "C:/Users/benbe/Documents/School/MaturaProject/VirusShare_00000.md5"
    fs = FileScanner(path_to_check, path_to_signatures)
    fs.start_scanner()


main()

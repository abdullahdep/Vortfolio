#include <iostream>
#include <string>
#include <cstdlib> // Required for std::system
#include <fstream> // Required for writing files

// Function to check if g++ is already installed and configure it if missing
void ensureCppCompilerIsAvailable() {
    std::cout << "\n[System Check] Verifying C++ compiler status...\n";
    
    int checkResult = std::system("g++ --version >nul 2>&1");
    
    if (checkResult == 0) {
        std::cout << "[System Check] Modern C++ (g++) is already available on this PC!\n";
        return;
    }
    
    std::cout << "[System Check] g++ NOT found. Downloading C++ compiler environment via winget...\n";
    std::cout << "Please wait, this may take a couple of minutes depending on internet speed...\n\n";
    
    std::string setupCompilerCmd = 
        "winget install --id MSYS2.MSYS2 --exact --silent --accept-source-agreements --accept-package-agreements";
        
    std::system(setupCompilerCmd.c_str());
    std::cout << "[System Check] Compiler installer triggered. If compilation below fails, please restart this terminal window.\n";
}

// Function to create a Desktop Shortcut using Windows Script Host via a temporary VBScript
void createDesktopShortcut() {
    std::cout << "\n[Shortcut Generator] Creating Desktop shortcut for vortfolio.exe...\n";

    // Write a temporary VBScript that safely grabs the user's Desktop path and hooks up the shortcut properties
    std::string vbsCode = 
        "Set shell = CreateObject(\"WScript.Shell\")\n"
        "desktop = shell.SpecialFolders(\"Desktop\")\n"
        "Set fso = CreateObject(\"Scripting.FileSystemObject\")\n"
        "currentDir = fso.GetAbsolutePathName(\".\")\n"
        "Set shortcut = shell.CreateShortcut(desktop & \"\\Vortfolio.lnk\")\n"
        "shortcut.TargetPath = currentDir & \"\\vortfolio.exe\"\n"
        "shortcut.WorkingDirectory = currentDir\n"
        "shortcut.Description = \"Launch Django Vortfolio Server\"\n"
        "shortcut.Save\n";

    std::ofstream vbsFile("create_shortcut_temp.vbs");
    if (!vbsFile) {
        std::cerr << "Error: Could not generate shortcut helper script.\n";
        return;
    }
    vbsFile << vbsCode;
    vbsFile.close();

    // Execute the shortcut creation script silently
    std::system("wscript.exe create_shortcut_temp.vbs");

    // Instantly wipe out the temporary VBS file to keep the workspace clean
    std::remove("create_shortcut_temp.vbs");
    std::cout << "[Shortcut Generator] Shortcut successfully placed on your Desktop!\n";
}

// Function to generate and compile the vortfolio executable
void createvortfolioExecutable() {
    std::cout << "\n[Generator] Creating vortfolio source file...\n";

    std::string internalCode = 
        "#include <iostream>\n"
        "#include <string>\n"
        "#include <cstdlib>\n\n"
        "int main() {\n"
        "    std::string envName = \"env\";\n"
        "    std::cout << \"using python virtual enviroment if avalible while global\\n\";\n"
        "    std::string command = \".\\\\\" + envName + \"\\\\Scripts\\\\activate && python manage.py runserver 0.0.0.0:8000\";\n"
        "    std::system(command.c_str());\n"
        "    std::cout << \"bat_done\\n\";\n"
        "    std::cout << \"Press Enter to continue . . . \";\n"
        "    std::cin.get();\n"
        "    return 0;\n"
        "}\n";

    // 1. Write source to a temporary file
    std::ofstream outFile("vortfolio_temp.cpp");
    if (!outFile) {
        std::cerr << "Error: Could not generate temporary source file.\n";
        return;
    }
    outFile << internalCode;
    outFile.close();

    // 2. Trigger active g++ toolchain compiler 
    std::cout << "[Generator] Compiling vortfolio_temp.cpp into vortfolio.exe...\n";
    int compileResult = std::system("g++ vortfolio_temp.cpp -o vortfolio.exe -static-libgcc");

    // 3. Delete temporary cpp file
    std::remove("vortfolio_temp.cpp");

    if (compileResult == 0) {
        std::cout << "[Generator] Successfully created vortfolio.exe!\n";
        
        // Trigger shortcut generator step only if compiling succeeded
        createDesktopShortcut();
    } else {
        std::cerr << "[Generator] Error: Compilation failed. If you just installed g++ via winget, you must close this window and run install.exe again to refresh your paths.\n";
    }
}

int main() {
    // 1. Ensure system compiler infrastructure is active
    ensureCppCompilerIsAvailable();

    // 2. Setup isolated Django runtime environment boundaries
    std::string envName = "env";
    std::cout << "\nStarting environment creation and package installation...\n";

    std::string command = "pip install virtualenv && "
                          "python -m venv " + envName + " && "
                          ".\\" + envName + "\\Scripts\\activate && "
                          "pip install -r requirements.txt";

    int result = std::system(command.c_str());

    if (result == 0) {
        std::cout << "installation has been completed\n";
        createvortfolioExecutable();
    } else {
        std::cerr << "An error occurred during Python installation. File generation skipped.\n";
    }

    std::cout << "Press Enter to continue . . . ";
    std::cin.get();

    return result;
}

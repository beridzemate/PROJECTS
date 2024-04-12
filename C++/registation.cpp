#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct User {
    string username;
    string password;
    string email;
};

void registerUser(const User& user) {
    ofstream outfile("users.txt", ios::app);
    if (outfile.is_open()) {
        outfile << user.username << "," << user.password << "," << user.email << "\n";
        outfile.close();
        cout << "Registration successful!\n";
    } else {
        cout << "Unable to open file for writing.\n";
    }
}

int main() {
    User newUser;
    cout << "Enter username: ";
    cin >> newUser.username;
    cout << "Enter password: ";
    cin >> newUser.password;
    cout << "Enter email: ";
    cin >> newUser.email;

    registerUser(newUser);

    return 0;
}

// //pirveli davaleba
// let variable1 = "hello";
//  let variable2 = "World";


// variable1 = "my name is ";
// variable2 = "mate";


// console.log(variable1);
// console.log(variable2);


// //meore davaleba
// const pirveliCvladi = "pirveli mnishneloba";

// const axaliCvladi = "axali mnishneloba";


// console.log(axaliCvladi);

// //mesame davaleba
// let variable3 = 5;
// let variable4 = 7;


// let pasuxi = variable1 * variable2;

// console.log(variable3, "and", variable4, "is:", pasuxi);

// //meotxe davaleba
// let length = 10;

// let width = 5;


// let partobi = length * width;


// console.log("samkutxedis partobi aris", partobi);


// //mexute davaleba
// let num1 = 10;
// let num2 = 20;
// let num3 = 30;


// let sum = num1 + num2 + num3;


// let count = 3;


// let pasuxi1 = sum / count;


// console.log("The arithmetic mean is:", pasuxi1);

// const personalInfo = {
//     firstName: "Mate",
//     firstSurname: "Beridze",
//     age: 14,
//     school: "10th public school"
// };


// const friendInfo = {
//     firstName: "Nika",
//     firstSurname: "arvicigvari",
//     age: 14,
//     school: "10th public school",
// }

// console.log(firstName);
// console.log(firstSurname);
// console.log(age);
// console.log(school);





// document.getElementById("registrationForm").addEventListener("submit", function(event) {
//   event.preventDefault();


//  const email = document.getElementById("email").value.trim();
//  const password = document.getElementById("password").value;
//  const confirmPassword = document.getElementById("confirmPassword").value;
//  const nickname = document.getElementById("nickname").value.trim();


//   if (!email || !password || !confirmPassword || !nickname) {
//     alert("Please fill in all fields");
//     return;
//   }

//   if (password !== confirmPassword) {
//     alert("Passwords do not match");
//     return;
//   }


//   alert("Registration successful! Redirecting to homepage...");

//   window.location.href = "about.html";
// });


  


// var count = 0;


// while (count < 0) {
//     console.log("fr");
//     count++;
// }




class BankAccount {
    constructor(accountNumber, balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    deposit(amount) {
        this.balance += amount;
        return this.balance;
    }

    withdraw(amount) {
        if (this.balance >= amount) {
            this.balance -= amount;
            return this.balance;
        } else {
            throw new Error("Insufficient funds");
        }
    }

    transfer(recipient, amount) {
        if (this.balance >= amount) {
            this.balance -= amount;
            recipient.balance += amount;
            return this.balance;
        } else {
            throw new Error("Insufficient funds");
        }
    }
}

function authenticate(username, password) {
    // Simulated authentication, replace with actual authentication logic
    if (username === "user123" && password === "password123") {
        return true;
    } else {
        return false;
    }
}

function performTransaction() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question("Enter your username: ", (username) => {
        rl.question("Enter your password: ", (password) => {
            if (authenticate(username, password)) {
                // Simulated account details, replace with database query
                const userAccount = new BankAccount("123456789", 1000);
                const recipientAccount = new BankAccount("987654321", 500);

                rl.question("Enter the amount: ", (amountInput) => {
                    const amount = parseFloat(amountInput);
                    rl.question("Enter 'D' for deposit, 'W' for withdrawal, or 'T' for transfer: ", (choice) => {
                        choice = choice.toUpperCase();

                        try {
                            if (choice === "D") {
                                userAccount.deposit(amount);
                                console.log("Deposit successful. New balance:", userAccount.balance);
                            } else if (choice === "W") {
                                userAccount.withdraw(amount);
                                console.log("Withdrawal successful. New balance:", userAccount.balance);
                            } else if (choice === "T") {
                                userAccount.transfer(recipientAccount, amount);
                                console.log("Transfer successful. New balance:", userAccount.balance);
                            } else {
                                console.log("Invalid choice");
                            }
                        } catch (error) {
                            console.log("Error:", error.message);
                        }

                        rl.close();
                    });
                });
            } else {
                console.log("Authentication failed");
                rl.close();
            }
        });
    });
}

// Example usage
performTransaction();

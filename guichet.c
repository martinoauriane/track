#include <stdio.h>
#include <string.h>

struct Account {
  int accountNumber;
  char name[50];
  float balance;
};

void createAccount(struct Account accounts[], int *numAccounts){
  
  struct Account newAccount;
  printf("Enter an account number");
  scanf("%d", &newAccount.accountNumber);
  printf("Enter an account holder name");
  scanf("%s", newAccount.name);
  newAccount.balance = 0.0;
  accounts[*numAccounts] = newAccount;
  (*numAccounts)++;
  printf("\nAccount added successfully!\n");
}

struct Account* getAccount (struct Account accounts[], int *numAccounts, int accountNumber){
  for(int i = 0; i< *numAccounts; i++){
    if(accounts[i].accountNumber == accountNumber){
      return &accounts[i];
  }
  }
    return NULL; // if no account found
}
void deposit(struct Account accounts[], int *numAccounts){
  int accountNumber;
  float amount;

  printf("Enter an account number");
  scanf("%d", &accountNumber);
  struct Account* account = getAccount(accounts, *numAccounts, accountNumber);
  if(account == NULL){
    printf("\nAccount not found!\n");
    return;
  }
  printf("Enter amount to deposit");
  scanf("%f", &amount);
  account->balance += amount;

  printf("\nAmount deposited successfully!\n"); 
}

void withdrawMoney(struct Account accounts[], int *numAccounts){
  int accountNumber;
  float amount;
  printf("Enter an account number");
  scanf("%d", &accountNumber);

  struct Account* account = getAccount(accounts, *numAccounts, accountNumber);
  if(account == NULL){
    printf("\nAccount not found!\n");
    return;
  }
  
  printf("Enter amount to withdraw");
  scanf("%f", &amount);
  if (account->balance >= amount){
    account->balance -= amount;
    printf("\nAmount withdrawn successfully!\n");
  } else {
    printf("Insufficient balance!");
  }
  return;
}

void checkAccountBalance(struct Account accounts[], int *numAccounts){
  int accountNumber;
  printf("Enter an account number");
  scanf("%d", &accountNumber);

  struct Account* account = getAccount(accounts, *numAccounts, accountNumber);
  if(account == NULL){
    printf("\nAccount not found!\n");
    return;
  }
  printf("\nAccount Holder: %s\n", account->name);
  printf("Account's current balance : %.2f", account->balance);
  return;
}
  
int main() {
    struct Account accounts[100];
    int numAccounts = 0;
    int choice;
    do {
        printf("\n==============================\n");
        printf("  WELCOME TO BANK MANAGEMENT SYSTEM  \n");
        printf("==============================\n");

        printf("\nPlease choose an option:\n");
        printf("[1] Add Account\n");
        printf("[2] Deposit Money\n");
        printf("[3] Withdraw Money\n");
        printf("[4] Check Balance\n");
        printf("[5] Exit\n");

        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                createAccount(accounts, &numAccounts);
                break;
            case 2:
                deposit(accounts, numAccounts);
                break;
            case 3:
                withdrawMoney(accounts, &numAccounts);
                break;
            case 4:
                checkAccountBalance(accounts, &numAccounts);
                break;
            case 5:
                printf("\nThank you for using the Bank Management System. Goodbye!\n");
                break;
            default:
                printf("\nInvalid choice! Please try again.\n");
        }
    } while (choice != 5);

    return 0;
}
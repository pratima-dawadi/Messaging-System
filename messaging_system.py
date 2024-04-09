'''
Task 2: 
	Messaging System / Snap chat 

	Functionality: 
        Users can create account if they don't have any 
        Users can login using their username and password 
        User can search for any other users who are available in the app 
        One User can message another user and their messages are stored, don't  save more then 15 conversations 
        Any user can delete msg history on their end 
        Database handling using json/txt file handling

'''
import json

class MessagingSystem:
    def __init__(self):
        self.users_file='users.json'
        self.users_data=self.load_data(self.users_file)
        self.messages_file='messages.json'
        self.messages_data=self.load_data(self.messages_file)

    def load_data(self,file_name):
        try:
            with open(file_name,'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error on loading data: {e}")

    def save_data(self):
        with open(self.users_file, 'w') as f1, open(self.messages_file, 'w') as f2:
            json.dump(self.users_data, f1)
            json.dump(self.messages_data, f2)

    def signup(self,username,password):
        if username in self.users_data:
            print('User already exists')
        else:
            self.users_data[username]={"password":password,"messages":{}}
            self.save_data()
            print("Users created successfully")
            print("Logging in....")
            username_input=input("Enter username: ")
            password_input=input("Enter password: ")
            self.login(username_input,password_input)
    
    def login(self,username,password):
        if username in self.users_data:
            if self.users_data[username]["password"]==password:
                print("Logged in successfully")
                self.dashboard(username)
            else:
                print('Invalid password')
        else:
            print('User does not exist')

    def search_user(self):
        for user in self.users_data:
            print(user)

    def message(self,sender):
        receiver=input("Enter receiver username: ")
        message=input("Enter your message: ")
        self.send_message(sender,receiver,message)

    def send_message(self,sender,receiver,message):
        if receiver in self.users_data:
            if receiver in self.users_data[sender]["messages"]:
                if len(self.users_data[sender]["messages"][receiver]) >= 15:
                    print("You have reached the maximum number of conversations.")
                    return
                self.users_data[sender]["messages"][receiver].append(message)
            else:
                self.users_data[sender]["messages"][receiver] = [message]
            self.messages_data[sender] = self.users_data[sender]["messages"]
            self.save_data()
            print("Message sent successfully\n")
        else:
            print("User does not exist")  

    def delete_message(self, username):
        if username in self.users_data:
            self.users_data[username]["messages"] = {}
            self.messages_data[username] = {}
            self.save_data()
            print("Message history deleted successfully")
        else:
            print("User does not exist")

    def dashboard(self,username):
        while True:
            print("\n 1. Search User\n 2. Send Message\n 3. Delete Message\n 4. Logout\n")
            user_input=input("Enter your choice: ")
            if user_input=='1':
                self.search_user()
            elif user_input=='2':
                self.message(username)
            elif user_input=='3':
                self.delete_message(username)
            elif user_input=='4':
                print("\nLogged out successfully\n")
                main()
        

message_instance=MessagingSystem()

print("\n*******************************************************************")
print("----------------Welcome to Messaging System----------------")
print("*******************************************************************\n")

def main():
    while True:
        user_input=input("Already have an account? (y/n):")
        if user_input=='y' or user_input=='Y':
            user_name=input("Enter username: ")
            password=input("Enter password: ")
            message_instance.login(user_name,password)
        elif user_input=='n' or user_input=='N':
            user_name=input("Enter username: ")
            password=input("Enter password: ")
            message_instance.signup(user_name,password)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
    



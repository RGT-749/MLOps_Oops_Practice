class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.attempts = 0
        self.max_attempts = 2
        self.menu()

    def signup(self):
        email = input("Enter your email here ->")
        pwd = input("Enter your password ->")
        self.username = email
        self.password = pwd
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please sign up first by pressing 1")
        else:
            while self.attempts < self.max_attempts:
                uname = input("Please enter your email here ->")
                pwd = input("Please enter your password here ->")
            
                if self.username == uname and self.password == pwd:
                    print("You have signed in successfully")
                    self.loggedin = True
                    return
                else:
                    self.attempts +=1
                    remaining = self.max_attempts - self.attempts

                    if remaining > 0:
                        print(f"Please enter correct credentials..{remaining} attempts remaining!")
                    else:
                        print("Account locked due to multiple failed attempts")          
        print("\n")
        self.attempts = 0
        self.menu()

    def post_message(self):
        if self.loggedin == True:
            message = input("Enter your message here ->")
            print(f"following content has been postd ->")
            print("\n")
            print(f"{message}")
        else:
            print("You need to signin first to post anything..")
        print("\n")
        self.menu()

    def message_someone(self):
        if self.loggedin == True:
            message = input("Enter your message here ->")
            friend = input ("Whom do you want to send the message?")
            print("Your message has been sent successfully")
        else:
            print("You need to signin first to send a message..")
        print("\n")
        self.menu()

    def menu(self):
        user_input =input("""Welccome to chatbook! How would you like to proceed?

                        Please select the appropriate option from the following list

                        Press "1" to signup
                        Press "2" to signin
                        Press "3" to write a post
                        Press "4" to message a friend
                        Press any other key to exit
                        """)

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post_message()
        elif user_input == "4":
            self.message_someone()
        else:
            exit()

        self.menu()
chatbook()
import streamlit as st


class Chatbook:

    def __init__(self):

        # Store values in Streamlit session
        if "username" not in st.session_state:
            st.session_state.username = ""

        if "password" not in st.session_state:
            st.session_state.password = ""

        if "loggedin" not in st.session_state:
            st.session_state.loggedin = False

        if "attempts" not in st.session_state:
            st.session_state.attempts = 0

        self.max_attempts = 2


    def signup(self):

        st.header("📝 Sign Up")

        email = st.text_input("Enter your email")

        password = st.text_input(
            "Enter your password",
            type="password"
        )

        if st.button("Sign Up"):

            if email == "" or password == "":
                st.warning("Please enter email and password.")

            else:
                st.session_state.username = email
                st.session_state.password = password

                st.success("You have signed up successfully!")


    def signin(self):

        st.header("🔐 Sign In")

        # Check whether user has signed up
        if st.session_state.username == "":

            st.info("Please sign up first.")

            return

        email = st.text_input("Enter your email")

        password = st.text_input(
            "Enter your password",
            type="password"
        )

        if st.button("Sign In"):

            if st.session_state.attempts >= self.max_attempts:

                st.error(
                    "Account locked due to multiple failed attempts."
                )

                return


            if (
                email == st.session_state.username
                and password == st.session_state.password
            ):

                st.session_state.loggedin = True
                st.session_state.attempts = 0

                st.success("You have signed in successfully!")


            else:

                st.session_state.attempts += 1

                remaining = (
                    self.max_attempts
                    - st.session_state.attempts
                )

                if remaining > 0:

                    st.error(
                        f"Incorrect credentials. "
                        f"{remaining} attempt(s) remaining."
                    )

                else:

                    st.error(
                        "Account locked due to multiple failed attempts."
                    )


    def post_message(self):

        st.header("📝 Write a Post")

        if not st.session_state.loggedin:

            st.warning(
                "You need to sign in first to post anything."
            )

            return


        message = st.text_area(
            "Enter your message"
        )

        if st.button("Post"):

            if message == "":
                st.warning("Please enter a message.")

            else:

                st.success(
                    "Your post has been published!"
                )

                st.write("### Your Post")

                st.write(message)


    def message_someone(self):

        st.header("💬 Message a Friend")

        if not st.session_state.loggedin:

            st.warning(
                "You need to sign in first to send a message."
            )

            return


        friend = st.text_input(
            "Whom do you want to send the message?"
        )

        message = st.text_area(
            "Enter your message"
        )


        if st.button("Send Message"):

            if friend == "" or message == "":

                st.warning(
                    "Please enter friend name and message."
                )

            else:

                st.success(
                    f"Your message has been sent to {friend}!"
                )


    def logout(self):

        st.session_state.loggedin = False

        st.success("You have been logged out.")


# --------------------------------------------------
# STREAMLIT APPLICATION
# --------------------------------------------------

st.set_page_config(
    page_title="Chatbook",
    page_icon="💬"
)

st.title("💬 Welcome to Chatbook")


app = Chatbook()


# Sidebar
st.sidebar.title("Menu")


if st.session_state.loggedin:

    option = st.sidebar.radio(
        "Choose an option",
        [
            "Home",
            "Write a Post",
            "Message a Friend",
            "Logout"
        ]
    )

else:

    option = st.sidebar.radio(
        "Choose an option",
        [
            "Home",
            "Sign Up",
            "Sign In"
        ]
    )


# --------------------------------------------------
# MENU
# --------------------------------------------------

if option == "Home":

    st.subheader("Welcome to Chatbook!")

    if st.session_state.loggedin:

        st.success(
            f"You are logged in as "
            f"{st.session_state.username}"
        )

    else:

        st.info(
            "You are not logged in."
        )


elif option == "Sign Up":

    app.signup()


elif option == "Sign In":

    app.signin()


elif option == "Write a Post":

    app.post_message()


elif option == "Message a Friend":

    app.message_someone()


elif option == "Logout":

    app.logout()
class User:
    """A class to store username and validate password."""

    def __init__(self, username, password):
        """Initialize username and password."""
        self.username = username
        self.__password = password

    def check_password(self, input_password):
        """Check whether the input password matches the stored password."""
        return self.__password == input_password


# Create a user object
u1 = User("alice", "secure123")

# Check passwords
print(u1.check_password("secure123"))
print(u1.check_password("wrong123"))
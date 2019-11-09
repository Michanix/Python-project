import getpass

def get_user_path():
    username = getpass.getuser()
    path = '/home/{}/Desktop'.format(username)
    return path

if __name__ == "__main__":
    get_user_path()
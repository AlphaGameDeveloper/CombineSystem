from termcolor import colored

def help():
    text = f"""{colored("CombineSystem", "green", attrs=["bold"])} is not like other operating systems. Rather then typing the command along with arguments, you only type the command, and then CombineSystem will prompt you for arguments!\n
    
    Commands:
    {colored("cowsay", "light_blue", attrs=["bold"])} - get ASCII art of a cow saying your text!\n
    {colored("help", "light_blue", attrs=["bold"])} - get help on commands! {colored("which you probably already figured out...", "white", attrs=["dark"])}\n
    {colored("ls", "light_blue", attrs=["bold"])} - show the files and folders in the current directory!\n
    {colored("cd", "light_blue", attrs=["bold"])} - change the directory you are in\n
    {colored("read", "light_blue", attrs=["bold"])} - read a text file!\n
    {colored("osmode", "light_blue", attrs=["bold"])} - run a command in OS mode, meaning it will be handled by your base OS and not CombineSystem\n
    {colored("wget", "light_blue", attrs=["bold"])} - download files from URL\n
    """
    print(text)

"""
    Color Print for Windows and Linux

    Offers very simply color printing 

"""

# Bright Foreground Colors
BF_GREY = '\033[90m'
BF_RED = '\033[91m'
BF_GREEN = '\033[92m'
BF_YELLOW = '\033[93m'
BF_BLUE = '\033[94m'
BF_PURPLE = '\033[95m'
BF_TEAL = '\033[96m'
BF_WHITE = '\033[97m'

# Not as Bright Foreground Colors
MF_GREY = '\033[30m'
MF_RED = '\033[31m'
MF_GREEN = '\033[32m'
MF_YELLOW = '\033[33m'
MF_BLUE = '\033[34m'
MF_PURPLE = '\033[35m'
MF_TEAL = '\033[36m'
MF_WHITE = '\033[37m'

# Background Colors
MB_GREY = '\033[40m'
MB_RED = '\033[41m'
MB_GREEN = '\033[42m'
MB_YELLOW = '\033[43m'
MB_BLUE = '\033[44m'
MB_PURPLE = '\033[45m'
MB_TEAL = '\033[46m'
MB_WHITE = '\033[47m'

# Bright Background Colors
BB_GREY = '\033[100m'
BB_RED = '\033[101m'
BB_GREEN = '\033[102m'
BB_YELLOW = '\033[103m'
BB_BLUE = '\033[104m'
BB_PURPLE = '\033[105m'
BB_TEAL = '\033[106m'
BB_WHITE = '\033[107m'

END_COLOR = '\033[0m'

def demo():
    '''
        Display a demo of what CPrint can do.
    '''
    
    print(f"""
    {BF_RED}   _____      _              _____                
    {BF_YELLOW} /  ____|    | |            |  __ \                     
    {BF_GREEN} | |     ___ | | ___  _ __  | |  | | ___ _ __ ___   ___  
    {BF_TEAL} | |    / _ \| |/ _ \| '__| | |  | |/ _ \ '_ ` _ \ / _ \   
    {BF_BLUE} | |___| (_) | | (_) | |    | |__| |  __/ | | | | | (_) |  
    {BF_PURPLE} \______\___/|_|\___/|_|    |_____/ \___|_| |_| |_|\___/  {END_COLOR} """)

    print(
        "",
        "# Bright Foreground Colors",
        f'{BF_GREY}{"BF_GREY":<17}{END_COLOR}' 
        f'{BF_RED}{"BF_RED":<17}{END_COLOR}'
        f'{BF_GREEN}{"BF_GREEN":<17}{END_COLOR}'
        f'{BF_YELLOW}{"BF_YELLOW":<17}{END_COLOR}',
        f'{BF_BLUE}{"BF_BLUE":<17}{END_COLOR}'
        f'{BF_PURPLE}{"BF_PURPLE":<17}{END_COLOR}'
        f'{BF_TEAL}{"BF_TEAL":<17}{END_COLOR}'
        f'{BF_WHITE}{"BF_WHITE":<17}{END_COLOR}',

        "",
        "# Not as Bright Foreground Colors",
        f'{MF_GREY}{"MF_GREY":<17}{END_COLOR}' 
        f'{MF_RED}{"MF_RED":<17}{END_COLOR}'
        f'{MF_GREEN}{"MF_GREEN":<17}{END_COLOR}'
        f'{MF_YELLOW}{"MF_YELLOW":<17}{END_COLOR}',
        f'{MF_BLUE}{"MF_BLUE":<17}{END_COLOR}'
        f'{MF_PURPLE}{"MF_PURPLE":<17}{END_COLOR}'
        f'{MF_TEAL}{"MF_TEAL":<17}{END_COLOR}'
        f'{MF_WHITE}{"MF_WHITE":<17}{END_COLOR}',

        "",
        "# Background Colors",
        f'{MB_GREY}{"MB_GREY":<17}{END_COLOR}' 
        f'{MB_RED}{"MB_RED":<17}{END_COLOR}'
        f'{MB_GREEN}{"MB_GREEN":<17}{END_COLOR}'
        f'{MB_YELLOW}{"MB_YELLOW":<17}{END_COLOR}',
        f'{MB_BLUE}{"MB_BLUE":<17}{END_COLOR}'
        f'{MB_PURPLE}{"MB_PURPLE":<17}{END_COLOR}'
        f'{MB_TEAL}{"MB_TEAL":<17}{END_COLOR}'
        f'{MB_WHITE}{"MB_WHITE":<17}{END_COLOR}',

        "",
        "# Bright Background Colors",
        f'{BB_GREY}{"BB_GREY":<17}{END_COLOR}' 
        f'{BB_RED}{"BB_RED":<17}{END_COLOR}'
        f'{BB_GREEN}{"BB_GREEN":<17}{END_COLOR}'
        f'{BB_YELLOW}{"BB_YELLOW":<17}{END_COLOR}',
        f'{BB_BLUE}{"BB_BLUE":<17}{END_COLOR}'
        f'{BB_PURPLE}{"BB_PURPLE":<17}{END_COLOR}'
        f'{BB_TEAL}{"BB_TEAL":<17}{END_COLOR}'
        f'{BB_WHITE}{"BB_WHITE":<17}{END_COLOR}',
        sep="\n"
        )


def color_string(string, color: str):
    if not string:
        return string
    return f"{color}{str(string)}{END_COLOR}"


def red(string: str) -> str:
    '''
        Given a string, this function will return the string 
        wrapped with escape codes that'll codes that'll color 
        the provided string red.
    '''
    return '{}{}{}'.format(
        BF_RED,
        str(string),
        END_COLOR
    )


def green(string: str) -> str:
    '''
        Given a string, this function will return the string 
        wrapped with escape codes that'll codes that'll color 
        the provided string green.
    '''
    return '{}{}{}'.format(
        BF_GREEN,
        str(string),
        END_COLOR
    )


def yellow(string: str) -> str:
    '''
        Given a string, this function will return the string 
        wrapped with escape codes that'll codes that'll color 
        the provided string yellow.
    '''
    return '{}{}{}'.format(
        BF_YELLOW,
        str(string),
        END_COLOR
    )


def blue(string: str) -> str:
    '''
        Given a string, this function will return the string 
        wrapped with escape codes that'll codes that'll color 
        the provided string blue.
    '''
    return '{}{}{}'.format(
        BF_BLUE,
        str(string),
        END_COLOR
    )


def purple(string: str) -> str:
    '''
        Given a string, this function will return the string 
        wrapped with escape codes that'll codes that'll color 
        the provided string purple.
    '''
    return '{}{}{}'.format(
        BF_PURPLE,
        str(string),
        END_COLOR
    )


def teal(string: str) -> str:
    '''
        Given a string, this function will return the string 
        wrapped with escape codes that'll codes that'll color 
        the provided string a bluey teal.
    '''
    return '{}{}{}'.format(
        BF_TEAL,
        str(string),
        END_COLOR
    )


def white(string: str) -> str:
    '''
        Given a string, this function will return the string 
        wrapped with escape codes that'll codes that'll color 
        the provided string a bright white, brighter than default 
        for most terminals.
    '''
    return '{}{}{}'.format(
        BF_WHITE,
        str(string),
        END_COLOR
    )


def pred(string: str) -> None:
    '''
        Given a string, this function will print the string in a red foreground.
    '''
    print('{}{}{}'.format(
        BF_RED,
        str(string),
        END_COLOR
    ))


def pgreen(string: str) -> None:
    '''
        Given a string, this function will print the string in a green foreground.
    '''
    print('{}{}{}'.format(
        BF_GREEN,
        str(string),
        END_COLOR
    ))


def pyellow(string: str) -> None:
    '''
        Given a string, this function will print the string in a yellow foreground.
    '''
    print('{}{}{}'.format(
        BF_YELLOW,
        str(string),
        END_COLOR
    ))


def pblue(string: str) -> None:
    '''
        Given a string, this function will print the string in a blue foreground.
    '''
    print('{}{}{}'.format(
        BF_BLUE,
        str(string),
        END_COLOR
    ))


def ppurple(string: str) -> None:
    '''
        Given a string, this function will print the string in a purple foreground.
    '''
    print('{}{}{}'.format(
        BF_PURPLE,
        str(string),
        END_COLOR
    ))


def pteal(string: str) -> None:
    '''
        Given a string, this function will print the string in a teal foreground.
    '''
    print('{}{}{}'.format(
        BF_TEAL,
        str(string),
        END_COLOR
    ))


def pwhite(string: str) -> None:
    print('{}{}{}'.format(
        BF_WHITE,
        str(string),
        END_COLOR
    ))



def _windows_on():
    # internal function to allow color printing on windows terminals
    import os
    import sys
    if 'win' in sys.platform.lower():
        _ = os.system('color FF')

_windows_on()


if __name__ == '__main__':
    demo()


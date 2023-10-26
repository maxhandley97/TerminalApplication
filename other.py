import sys
from colorama import init
from termcolor import colored, cprint


text = colored("Hello, World!", "red", attrs=["bold"])

print(text)
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
    cprint(i, "magenta", end=" ")

cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)


# use Colorama to make Termcolor work on Windows too
init()

# then use Termcolor for all colored text output
color = input('type in a color').lower()
x = colored(color, "red")
print(x)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{Colors.BOLD}{Colors.UNDERLINE}{Colors.HEADER}Stars War Series. Death Star Fun Facts:\n{Colors.ENDC}")

# have at least three lines or sentences
# have at least three and no more than eight replacements and two of them must be present in more than one sentence

replacements = [
    "noun(space): ",  # 0 noun : space-station
    "noun(war): ",  # 1 noun : weapon
    "noun(authority): ",  # 2 noun : empire
    "adjective(size): ",  # 3 adjective : big
    "noun(space): ",  # 4 noun : moon
    "adjective(strength): ",  # 5 adjective : powerful
    "verb(war): ",  # 6 verb : destroy
    "noun(number): ",  # 7 noun(number) : two
]

print(
    "\nThe Death Star is a {0} and super-{1} built by the Galactic {2}.\nA Death Star is so {3} that it's the size of a {4}.\nThis {1} is so {5} it can {6} an entire planet.\nDespite all odds, the Revel Alliance was able to {6} not one but {7} Death Stars."
    .format(
        *map(
            lambda replacement: f'{Colors.WARNING}{Colors.BOLD}{Colors.UNDERLINE}' + input(
                replacement) + f'{Colors.ENDC}',
            replacements
        )
    )
)

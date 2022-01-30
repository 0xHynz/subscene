
import sys
from .scrap import Functions as func
from .scrap import Subscene as subs

options = ['genre','tahun','bahasa']
banner = "\nSupport me in \033[92mhttps://trakteer.id/0xhynz\033[97m\ncredit: subscene.my.id"

def looping_result(__):
    n = 0;print()
    for _ in __:
        print ("[{}]. {}".format(n,_[0]))
        n += 1
    return

def select_options(lists):
    looping_result(lists)
    getter = input('\n[?] select options: ')

    try:
        x = lists[int(getter)][1]
    except:
       sys.exit('[!] out of options, bye!')

    subs().start_download(x)


def main():
    print (banner)
    try:
        sys.argv[1] = sys.argv[1]
    except IndexError:
        sys.exit("""\n[-] usage: main.py <query>

    [?] example:
        - python3 main.py fate
        - python3 main.py "mr robot" (with spaces)
""")

    if not sys.argv[1] in options:
       result = func.search(sys.argv[1])
       select_options(result)






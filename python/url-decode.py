# protocol: intratech-smartag:o1|o2|o3|thePDF
# update pnid list - glob
# update iso list - glob
# download ip data
# op1:
# op2:
# op3: optional ip data (pid folder , ../iso ) to download
# thePDF: pdf file to open
#  glob: create iso file list
#
from urllib.request import urlopen
with urlopen(r'http://127.0.0.1:/esop/utftest.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

for word in story_words:
    print(word)
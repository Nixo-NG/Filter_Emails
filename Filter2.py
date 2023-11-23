# download last python update
# https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
# You must add TLD you don't want in text warned_list


import os

Textfilter = str(input(r"Your combo: "))
if not os.path.isdir("Filtered_Emails"):
    os.mkdir("Filtered_Emails")
else:
    pass

Emails_filtered = open("Filtered_Emails/Filtered_Combo.txt", 'a', encoding="utf8", errors="ignore")
warned_list = open(r"warned_list.txt", 'r', encoding="utf8", errors="ignore").readlines()
set1 = set()
newlist = []
for TLD in warned_list:
    newlist.append(TLD.strip())

with open(Textfilter, 'r', encoding="utf8", errors="ignore") as file:
    for i in file:
        if ':' not in i or '@' not in i:
            continue
        elif i[i.index('@'): i.index(':')].lower() in newlist:
            continue
        elif i not in set1:
            Emails_filtered.write(i)
            set1.add(i)
        else:
            continue

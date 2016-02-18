#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails =list()
for line in handle :
    if line.startswith("From ") :
        linesplit = line.split()
        emails.append(linesplit[1])

emailrate = dict()
for address in emails:
    emailrate[address]=emailrate.get(address,0)+1

largest = None
for v in emailrate.values():
    if (largest is None or v>largest):
        largest = v
mostfreqemail = {key:value for key,value in emailrate.items() if value==largest}
for key,value in mostfreqemail.items():
    print key,value
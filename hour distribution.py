#Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull
#the hour out from the 'From ' line by finding the time and then splitting
#the string a second time using a colon.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hour = list()
for line in handle:
    if line.startswith('From '):
        time = line.split()[5]
        hour.append(time[:2])
        
count = dict()
for h in hour:
    count[h]=count.get(h,0)+1
result = count.items()
for x,y in sorted(result):
    print x,y


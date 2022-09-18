#Using double split
#Goal - To extract the words after '@' i.e. name of the school

receivedmessage_email = "From nehajoshi@asu.com Sat Jan 5 09:14:16 2008"
words = receivedmessage_email.split()
email = words[1]
part = email.split('@')
print(part[1])

#
import random
import string
list_of_domain=['aa.com','gmail.com','yahoo.com','outlook.com']
length_of_mail=10
letters= string.ascii_lowercase
all_mail=[]
path='demo.txt'
for domain in list_of_domain:
    for i in range(20):
        randstring=''.join(random.choice(letters) for i in range(length_of_mail))
        mail= randstring + '@' + domain
        all_mail.append(mail)
print(mail)


with open(path,'w') as f:
    for email in all_mail:
        f.write(email)
        f.write(',')
        f.write('\n')

    #option1
    all_mail_list=',\n'.join(all_mail)
    f.write(all_mail_list)
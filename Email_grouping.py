#Email Domain Grouping
with open('emails.txt') as f: #Ensure emails.txt is available in the same path of this python code
    emails = f.readlines()

domain_to_users = {}
for email in emails:
    user, domain = email.strip().split('@')
    domain_to_users.setdefault(domain, []).append(user)

print(domain_to_users)

import outlook
mail = outlook.Outlook()
mail.login('devtest0312@outlook.com','U0IQ0AiF')
mail.inbox()
print(mail.read())

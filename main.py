from themail import *

html = """
<html>
  <body>
    <h1>Olá,</h1>
    <p>Se recebeu este email, quer dizer que está funcionando.</p>
    <p>Para usar outra conta de email do Gmail, será necessário criar uma nova chave</p>
    <p>para habilitar o app.</p>
    <b>Acesse este <a href="https://myaccount.google.com/u/1/apppasswords">link</a> para criar chave.</b>
    <br><br>
    <p>Em seguida use o código abaixo para testar com o email e chave criada!</p>
    <i>from themail import *</i><br>
    <i>html = "Teste do novo email"</i><br>
    <i>email = Themail("NOVO EMAIL","CHAVE CRIADA","smtp.gmail.com","465")</i><br>
    <i>email.send(["EMAIL USUARIO 1","EMAIL USUARIO 2"],"Email novo!",html)</i>
    <br><br>
    At.te,<br>
    Python To Developer
  </body>
</html>
"""

email = Themail()
result = email.send("<YOUR EMAIL>","Habilidando novo email!",html)
print(result)

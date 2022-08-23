import os

version = "1.0.0"

status = "status"
criar = "criar"
deletar = "deletar"
usuarios = "usuarios"
nomeUsuario = ""
senhaUsuario = ""
versionTool = "--version"
helpTool = "--help"
cancelTool = "--cancel"

  
def _tools(tool):
  if tool == versionTool:
    print ("Versão: " + version)
  if tool == helpTool:
    print ("Para entender como utilizar esse programa abra o arquivo ReadMe que se encontra na pasta raiz do arquivo baixado, junto a este programa.")
  if tool == cancelTool:
    print ("Retornando ao módulo principal")
    start()

def _createUser(): ##criar
    nomeUsuario = input(str("Qual o nome do usuário? Digite --cancel para cancelar: "))
    if nomeUsuario == versionTool or nomeUsuario == helpTool or nomeUsuario == cancelTool:
      _tools(nomeUsuario)
      _createUser()
    senhaUsuario = input(str("Qual a senha do usuário? Digite --cancel para cancelar: "))
    if senhaUsuario == versionTool or senhaUsuario == helpTool or senhaUsuario == cancelTool:
      _tools(senhaUsuario)
      _createUser()
    os.system('cmd /c "net user {} {} /add"'.format(nomeUsuario, senhaUsuario))
    binaryAdmin = input(str("Gostaria de tornar o usuário administrador? 1 para sim, 0 para não, --cancel para cancelar: "))
    if binaryAdmin == versionTool or binaryAdmin == helpTool or binaryAdmin  == cancelTool:
      _tools(binaryAdmin)
      os.system('cmd /c "net user {} /delete"'.format(nomeUsuario))
      _createUser()
      
    elif (binaryAdmin == "1"):
        os.system('cmd /c "net localgroup Administradores {} /add"'.format(nomeUsuario))
        os.system('cmd /c "net localgroup Administrators {} /add"'.format(nomeUsuario))
        print("Adicionado como Administrador")
        print ("Retornando ao módulo principal")

    elif (binaryAdmin == "0"):
        print ("Retornando ao módulo principal")

    else:
        print ("ERROR 01: Usuário não será criado")
        os.system('cmd /c "net user {} /delete"'.format(nomeUsuario))
    start()

def _deleteUser(): ##deletar
    nomeUsuario = input(str("Qual o nome do usuário a ser deletado? Digite --cancel para cancelar: "))
    if nomeUsuario == versionTool or nomeUsuario == helpTool or nomeUsuario == cancelTool:
      _tools(nomeUsuario)
      _deleteUser()
    else:
        os.system('cmd /c "net user {} /delete"'.format(nomeUsuario))
        print("Usuário removido")
        print ("Retornando ao módulo principal")
    start()

def _checkUsers(): ##usuarios
    os.system('cmd /c "net user"')
    input("Pressione Enter para continuar ")
    start()

def _checkUserStatus(): ##status
    nomeUsuario = input(str("Qual usuário você gostaria de visualizar? "))
    os.system('cmd /c "net user {}"'.format(nomeUsuario))
    input("Pressione Enter para continuar ")
    start()


def start():
    userInput = ""
    userInput = input(str("Qual comando você desejaria utilizar? "))
    if userInput == versionTool or userInput == helpTool or userInput == cancelTool:
      _tools(userInput)
      start()
    else: 
      if (userInput == criar):
          _createUser()
      elif (userInput == deletar):
          _deleteUser()
      elif (userInput == usuarios):
          _checkUsers()
      elif (userInput == status):
          _checkUserStatus()
      else:
          print ("Você não selecionou uma opção válida. Caso não esteja entendendo o problema, leia o ReadMe baixado junto ao arquivo.")
          start()

start()
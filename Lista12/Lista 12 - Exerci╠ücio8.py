#Exercício 8 - Um sistema precisa validar o cadastro de usuários com as seguintes regras:
# O nome completo deve conter pelo menos 5 caracteres e pelo menos um espaço (para garantir nome + sobrenome).
# O e-mail informado deve conter exatamente um caractere "@".
#O domínio do e-mail deve ser "example.com" (ou seja, o e-mail termina com "@example.com", sem considerar maiúsculas ou minúsculas).
# A senha deve conter pelo menos 8 caracteres.
# A senha não pode conter o nome do usuário (independente de maiúsculas/minúsculas).
#Se todas as condições forem atendidas, exibir "Cadastro válido", senão, informar qual regra falhou.

nome = input("Digite seu nome completo: ")
email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ")

# Verificar nome: pelo menos 5 caracteres e contém espaço
if len(nome) < 5:
    print("Nome muito curto")
elif nome.find(" ") == -1:
    print("Nome deve conter sobrenome")
# Verificar email: exatamente um '@' e termina com '@example.com' (case insensitive)
elif email.count("@") != 1:
    print("E-mail inválido: deve conter exatamente um '@'")
elif email.lower().find("@example.com") == -1:
    print("E-mail inválido: domínio deve ser '@example.com'")
# Verificar senha: pelo menos 8 caracteres e não contém o nome (case insensitive)
elif len(senha) < 8:
    print("Senha muito curta")
elif senha.lower().find(nome.lower()) != -1:
    print("Senha não pode conter o nome")
else:
    print("Cadastro válido")
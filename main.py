import os
import pickle

#########################################################################
#####                     Projeto PyHair - Versão 12                #####
#########################################################################
#####                      Sistema de Gestão para                   #####
#####                           cabeleireiros                       #####
#####             (CADASTRA SERVIÇOS, CLIENTES E AGENDAMENTOS)      #####
#####                         Desenvolvido por:                     #####
#####                          Fillipe Medeiros                     #####
#####                    Curso: Sistemas de Informação              #####
#####                         Universidade: UFRN                    #####
#####             Cadeira: Algoritmos e Lógica de Programação       #####
#####                     Professor: Flavius Gorgônio               #####
#########################################################################

### Dicionários:
### Créditos: Professor Flavius Gorgônio
servs = {}
try:
    arq_servs = open("servs.dat", "rb")
    servs = pickle.load(arq_servs)
except:
    arq_servs = open("servs.dat", "wb")
arq_servs.close()


clientes = {}
try:
    arq_clientes = open("clientes.dat", "rb")
    clientes = pickle.load(arq_clientes)
except:
    arq_clientes = open("clientes.dat", "wb")
arq_clientes.close()
    

agendamentos = {}
try:
    arq_agendamentos = open("agendamentos.dat", "rb")
    agendamentos = pickle.load(arq_agendamentos)
except:
    arq_agendamentos = open("agendamentos.dat", "wb")
arq_agendamentos.close()


################################################################
################################################################
##########               F u n ç õ e s                ##########
################################################################
################################################################

### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def menu_principal():
    os.system("clear")
    print("############################################")
    print("######         Projeto PyHair         ######")
    print("############################################")
    print("#####      1 - Serviços                #####")
    print("#####      2 - Clientes                #####")
    print("#####      3 - Agendamento             #####")
    print("#####      4 - Informações             #####")
    print("#####      0 - Sair                    #####")
    resp = input("##### Escolha sua opção: ")
    return resp


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def menu_servicos():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Seção de Serviços         ####")
    print("############################################")
    print("#####   1 - Cadastrar Serviço          #####")
    print("#####   2 - Exibir Serviços            #####")
    print("#####   3 - Alterar Serviço            #####")
    print("#####   4 - Excluir Serviço            #####")
    print("#####   0 - Retornar ao Menu           #####")
    resp2 = input("##### Escolha sua opção: ")
    return resp2


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def cadastrar_servico():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Cadastro Serviço         #####")
    print("############################################")
    print()
    serv = input("##### Serviço: ")
    print()
    preco = input("##### Preço: ")
    print()
    if not servs: 
        id = "1"
    else:
        id = int(sorted(servs.keys())[-1]) + 1
        id = str(id)
    servs[id] = [serv, preco]
    print("O serviço foi cadastrado com sucesso!")
    input("Tecle <ENTER> ou ↵ para continuar...")


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def exibir_servicos():
    os.system("clear")
    print()
    print("############################################")
    print("#####       Serviços Disponíveis       #####")
    print("############################################")
    print()
    for i in servs:
        print("\t\t","ID:", i, "-", servs[i][0], "-", "R$", servs[i][1]) 
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def alterar_servicos():
    os.system("clear")
    print()
    print("############################################")
    print("#####          Alterar Serviços        #####")
    print("############################################")
    print()
    id = input("##### ID do Serviço: ") 
    print()
    serv = input("##### Serviço: ")
    print()
    preco = input("##### Preço: ")
    if id in servs:
        servs[id] = [serv, preco]
        print()
        print("O serviço foi alterado com sucesso!")
    else:
        print()
        print("O serviço não existe!")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def excluir_servico():
    os.system("clear")
    print()
    print("############################################")
    print("#####          Excluir Serviço         #####")
    print("############################################")
    print()
    id = input("##### ID do Serviço: ")
    if id in servs:
        ctz = input("Tem certeza que deseja excluir o serviço? (S/N) ")
        if ctz.upper() == "S":
            del servs[id]
            print()
            print("O serviço foi excluído com sucesso!")
        else:
            print()
            print("O serviço não foi excluído!")
    else:
        print()
        print("O serviço não existe!")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")

#--------------------------------------------------------------------------------------------#

### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def menu_clientes():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Seção de Clientes         ####")
    print("############################################")
    print("#####   1 - Cadastrar Cliente          #####")
    print("#####   2 - Exibir Cliente             #####")
    print("#####   3 - Alterar Cadastro           #####")
    print("#####   4 - Excluir Cadastro           #####")
    print("#####   0 - Retornar ao Menu           #####")
    resp2 = input("##### Escolha sua opção: ")
    return resp2


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def cadastrar_cliente():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Cadastro Cliente         #####")
    print("############################################")
    print()
    nome = ler_nome()
    print()
    cpf = ler_cpf()
    print()
    fone = ler_fone()
    print()
    clientes[cpf] = [nome, fone]
    agendamentos[cpf] = []
    print("O cliente foi cadastrado com sucesso!")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def exibir_cliente():
    os.system("clear")
    print()
    print("############################################")
    print("#####        Exibir Dados Cliente      #####")
    print("############################################")
    print()
    opc_cliente = input("Deseja checar todos os clientes ou algum específico? (TODOS - 1 / PESSOA - 2): ")
    if opc_cliente == "1":
        for cpf in clientes:
            print()
            print("Nome:", clientes[cpf][0])
            print("CPF:", cpf)
            print("Telefone:", clientes[cpf][1])

    elif opc_cliente == "2":
        cpf = input("Qual o CPF do cliente?: ")
        if cpf in clientes:
            print()
            print("##### Nome: ", clientes[cpf][0])
            print("##### CPF: ", cpf)
            print("##### Celular: ", clientes[cpf][1])
        else:
            print()
            print("O cliente não existe!")
    else:
        print()
        print("Opção inválida!")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def alterar_cliente():
    os.system("clear")
    print()
    print("############################################")
    print("#####      Alterar Dados do Cliente    #####")
    print("############################################")
    print()
    cpf = input("Qual o CPF do cliente que deseja alterar?: ")
    if cpf in clientes:
        print()
        print("Insira os novos dados do cliente: ")
        nome = input("##### Nome: ")
        fone = input("##### Celular: ")
        clientes[cpf] = [nome, fone]
        print("O cliente foi alterado com sucesso!")
    else:
        print()
        print("O cliente não existe!")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def excluir_cliente():
    os.system("clear")
    print()
    print("############################################")
    print("#####          Excluir Cliente         #####")
    print("############################################")
    print()
    cpf = input("Qual o CPF do cliente que deseja excluir?: ")
    if cpf in clientes:
        ctz = input("Tem certeza que deseja excluir o cliente? (S/N) ")
        if ctz.upper() == "S":
            del clientes[cpf]
            print()
            print("O cliente foi excluído com sucesso!")
        else:
            print()
            print("O cliente não foi excluído!")
    else:
        print()
        print("O cliente não existe!")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")

#--------------------------------------------------------------------------------------------#

### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def menu_agendamento():
    os.system("clear")
    print()
    print("############################################")
    print("#####        Seção de Agendamento       ####")
    print("############################################")
    print("#####   1 - Realizar Agendamento       #####")
    print("#####   2 - Exibir Agendamentos        #####")
    print("#####   3 - Alterar Agendamento        #####")
    print("#####   4 - Excluir Agendamento        #####")
    print("#####   0 - Retornar ao Menu           #####")
    resp2 = input("##### Escolha sua opção: ")
    return resp2


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def cadastrar_agendamento():
    os.system("clear")
    print()
    print("############################################")
    print("#####        Realizar Agendamento      #####")
    print("############################################")
    print()
    cpf_agenda = input("##### CPF: ")
    print()
    serv_agenda = input("##### Serviço: ")
    print()
    dia_agenda = input("##### Dia: ")
    print()
    hora_agenda = input("##### Hora: ")
    print()
    if serv_agenda in servs:
        agendamentos[cpf_agenda].append([serv_agenda, dia_agenda, hora_agenda])
        print("O agendamento foi realizado com sucesso!")
    else:
        print("O serviço não existe!")
        print("Tente novamente!")
    input("Tecle <ENTER> ou ↵ para continuar...")


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def exibir_agendamento():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Exibir Agendamentos      #####")
    print("############################################")
    print()
    opc_agenda = input("Deseja checar os agendamentos do dia ou de algum cliente específico? (DIA - 1 / CLIENTE - 2): ")
    if opc_agenda == "1":
        print()
        dia_agenda = input("Desejar checar os agendamentos de qual dia?: ")
        bool = False
        for i in agendamentos:
            for j in range(len(agendamentos[i])):
                if agendamentos[i][j][1] == dia_agenda:
                    print()
                    print("##### Nome: ", clientes[i][0])
                    print("##### Serviço: ", agendamentos[i][j][0])
                    print("##### Dia: ", agendamentos[i][j][1])
                    print("##### Hora: ", agendamentos[i][j][2])
                    print()
                    bool = True
        if bool == False:
            print()
            print("Não há agendamentos nesse dia!")

    elif opc_agenda == "2":
        print()
        cpf_agenda = input("Desejar checar os agendamentos de qual cliente? (Insira o CPF): ")
        if cpf_agenda in agendamentos:
            for i in range(len(agendamentos[cpf_agenda])):
                print()
                print("##### Serviço: ", agendamentos[cpf_agenda][i][0])
                print("##### Dia: ", agendamentos[cpf_agenda][i][1])
                print("##### Hora: ", agendamentos[cpf_agenda][i][2])
        else:
            print()
            print("Não existem agendamentos nesse CPF!")
            print("Tente novamente!")
    else:
        print()
        print("Opção inválida!")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")
        

### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def alterar_agendamento():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Alterar Agendamento      #####")
    print("############################################")
    print()
    cpf_agenda = input("Em qual CPF foi cadastrado o agendamento?: ")
    if cpf_agenda in agendamentos:
        bool = False
        dia_agenda = input("Para qual dia o serviço tinha sido agendado?: ")
        serv_agenda = "1"
        for i in range(len(agendamentos[cpf_agenda])):
            if agendamentos[cpf_agenda][i][1] == dia_agenda:
                print()
                print("Insira os novos dados do agendamento: ")
                serv_agenda = input("##### Serviço: ")
                dia_agenda = input("##### Dia: ")
                hora_agenda = input("##### Hora: ")
                bool = True
        if serv_agenda in servs:
            if bool is False:
                print()
                print("Não existem agendamentos nesse dia!")
                print("Tente novamente!")
            else:
                agendamentos[cpf_agenda][i] = [serv_agenda, dia_agenda, hora_agenda]
                print("O agendamento foi alterado com sucesso!")
        else:
            print()
            print("O serviço não existe!")
            print("Tente novamente!")
    else:
        print()
        print("Não existem agendamentos nesse CPF!")
        print("Tente novamente!")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def excluir_agendamento():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Excluir Agendamento      #####")
    print("############################################")
    print()
    cpf_agenda = input("Em qual CPF foi cadastrado o agendamento?: ")
    if cpf_agenda in agendamentos:
        bool = False
        tam = len(agendamentos[cpf_agenda])
        dia_agenda = input("Para qual dia foi feito o agendamento?: ")
        for i in range(tam):
            if agendamentos[cpf_agenda][i][1] == dia_agenda:
                excluir = agendamentos[cpf_agenda][i]
                bool = True
        if bool == False:
            print()
            print("Não existem agendamentos nesse dia!")
            print("Tente novamente!")
        else:
            ctz = input("Tem certeza que deseja excluir o agendamento? (S/N)")
            if ctz.upper() == "S":
                agendamentos[cpf_agenda].remove(excluir)
                print()
                print("O agendamento foi excluído com sucesso!")
            else:
                print()
                print("O agendamento não foi excluído!")
    else:
        print()
        print("Não existem agendamentos nesse CPF!")
        print("Tente novamente!")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")

#--------------------------------------------------------------------------------------------#

### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
def menu_informacoes():
    os.system("clear")
    print()
    print("############################################")
    print("#####        Seção de Informações       ####")
    print("############################################")
    print()
    print("### Projeto de Gestão para Cabeleireiros ###")
    print("##### Equipe de desenvolvimento:        ####")
    print("##### Fillipe Medeiros @fillipemdrs     ####")
    print("##### fillipe.morais.095@ufrn.edu.br    ####")
    print("##### (83)98131-6252                    ####")
    print("##### Parceiros do projeto:             ####")
    print("##### Prof. Flavius Gorgônio @flgorgonio ####")
    print()
    input("Tecle <ENTER> ou ↵ para continuar...")

#--------------------------------------------------------------------------------------------#

### Créditos: Professor Flavius Gorgônio 
def valida_cpf(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    tam = len(cpf)
    soma = 0
    d1 = 0
    d2 = 0

    if tam != 11:
        return False

    for i in range(11):
        if cpf[i] < '0' or cpf[i] > '9':
            return False

    for i in range(9):
        soma += (int(cpf[i]) * (10 - i))
    d1 = 11 - (soma % 11)
    if d1 == 10 or d1 == 11:
        d1 = 0
    if d1 != int(cpf[9]):
        return False

    soma = 0
    for i in range(10):
        soma += (int(cpf[i]) * (11 - i))
    d2 = 11 - (soma % 11)
    if d2 == 10 or d2 == 11:
        d2 = 0
    if d2 != int(cpf[10]):
        return False

    return True


### Créditos: Professor Flavius Gorgônio
def valida_nome(nome):
    nome = nome.replace(' ', '')
    return bool(nome.isalpha())


### Créditos: Professor Flavius Gorgônio
def valida_fone(fone):
    fone = fone.replace(' ', '')
    fone = fone.replace('-', '')
    fone = fone.replace('(', '')
    fone = fone.replace(')', '')
    fone = fone.replace('+', '')
    tam = len(fone)
    if tam < 11:
        return False
    if not(fone.isdigit()):
        return False
    return True

#--------------------------------------------------------------------------------------------#

### Créditos: Professor Flavius Gorgônio
def ler_cpf():
    cpf = input("##### CPF: ")
    while not(valida_cpf(cpf)):
        print()
        print("CPF inválido!")
        print("Tente novamente!")
        print()
        cpf = input("##### CPF: ")
    return cpf


### Créditos: Professor Flavius Gorgônio
def ler_nome():
    nome = input("##### Nome: ")
    while not(valida_nome(nome)):
        print()
        print("Nome inválido!")
        print("Tente novamente!")
        print()
        nome = input("##### Nome: ")
    return nome


### Créditos: Professor Flavius Gorgônio
def ler_fone():
    fone = input("##### Celular: ")
    while not(valida_fone(fone)):
        print()
        print("O número de celular é inválido!")
        print("Tente novamente!")
        print()
        fone = input("##### Celular: ")
    return fone

################################################################
################################################################
##########    P R O G R A M A   P R I N C I P A L     ##########
################################################################
################################################################


### Créditos do modelo de interface (Adaptado): Professor Flavius Gorgônio
resp = ""

while resp != "0":
    resp = menu_principal()

    if resp == "1":
        resp2 = ""
        while resp2 != "0":
            resp2 = menu_servicos()
            print()
            if resp2 == "1":
                cadastrar_servico()
            elif resp2 == "2":
                exibir_servicos()
            elif resp2 == "3":
                alterar_servicos()
            elif resp2 == "4":
                excluir_servico()

    elif resp == "2":
        resp2 = ""
        while resp2 != "0":
            resp2 = menu_clientes()
            print()
            if resp2 == "1":
                cadastrar_cliente()
            if resp2 == "2":
                exibir_cliente()
            if resp2 == "3":
                alterar_cliente()
            if resp2 == "4":
                excluir_cliente()

    elif resp == "3":
        resp2 = ""
        while resp2 != "0":
            resp2 = menu_agendamento()
            print()
            if resp2 == "1":
                cadastrar_agendamento()
            if resp2 == "2":
                exibir_agendamento()
            if resp2 == "3":
                alterar_agendamento()
            if resp2 == "4":
                excluir_agendamento()

    elif resp == "4":
        resp = menu_informacoes()

os.system("clear")
print("O programa foi encerrado!")
print("Até mais, obrigado por usar o PyHair!")    

### Salvando os dados nos arquivos
### Créditos: Professor Flavius Gorgônio

arq_servs = open("servs.dat", "wb")
pickle.dump(servs, arq_servs)
arq_servs.close()

arq_clientes = open("clientes.dat", "wb")
pickle.dump(clientes, arq_clientes)
arq_clientes.close()

arq_agendamentos = open("agendamentos.dat", "wb")
pickle.dump(agendamentos, arq_agendamentos)
arq_agendamentos.close()
# func para formatar os nomes
def create_mail(full_name, count, mail_created):
    interlist = []

    if len(full_name) < 3:
        interlist.append(full_name[-1].strip())
        mail_created.append(interlist[-1]+"."+full_name[0][0])

    elif len(full_name) > 2:
        interlist.append(full_name[-1].strip())
        mail_created.append(
            interlist[-1]+"."+full_name[0][0]+"."+full_name[1][0])
    return mail_created


# variáveis
final_list = []
mail_created = []
lines = []

# dic para trackear nomes repetidos
compare_list = {}

# operando o arquivo
try:
    names_list = open("arqnomes.txt", "r")
    lines = names_list.readlines()
except OSError as err:
    print("OS error: {0}".format(err))
finally:
    names_list.close()

# loop para formatação dos nomes da lista
try:
    for line in iter(lines):
        # separa os nomes
        auxiliar = line.split(" ")
        # chama função de formatação dos nomes
        mail_created = create_mail(auxiliar, int(len(auxiliar)), mail_created)
except:
    print("Erro na formatação dos nomes")

try:
    # nomes => lowercase
    for i in range(len(mail_created)):
        mail_created[i] = mail_created[i].lower()

    # trackeando e alterando nomes repetidos
    try:
        aux = 0
        for i in mail_created:
            if i in compare_list:
                compare_list[i] += 1
                mail_created[aux] = i + str(compare_list[i])
            else:
                compare_list[i] = 0
            aux += 1
    except:
        print("Erro no tracking de duplicatas")

    # adicionar o domínio da empresa
    for i in range(len(mail_created)):
        mail_created[i] = str(mail_created[i]) + "@company.com"

    # retirar hífens
    for string in mail_created:
        auxlist = string.replace("-", "")
        final_list.append(auxlist)

    # output do resultado dos e-mails
    count = 0
    for line in lines:
        print("<"+final_list[count]+"> "+line)
        count = count + 1

except Exception as err:
    print(err)

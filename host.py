def config(host):
    print("host "+host[1]+" {\n\thardware ethernet "+host[0]+";\n\tfixed-address "+host[2]+";}\n}")


ip = "172.21.2."
mac = "01:01:01:01:01:01"

lista = []

with open("ips/02.txt") as file:

    cont = 1
    for line in file:

        if "reserva" in line:
            lista.append([mac,"reserva",ip + str(cont)])

        else:
            linha = line.split()
            linha.append(ip + str(cont))
            lista.append(linha)

        cont += 1

    for host in lista:
        config(host)
# host WIN-SERVER {
#   hardware ethernet 00:0c:19:bc:2e:e1;
#   fixed-address 192.168.1.7;}
# }

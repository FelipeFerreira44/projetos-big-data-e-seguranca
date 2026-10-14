# Firewall pfSense com DMZ

Trabalho de Segurança da Informação / Redes (PUCPR), em equipe: implementação de uma arquitetura de firewall com DMZ usando pfSense em máquinas virtuais (VirtualBox).

## Topologia
Três redes interligadas pelo pfSense:

| Rede | Interface | Endereço |
|---|---|---|
| WAN (Internet virtual) | em0 | 10.0.2.15/24 |
| LAN (PC) | em1 | 192.168.1.1/24 (pfSense); PC em 192.168.1.100 via DHCP |
| DMZ (Webserver) | em2 | 192.168.2.1/24 (pfSense); Webserver em 192.168.2.10 |

## Regras
**LAN**: permitir HTTP/HTTPS para a Internet; DNS para servidores externos; HTTP e SSH para o Webserver da DMZ.
**DMZ**: bloquear acesso à LAN e à Internet (negação por padrão).
**WAN**: permitir acesso externo ao Webserver (192.168.2.10, porta 80).
**Demais tráfego**: bloqueado pela política implícita de negação do pfSense.

## Testes
Os testes foram feitos a partir das VMs: `curl` e `ssh` do PC ao Webserver, `nslookup` com servidor DNS externo.
A regra da WAN foi configurada, mas **não foi testada** por limitações de rede do VirtualBox.



## Tecnologias
pfSense, VirtualBox, regras de firewall, DMZ, DHCP, DNS, HTTP/SSH.

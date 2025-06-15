"""
Grade 100%

Pregunta 1
¿Qué tráfico bloquea una regla de denegación implícita en un firewall?
✅ All traffic that is not explicitly permitted or allowed

Una regla de denegación implícita (implicit deny) significa que todo lo que no está permitido explícitamente, se bloquea por defecto.

Pregunta 2
¿Qué característica de switch empresarial protege contra ataques de servidores DHCP falsos?
✅ DHCP Snooping

Esta función valida los mensajes DHCP y bloquea servidores DHCP no autorizados.

Pregunta 3
¿Qué se puede configurar para permitir conexiones remotas seguras a aplicaciones web sin usar VPN?
✅ Reverse proxy

Un reverse proxy puede manejar autenticación, cifrado SSL, y redirigir el tráfico a servidores internos de forma segura.

Pregunta 4
¿Qué cifrado simétrico subyacente usa WEP?
✅ RC4

WEP usa RC4, un cifrado de flujo ya obsoleto y vulnerable.

Pregunta 5
¿Qué método WPS introduce vulnerabilidades críticas?
✅ Pin-entry authentication with a hard-coded PIN

Esta opción es insegura porque los PINs codificados pueden ser forzados fácilmente con ataques automatizados.

Pregunta 6
¿Qué herramienta se puede usar para asegurarte de que WPS esté deshabilitado en tus APs?
✅ Wash

wash es parte del conjunto de herramientas Reaver y sirve para escanear redes Wi-Fi en busca de WPS habilitado.

Pregunta 7
¿Qué característica de switches gestionados permite capturar todos los paquetes de un puerto o VLAN y replicarlos a otro puerto?
✅ Port mirroring

Ideal para diagnósticos o para configurar un IDS/NIDS.

Pregunta 8
¿Qué restricción debes considerar al configurar un sistema NIDS?
✅ You must be able to monitor and access all traffic, not just the traffic flowing directly through the NIDS device.

NIDS funciona pasivamente, por lo tanto, debes enrutar/copiar el tráfico (con port mirroring) para que pueda verlo.

Pregunta 9
¿Qué comando tcpdump es correcto para IP 113.8.81.2 y puerto 8080?
✅ sudo tcpdump -i eth0 -vn host 113.8.81.2 and port 8080 &

Este comando filtra por IP de host y puerto, capturando como origen o destino.

Pregunta 10
¿Qué muestra tcpdump al ejecutar sudo tcpdump -i eth0 -vn?
✅ IP header details
✅ TCP details
✅ The layer 3 protocol, source, and destination addresses and ports
✅ Service names commonly associated with the detected port numbers

El modo -vn de tcpdump es verbose y no resuelve nombres DNS, pero sí muestra información detallada de protocolos y puertos.
8.
Question 8
You’re an IT support specialist tasked with setting up a NIDS system to monitor your company’s network traffic for suspicious behavior. Which constraint must you consider when you set up the NIDS?

The NIDS must have access to all incoming traffic.
The monitored traffic must pass through the NIDS. X
You must be able to monitor and access all traffic, not just the traffic flowing directly through the NIDS device.*
The NIDS must have access to all outgoing traffic.

2.
Question 2
Which enterprise switch features protect against layer 2 man-in-the-middle attacks? Select all that apply.

Dynamic ARP inspection (DAI)*
IP Source Guard x
Flood Guard x
DHCP Snooping*


4.
Question 4
Multiple vulnerabilities in the WEP protocol make it possible for the encryption key to be recovered by hackers. Which parts of the WEP protocol create this vulnerability? Select all that apply.

The initialization vectors, and therefore the encryption keys, were weak and reused too often.*
WEP encryption is limited to a 64-bit protocol. x
In shared-key WEP authentication mode, the Access Point (AP) shares both the plaintext and the ciphertext with the client.*
In open-system WEP authentication mode, the client can be authenticated by the Access Point (AP) without passing the decryption challenge. x

10.
Question 10
Complete the Qwiklab 
Introduction to tcpdump
 or review 
the exemplar
 before answering this question. 

When you run the command sudo tcpdump -i eth0 -vn, what output does tcpdump provide about each packet? Select all that apply. 


IP header details.*
Service names commonly associated with the detected port numbers.x
The layer 3 protocol, source, and destination addresses and ports. *
TCP details.*
"""

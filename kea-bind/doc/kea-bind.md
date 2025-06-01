## Playbook de Ansible de Kea, Bind, Radvd y iptables:

Con este playbook se implementa un servidor dhcp(kea), un servidor dns(bind) y unas reglas de iptables para redireccionar tráfico de una read interna al exterior, todo con soporte ipv6.

### Requisitos

Necesitaremos una máquina debian con las siguientes carácterísticas:
- Dos interfaces de red que serán:
  - wan: será el que tenga salida al exterior desde la red interna y por la que conecta ansible. Esta deberá estar previamente configurada con ip estática o dhcp con reserva.
  - lan: será el adaptador para la red interna y por el que se servirá dhcp y dns. Se configurará mediante un rol en el playbook.
- Instalado el paquete de python
- Instalado y configurado el servidor de ssh para la autentificación por claves.

### Estructura de directorios.

La estructura 




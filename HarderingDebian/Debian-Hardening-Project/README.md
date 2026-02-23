#  Debian Hardening & Security Audit

Este proyecto documenta el proceso de endurecimiento (*hardening*) y auditoría de seguridad realizado sobre un servidor **Debian 12**, logrando un **Hardening Index de 80+** en la suite de auditoría **Lynis**.

##  Tecnologías Utilizadas
* **OS:** Debian GNU/Linux
* **Audit:** Lynis 3.1.6
* **HIDS:** AIDE (Advanced Intrusion Detection Environment)
* **Auth:** OpenSSH, PBKDF2 (GRUB)
* **Kernel:** Modprobe (Hardening de módulos)

##  Implementaciones Realizadas

### 1. Seguridad en el Arranque y Acceso
- [x] Configuración de contraseña en **GRUB** con hash PBKDF2 para evitar edición no autorizada.
- [x] Hardening de **OpenSSH**: Desactivación de protocolos antiguos, ajuste de `LogLevel` a VERBOSE y restricción de `AllowTcpForwarding`.

### 2. Integridad del Sistema
- [x] Despliegue de **AIDE** para el monitoreo de integridad de archivos críticos.
- [x] Automatización de la base de datos de firmas de integridad.

### 3. Reducción de Superficie de Ataque
- [x] **Blacklist de Kernel:** Desactivación de drivers innecesarios (USB Storage, Firewire, Thunderbolt).
- [x] Desactivación de protocolos de red raros (DCCP, SCTP, RDS, TIPC).
- [x] Restricción de permisos en compiladores (GCC) solo para root.

##  Resultados de Auditoría
> "Great, no warnings" - Reporte final de Lynis.
> **Hardening Index: 80/100**

---
**Desarrollado por [ Claudio F Morales/ AdminSecurityPro]** *Ingeniero Electrónico | SysAdmin | DevOps Enthusiast*
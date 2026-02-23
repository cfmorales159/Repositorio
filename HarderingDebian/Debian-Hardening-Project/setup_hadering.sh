echo "--- Iniciando Hardening de Sistema ---"

# 1. Restricción de Compiladores (Solo root)
echo "[+] Protegiendo binarios de compilación..."
chmod 700 /usr/bin/gcc /usr/bin/make 2>/dev/null || true

# 2. Configuración de Banner Legal
echo "[+] Configurando Banner de acceso legal..."
echo "ACCESO RESTRINGIDO: Solo personal autorizado. Toda actividad es monitoreada." > /etc/issue.net

# 3. Hardening de SSH (Ejemplo de parámetros críticos)
echo "[+] Verificando parámetros de SSH..."
# LogLevel VERBOSE ayuda a Lynis y auditorías forenses
sed -i 's/#LogLevel INFO/LogLevel VERBOSE/' /etc/ssh/sshd_config 2>/dev/null || echo "Revisar sshd_config manualmente"

# 4. Finalización
echo "--- Proceso completado. Hardening Index sugerido: 80+ ---"
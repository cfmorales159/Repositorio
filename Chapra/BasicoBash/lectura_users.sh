#!/bin/bash
#!/bin/bash
# Archivos de entrada
lista="new.txt"
lista2="old.txt"

# Archivos de salida
repetidos="usuarios_repetidos.txt"
nuevos_con_clave="usuarios_con_clave.txt"

# Limpiar archivos anteriores si existen
cat /dev/null > $repetidos
cat /dev/null > $nuevos_con_clave
# Leer ambas listas y encontrar los repetidos
while read -r new; do
    if grep -q "^$new$" "$lista2"; then
        echo "$new" >> "$repetidos"
    else
        clave=$(pwgen -n1 )
        echo "$new $clave" >> "$nuevos_con_clave"
    fi
done < "$lista"

echo "Comparación completa."
echo "Repetidos guardados en: $repetidos"
echo "Nuevos con clave en:   $nuevos_con_clave"




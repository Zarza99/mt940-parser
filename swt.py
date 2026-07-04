"""
Proyecto: Procesador de archivos MT940
Autor: Jhonatan Zarza
Fecha: Septiembre 2025

Descripción:
Aplicación desarrollada en Python para procesar archivos
bancarios en formato MT940. El sistema analiza el contenido
del archivo, identifica los movimientos financieros, extrae
la información relevante y la exporta a un archivo CSV para
su posterior análisis o integración con otros sistemas.

"""

import re
import pandas as pd
import glob
import os

#Carpeta de los archivos
carpeta = "./mt940"

#Archivos para procesar
archivos = glob.glob(os.path.join(carpeta, "*.txt"))

todas_filas = []

for archivo in archivos:
    with open(archivo, "r", encoding="utf-8") as f:
        data = f.read()

    #Buscar movimientos (:61: ... seguido de :86:)
    movimientos = re.findall(r":61:(.*?)\n:86:(.*?)\n", data, re.DOTALL)

    for mov, desc in movimientos:
        try:
            fecha = "20" + mov[0:6]  # AAAAMMDD
            signo = "D" if "D" in mov else "C"

            #Patrón corregido para DR/CR
            match_importe = re.search(r"[DC][A-Z]?(\d+,\d+)", mov)
            importe = match_importe.group(1).replace(",", ".") if match_importe else "0.0"

            #Mantener acentos y reemplazar solo comas para CSV
            desc_seguro = desc.replace(",", ";").strip()
            
            todas_filas.append({
                "Archivo": os.path.basename(archivo),
                "Fecha": fecha,
                "Signo": signo,
                "Importe": float(importe),
                "Descripcion": desc_seguro
            })
        except Exception as e:
            print(f"Error procesando movimiento en {archivo}: {mov} -> {e}")

#Exportar todas las transacciones a un archivo CSV
df = pd.DataFrame(todas_filas)
df.to_csv("extractos_consolidados.csv", index=False, encoding="utf-8-sig")

print(f"\nArchivos procesados: {len(archivos)} archivos.")
print(f"Archivo exportado: extractos_consolidados.csv con {len(df)} movimientos.\n")
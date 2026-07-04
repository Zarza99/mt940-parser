#Conversor de MT940 a CSV:

Aplicación en Python que procesa archivos de extractos bancarios en formato **MT940** y exporta los datos de las transacciones a un archivo **CSV** consolidado.

#Descripción general:

Este proyecto automatiza la extracción de información de transacciones a partir de archivos de extractos bancarios MT940. Lee uno o varios archivos MT940,
procesa los registros de transacciones y genera un archivo CSV que puede abrirse en aplicaciones de hoja de cálculo como Microsoft Excel.

#Características:

* Procesamiento de archivos de extractos bancarios MT940.
* Procesamiento de múltiples archivos desde un mismo directorio.
* Extracción de la fecha de la transacción.
* Identificación de transacciones de débito y crédito.
* Extracción del importe de la transacción.
* Exportación de todas las transacciones a un único archivo CSV.
* Generación de CSV codificado en UTF-8 con BOM para compatibilidad con Excel.

#Tecnologías

* Python 3
* pandas
* re (Expresiones regulares)
* glob
* os

#Instalación

Clona el repositorio:

```bash
git clone https://github.com/Zarza99/mt940-to-csv.git
```

Instala la dependencia necesaria:

```bash
pip install pandas
```

#Uso

1. Crea una carpeta llamada `mt940`.
2. Copia los archivos `.txt` en formato MT940 dentro de esa carpeta.
3. Ejecuta la aplicación:

```bash
python swt.py
```

El programa generará:

```
extractos_consolidados.csv
```

que contendrá las transacciones extraídas.

#Ejemplo de salida

| Archivo     | Fecha    | Signo | Importe | Descripción   |
| ----------- | -------- | ----- | ------- | ------------- |
| estado1.txt | 20250115 | D     | 1500.00 | Payment       |
| estado2.txt | 20250116 | C     | 250.50  | Transferencia |


#Autor

**Jhonatan Zarza**

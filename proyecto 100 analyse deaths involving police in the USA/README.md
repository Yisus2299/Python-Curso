# Análisis de Muertes Policiales en EE.UU.

Este proyecto analiza datos de muertes por disparos policiales en Estados Unidos junto con datos socioeconómicos del censo.

## Archivos esperados

- `fatal-police-shootings-data.csv` o `police_killings.csv`: datos de muertes en enfrentamientos con policía.
- `us_census_data.csv` o `census_by_state.csv`: datos del censo por estado, incluyendo tasa de pobreza, tasa de graduación de secundaria, ingreso medio del hogar y demografía racial.

## Uso

1. Coloca los archivos CSV en la misma carpeta que `main.py`.
2. Instala dependencias si no las tienes:

```bash
pip install pandas matplotlib seaborn
```

3. Ejecuta el script:

```bash
python main.py
```

> Si `python` no se reconoce en PowerShell, usa el intérprete completo:
>
> ```powershell
> & "C:/Users/ImKen/AppData/Local/Python/pythoncore-3.14-64/python.exe" main.py
> ```
>
> O si prefieres un alias temporal dentro de esa sesión:
>
> ```powershell
> set-alias python "C:/Users/ImKen/AppData/Local/Python/pythoncore-3.14-64/python.exe"
> python main.py
> ```

4. Si los archivos tienen nombres distintos, usa:

```bash
python main.py --shootings ruta/del/archivo.csv --census ruta/del/censo.csv
```

5. Los gráficos generados se guardarán en la carpeta `analysis_output`.

## Qué hace el script

- Carga y normaliza los datos de muertes policiales y censo.
- Calcula el número de muertes por estado.
- Combina los datos con indicadores socioeconómicos.
- Reporta correlaciones entre:
  - tasa de pobreza
  - tasa de graduación de secundaria
  - ingreso medio del hogar
  - muertes policiales por 100k
- Analiza la distribución racial de las muertes.
- Genera gráficos de relación entre muertes policiales y los indicadores principales.

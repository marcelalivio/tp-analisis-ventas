import pandas as pd
import matplotlib.pyplot as plt

# cargar datos
df = pd.read_csv("datos/sales_sample_2024.csv")

# convertir fechas
df["sales_date"] = pd.to_datetime(df["sales_date"])

# métricas principales
total_ventas = df["sales_amount"].sum()
promedio_diario = df["sales_amount"].mean()

mejor_dia = df.loc[df["sales_amount"].idxmax()]
peor_dia = df.loc[df["sales_amount"].idxmin()]

# resumen
resumen = pd.DataFrame({
    "metrica": [
        "Total ventas",
        "Promedio diario",
        "Mejor día",
        "Peor día"
    ],
    "valor": [
        total_ventas,
        promedio_diario,
        mejor_dia["sales_date"],
        peor_dia["sales_date"]
    ]
})

resumen.to_csv("resultados/resumen_ventas.csv", index=False)

# gráfico
plt.figure(figsize=(12,6))
plt.plot(df["sales_date"], df["sales_amount"])
plt.title("Ventas diarias 2024")
plt.xlabel("Fecha")
plt.ylabel("Monto de ventas")
lt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("resultados/ventas_diarias.png")

print("Análisis completado correctamente.")

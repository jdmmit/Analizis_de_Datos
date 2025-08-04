import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Configurar semilla para reproducibilidad (puedes cambiarla para diferentes datasets)
np.random.seed(42)
n = 10000000

# Generar variables predictoras con diferentes distribuciones
print("Generando dataset sintético para regresión lineal...")

# Variable 1: Número de habitaciones (distribución normal)
rooms = np.clip(np.random.normal(loc=6.0, scale=1.2, size=n), 3.0, 10.0)

# Variable 2: Distancia al centro (distribución exponencial para mayor dispersión)
distance = np.random.exponential(scale=4.0, size=n)
distance = np.clip(distance, 0.5, 25.0)

# Variable 3: Edad de la casa (distribución uniforme)
age = np.random.uniform(low=1, high=100, size=n)

# Variable 4: Índice de criminalidad (distribución gamma para asimetría)
crime_rate = np.random.gamma(shape=2, scale=2, size=n)
crime_rate = np.clip(crime_rate, 0.1, 20.0)

# Variable 5: Ratio estudiante-profesor (distribución normal con outliers)
student_teacher_ratio = np.random.normal(loc=18, scale=3, size=n)
# Agregar algunos outliers
outlier_indices = np.random.choice(n, size=int(0.05*n), replace=False)
student_teacher_ratio[outlier_indices] += np.random.normal(0, 10, len(outlier_indices))
student_teacher_ratio = np.clip(student_teacher_ratio, 10, 35)

# CREAR LA VARIABLE OBJETIVO CON RELACIONES REALISTAS
# El precio de la casa depende de las variables predictoras + ruido
base_price = 50  # precio base

# Relaciones con las variables (coeficientes realistas)
price_from_rooms = rooms * 8.5  # más habitaciones = mayor precio
price_from_distance = -distance * 1.2  # mayor distancia = menor precio
price_from_age = -age * 0.15  # casas más viejas = menor precio
price_from_crime = -crime_rate * 2.3  # mayor criminalidad = menor precio
price_from_ratio = -student_teacher_ratio * 0.8  # peor ratio = menor precio

# Agregar interacciones no lineales para mayor complejidad
interaction_1 = (rooms * distance) * 0.05  # interacción rooms-distance
interaction_2 = np.log(age + 1) * crime_rate * 0.3  # interacción no lineal

# Calcular precio base
house_price = (base_price + 
               price_from_rooms + 
               price_from_distance + 
               price_from_age + 
               price_from_crime + 
               price_from_ratio + 
               interaction_1 - 
               interaction_2)

# Agregar ruido significativo para mayor dispersión
noise_level = 0.25  # 25% de ruido
noise = np.random.normal(0, house_price.std() * noise_level, size=n)
house_price += noise

# Asegurar precios positivos y realistas
house_price = np.clip(house_price, 5.0, 100.0)

# Crear DataFrame
df = pd.DataFrame({
    'Rooms': np.round(rooms, 1),
    'Distance_to_Center': np.round(distance, 2),
    'House_Age': np.round(age, 0),
    'Crime_Rate': np.round(crime_rate, 2),
    'Student_Teacher_Ratio': np.round(student_teacher_ratio, 1),
    'House_Price': np.round(house_price, 2)
})

# Agregar algunas variables categóricas para mayor realismo
neighborhoods = ['Downtown', 'Suburbs', 'Residential', 'Industrial', 'Commercial']
df['Neighborhood'] = np.random.choice(neighborhoods, size=n, 
                                    p=[0.15, 0.35, 0.25, 0.15, 0.10])

# Tipo de casa
house_types = ['Apartment', 'House', 'Condo', 'Townhouse']
df['House_Type'] = np.random.choice(house_types, size=n,
                                  p=[0.30, 0.40, 0.20, 0.10])

# Reordenar columnas (variable objetivo al final)
columns_order = ['Rooms', 'Distance_to_Center', 'House_Age', 'Crime_Rate', 
                'Student_Teacher_Ratio', 'Neighborhood', 'House_Type', 'House_Price']
df = df[columns_order]

# Guardar el dataset
df.to_csv('boston_sintetico.csv', index=False)

# Mostrar estadísticas básicas
print(f"\nDataset generado exitosamente!")
print(f"Forma del dataset: {df.shape}")
print(f"\nPrimeras 5 filas:")
print(df.head())
print(f"\nEstadísticas descriptivas:")
print(df.describe().round(2))

# Mostrar correlaciones con la variable objetivo
print(f"\nCorrelaciones con House_Price:")
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlations = df[numeric_cols].corr()['House_Price'].sort_values(ascending=False)
for col, corr in correlations.items():
    if col != 'House_Price':
        print(f"{col}: {corr:.3f}")

print(f"\nArchivo 'boston_sintetico.csv' guardado exitosamente!")
print(f"El dataset tiene {n} observaciones con relaciones realistas entre variables.")
print(f"Perfecto para practicar regresión lineal múltiple!")
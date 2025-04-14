import pandas as pd
import numpy as np

# Generación de datos de ejemplo para el transporte masivo
np.random.seed(42)

# Número de registros
num_records = 1000

# Generación de datos sintéticos
data = {
    "bus_id": np.random.choice(["bus_1", "bus_2", "bus_3", "bus_4"], num_records),
    "latitude": np.random.uniform(4.5, 4.8, num_records),  # Latitud en la zona de La Dorada
    "longitude": np.random.uniform(-74.8, -74.5, num_records),  # Longitud en la zona de La Dorada
    "passenger_count": np.random.randint(0, 40, num_records),
    "route": np.random.choice(["route_1", "route_2", "route_3"], num_records),
    "speed": np.random.uniform(10, 60, num_records),  # Velocidad en km/h
    "weather_condition": np.random.choice(["Sunny", "Rainy", "Cloudy"], num_records),
    "time_of_day": np.random.choice(["Morning", "Afternoon", "Evening"], num_records),
    "traffic_level": np.random.choice([1, 2, 3], num_records),  # 1: Low, 2: Medium, 3: High
    "timestamp": pd.date_range(start="2025-04-01", periods=num_records, freq="T")
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Guardar el DataFrame a un archivo CSV
df.to_csv("transporte_masivo_dataset.csv", index=False)

print(df.head())

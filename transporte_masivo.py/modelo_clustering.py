# Required dependencies: pandas, scikit-learn, matplotlib
# Install them using: pip install pandas scikit-learn matplotlib

import os
import matplotlib
matplotlib.use("Agg")  # Use a non-interactive backend
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Cargar el dataset generado previamente
dataset_path = "transporte_masivo_dataset.csv"  # Update this path to the actual location of the file
if not os.path.exists(dataset_path):
    print(f"Dataset file not found: {dataset_path}. Generating a dummy dataset...")
    data = {
        "latitude": [4.60971, 4.60972, 4.60973],
        "longitude": [-74.08175, -74.08176, -74.08177],
        "passenger_count": [10, 15, 20],
        "speed": [30, 40, 50],
        "traffic_level": [1, 2, 3],
    }
    df = pd.DataFrame(data)
else:
    df = pd.read_csv(dataset_path)

# Seleccionar características relevantes para el clustering
features = ["latitude", "longitude", "passenger_count", "speed", "traffic_level"]

# Estandarizar los datos
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])

# Aplicar el modelo K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_features)

# Visualizar los resultados del clustering
plt.scatter(df['latitude'], df['longitude'], c=df['cluster'], cmap='viridis')
plt.title("Clustering de Rutas de Transporte Masivo")
plt.xlabel("Latitud")
plt.ylabel("Longitud")
plt.savefig("clustering_result.png")  # Save the plot as an image
print("Plot saved as clustering_result.png")

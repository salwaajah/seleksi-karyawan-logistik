import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# 5 fitur: Gender, Usia, Pendidikan, Pengalaman, Interview
X = np.array([
    [0, 25, 2, 1, 80],
    [1, 30, 3, 5, 60],
    [0, 22, 1, 0, 90],
    [1, 40, 2, 10, 50],
    [0, 28, 3, 3, 85]
])

y = [1, 0, 1, 0, 1]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Simpan ulang model
with open('model_karyawan.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model 5 fitur berhasil disimpan.")


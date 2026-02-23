import matplotlib.pyplot as plt

# 1. Veri setini tanımlayalım
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

def calculate_regression(x, y):
    n = len(x)
    
    # Ortalama değerleri hesapla
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Eğim (m) formülü: Σ((x - mean_x) * (y - mean_y)) / Σ((x - mean_x)^2)
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((x[i] - mean_x)**2 for i in range(n))
    
    m = numerator / denominator
    # Kesim noktası (b) formülü: b = mean_y - m * mean_x
    b = mean_y - m * mean_x
    
    return m, b

# 2. m ve b değerlerini hesapla ve yazdır
m, b = calculate_regression(x, y)
print(f"Eşitlik: y = {m:.2f}x + {b:.2f}")

# 3. Tahmin fonksiyonu
def predict(x_value):
    return m * x_value + b

# Örnek tahmin
print(f"x=6 için tahmin edilen y: {predict(6):.2f}")

# Opsiyonel: Görselleştirme
plt.scatter(x, y, color='red', label='Veri Noktaları')
regression_line = [predict(val) for val in x]
plt.plot(x, regression_line, color='blue', label='Regresyon Doğrusu')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
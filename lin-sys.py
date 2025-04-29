import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Wizualizacja układu równań liniowych")

st.markdown("Zmieniaj współczynniki równań liniowych i zobacz graficzne rozwiązanie układu równań.")

st.subheader("Równanie 1: a₁·x + b₁·y = c₁")
a1 = st.slider("a₁", -10, 10, 2)
b1 = st.slider("b₁", -10, 10, -5)
c1 = st.slider("c₁", -20, 20, -5)

st.subheader("Równanie 2: a₂·x + b₂·y = c₂")
a2 = st.slider("a₂", -10, 10, -5)
b2 = st.slider("b₂", -10, 10, 8)  # np. 15/2 ≈ 7.5 -> użyj 8
c2 = st.slider("c₂", -20, 20, 5)

# Zakres x
x_vals = np.linspace(-10, 10, 400)

# Funkcje y, tylko gdy b ≠ 0 (aby uniknąć dzielenia przez 0)
def get_line(a, b, c):
    if b != 0:
        return (c - a * x_vals) / b
    else:
        return None

y1 = get_line(a1, b1, c1)
y2 = get_line(a2, b2, c2)

fig, ax = plt.subplots(figsize=(8, 6))
if y1 is not None:
    ax.plot(x_vals, y1, label=f"{a1}·x + {b1}·y = {c1}", color='blue')
else:
    ax.axvline(x=c1/a1, color='blue', label=f"{a1}·x = {c1} (prosta pionowa)")

if y2 is not None:
    ax.plot(x_vals, y2, label=f"{a2}·x + {b2}·y = {c2}", color='green')
else:
    ax.axvline(x=c2/a2, color='green', label=f"{a2}·x = {c2} (prosta pionowa)")

# Rozwiązywanie układu równań
try:
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    solution = np.linalg.solve(A, B)
    x_sol, y_sol = solution
    ax.plot(x_sol, y_sol, 'ro', label=f"Punkt przecięcia: ({x_sol:.2f}, {y_sol:.2f})")
except np.linalg.LinAlgError:
    st.warning("Brak jednoznacznego rozwiązania (układ sprzeczny lub nieoznaczony).")

# Opisy i styl
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Wykres układu równań liniowych")
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.legend()
st.pyplot(fig)

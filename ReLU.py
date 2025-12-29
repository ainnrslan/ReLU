import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("ReLU Activation Function")

x = np.linspace(-10, 10, 400)
relu = np.maximum(0, x)

plt.figure()
plt.plot(x, relu)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Rectified Linear Unit (ReLU)")
st.pyplot(plt)
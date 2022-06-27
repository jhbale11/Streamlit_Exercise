# Streamlit_Exercise

> The fastest way to build and share data apps

### Pros+
- Build application with simple python codes
- Interactive features without backend, http requests
- Deploy app with Streamlit Cloud
- Can record a screencast

### Installation
```bash
pip install streamlit
```

### Sample Code
```python
import streamlit as st
import pandas as pd
import numpy as np

# set title
st.title('This is Streamlit')

# set subheader
st.subheader('This is subheader')

# draw chart
st.bar_chart(data)
```

### Run Streamlit Server
```bash
streamlit run sample.py
```
connect to `http://localhost:8501/`

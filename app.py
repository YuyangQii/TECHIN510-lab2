import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Iris Flower Explorer",
    page_icon="🌸",
    layout="wide",
)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("🌸 Iris Flower Explorer")


col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("""
    ## Dataset Overview
    The Iris Flower dataset is a classic in the field of machine learning and statistics. It contains 150 observations of iris flowers, including the following features:
    - **Sepal Length (cm)**: The length of the outer part of the flower.
    - **Sepal Width (cm)**: The width of the outer part of the flower.
    - **Petal Length (cm)**: The length of the inner part of the flower.
    - **Petal Width (cm)**: The width of the inner part of the flower.
    Each observation is classified into one of three species: Setosa, Versicolor, and Virginica.
    """)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("""
    ## Findings
    After analyzing the Iris Flower dataset, several interesting findings have been observed:
    - **Setosa** species tend to have shorter but wider sepals compared to other species.
    - **Versicolor** species usually feature medium-sized petals and sepals, making them intermediate between Setosa and Virginica.
    - **Virginica** species generally have the longest and widest petals, which significantly distinguish them from the other two species.
    """)

st.divider()

# Load the Iris dataset
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

# Sidebar for filter options
with st.sidebar:
    st.header("Filter Options")
    species_filter = st.selectbox("Species", ["All"] + list(df["species"].unique()))
    sepal_length_slider = st.slider("Sepal Length (cm)", float(df["sepal_length"].min()), float(df["sepal_length"].max()), (float(df["sepal_length"].min()), float(df["sepal_length"].max())))
    sepal_width_slider = st.slider("Sepal Width (cm)", float(df["sepal_width"].min()), float(df["sepal_width"].max()), (float(df["sepal_width"].min()), float(df["sepal_width"].max())))
    petal_length_slider = st.slider("Petal Length (cm)", float(df["petal_length"].min()), float(df["petal_length"].max()), (float(df["petal_length"].min()), float(df["petal_length"].max())))
    petal_width_slider = st.slider("Petal Width (cm)", float(df["petal_width"].min()), float(df["petal_width"].max()), (float(df["petal_width"].min()), float(df["petal_width"].max())))

# Filter data
if species_filter != "All":
    df = df[df["species"] == species_filter]
df = df[
    (df["sepal_length"] >= sepal_length_slider[0]) & (df["sepal_length"] <= sepal_length_slider[1]) &
    (df["sepal_width"] >= sepal_width_slider[0]) & (df["sepal_width"] <= sepal_width_slider[1]) &
    (df["petal_length"] >= petal_length_slider[0]) & (df["petal_length"] <= petal_length_slider[1]) &
    (df["petal_width"] >= petal_width_slider[0]) & (df["petal_width"] <= petal_width_slider[1])
]


col1, col2, col3 = st.columns([1,2,1])
with col2:
    with st.expander("View Filtered Data"):
        st.write(df)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("### Sepal Length & Width")
    fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species", symbol="species",
                     title="Sepal Length vs. Sepal Width", labels={"species": "Species"})
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Petal Length & Width")
    fig2 = px.scatter(df, x="petal_length", y="petal_width", color="species", symbol="species",
                      title="Petal Length vs. Petal Width", labels={"species": "Species"})
    st.plotly_chart(fig2, use_container_width=True)

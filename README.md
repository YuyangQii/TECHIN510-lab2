# TECHIN510-lab2
# Iris Flower Explorer🌸
A data analysis application to find oyt interesting insights about Iris🌸.

## Get Started
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

streamlit run app.py
```

## What's Included
- `.gitignore`: A configuration file for Git that specifies which files or folders to ignore in the project.
- `README.md`: The guide to your project, containing instructions and information on the Iris Flower Explorer.
- `app.py`: The Streamlit application script where the setup and layout of the web app, as well as the data processing and visualization, are defined.
- `requirements.txt`: Lists all the Python dependencies necessary to run the app, which can be installed using `pip`.


## Lessons Learned
- Streamlit's Data Flow: I learned how Streamlit reruns the entire script from top to bottom whenever the source code is modified or a user interacts with the app. This behavior was key to creating responsive and interactive features.
- Widget Utilization: Implementing Streamlit widgets like sliders and select boxes was instrumental for user interaction, enabling real-time data filtering and visualization, which made the app more engaging.
- Data Visualization with Plotly: Integrating Plotly with Streamlit for the scatter plots allowed me to provide rich visualizations that made the Iris dataset more accessible and understandable to users.
- Layout Management: Streamlit's column and sidebar functionality can effectively manage the app's layout to enhance user experience.

## Questions
- How can I implement real-time data updates in my Streamlit application? How does Streamlit detect and push new data when the data source is updated?
- When using Plotly to create charts in Streamlit, how can I customise the style and layout of the charts to better match our web visual design needs?

## TODO
 - Implement additional filter options for more granular data analysis.
 - Incorporate more datasets for comparative analysis with the Iris dataset.
 - Explore the use of Streamlit's custom components to further enhance the app's interactive capabilities.
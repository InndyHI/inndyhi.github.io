import pandas as pd
import altair as alt

DATA_URL = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"

# Load the dataset
data = pd.read_csv(DATA_URL)

# Preprocess data
data['Year Constructed'] = pd.to_numeric(data['Year Constructed'], errors='coerce')
data['Square Footage'] = pd.to_numeric(data['Square Footage'], errors='coerce')

data = data.dropna(subset=['Year Constructed', 'Square Footage'])
data = data[data['Year Constructed'] != 0]

# Line Plot
yearly_data = data.groupby('Year Constructed')['Square Footage'].sum().reset_index()

chart1 = alt.Chart(yearly_data).mark_line(point=True).encode(
    x=alt.X('Year Constructed:O', title="Year Constructed"),
    y=alt.Y('Square Footage:Q', title="Total Square Footage"),
    tooltip=['Year Constructed', 'Square Footage']
).properties(
    title="Total Square Footage by Year Constructed",
    width=1200,
    height=400
)

# Stacked Bar Plot
grouped_data = data.groupby(['Year Constructed', 'Usage Description'])['Square Footage'].sum().reset_index()

chart2 = alt.Chart(grouped_data).mark_bar().encode(
    x=alt.X('Year Constructed:O', title="Year Constructed"),
    y=alt.Y('Square Footage:Q', title="Total Square Footage"),
    color=alt.Color('Usage Description:N', title="Usage Description",
                    scale=alt.Scale(scheme='category20')),  # Use category20 for more categories
    tooltip=['Year Constructed', 'Usage Description', 'Square Footage']
).properties(
    title="Total Square Footage by Usage Description",
    width=1200,
    height=400
)

chart1.save("chart1.html")
chart2.save("chart2.html")
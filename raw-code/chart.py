import pandas as pd
import altair as alt

DATA_URL = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"

# Load the dataset
data = pd.read_csv(DATA_URL)

# Preprocess data
data['Year Constructed'] = pd.to_numeric(data['Year Constructed'], errors='coerce')
data = data.dropna(subset=['Year Constructed', 'Usage Description'])
data = data[data['Year Constructed'] != 0]

# Pie Chart
highlight = alt.selection_point(fields=["Usage Description"], on="mouseover", empty="none")

# Create the pie chart with highlighting
chart1 = alt.Chart(data).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="Usage Description", type="nominal", aggregate="count", title="Building Counts"),
    color=alt.condition(
        highlight,
        alt.value("lime"),
        alt.Color('Usage Description:N', title="Usage Description",
                    scale=alt.Scale(scheme='category20'))  # Color for non-highlighted parts
    ),
    tooltip=["Usage Description", alt.Tooltip("count()", title="Building Count")]
).add_params(
    highlight
).properties(
    title="Distribution of Building Counts by Usage Description",
    width=400,
    height=400
)

year_range = data['Year Constructed'].dropna().astype(int).unique()
year_range = sorted(year_range)

# Generate ticks for every 10th year
year_ticks = [year for year in year_range if year % 10 == 0]

# Stacked Bar Chart
chart2 = alt.Chart(data).mark_bar().encode(
    x=alt.X(
        'Year Constructed:O',
        title="Year Constructed",
        axis=alt.Axis(values=year_ticks)  # Add labels only for every 10th year
    ),
    y=alt.Y('count()', title="Building Count"),
    color=alt.Color('Usage Description:N', title="Usage Description",
                    scale=alt.Scale(scheme='category20')),  # Use category20 for more categories
    tooltip=["Year Constructed", "Usage Description", alt.Tooltip("count()", title="Building Count")]
).properties(
    title="Building Counts by Usage Description",
    width=1000,
    height=400
)

chart1.save("chart1.html")
chart2.save("chart2.html")
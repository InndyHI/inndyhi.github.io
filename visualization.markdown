---
layout: default
title: 'Visualizations'
permalink: /visualizations/
---

# Total Records Destribution by Usage Description

The pie chart displays the total counts of building categories constructed. Pie chart is good for showing category distribution.
I add a `highlight` and `tooltip` interaction to enhance visualization.
There are too many categories of usage desccription, so using lines to visualize them will be messy. In addition, the default color scheme for stacked bar plot is `category10`, so this needs to be changed to avoid same colors, same as chart 2 below.
I use `html` for both charts. Even though `json` is light weighted, `html` doesn't need any dependencies to visualize these charts. In addition, it can also be automatically converted to `json` and editted in `vega-lite` editor.

<iframe src="/assets/chart1.html" width="200%" height="500" frameborder="0"></iframe>

# Total Records by Usage Description and Year

The stacked bar chart breaks down the building counts by usage description and year.
Since there are too many records on different `year`, and the time range is also long, so I add a tick to make `year` label appears every 10 years.
We can easliy find out how different building usage types contribute to total records each year.

<iframe src="/assets/chart2.html" width="200%" height="500" frameborder="0"></iframe>

<div style="text-align: center;">
    <a href="https://github.com/InndyHI/inndyhi.github.io/blob/main/raw-code/Workbook.ipynb" style="text-decoration: none;">
        <button style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
            View Raw Code
        </button>
    </a>
    <a href="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv" style="text-decoration: none;">
        <button style="padding: 10px 20px; background-color: #28A745; color: white; border: none; border-radius: 5px; cursor: pointer;">
            View Data
        </button>
    </a>
</div>

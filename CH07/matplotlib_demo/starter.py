"""
CH07 Demo: Plotting Data with matplotlib

1) Line graphs
2) Customizing axes
3) Bar graphs
4) Pie charts

Matplotlib is NOT part of standard Python,
so you may need to install it:

pip install matplotlib
python3 -m pip install matplotlib
"""




"""
=========== Line Graph Basics ===========
A line graph connects points (x,y).

We usually store the x values and y values
in lists.
"""



# --- Mini Task ---
# Change the y_coords list to:
# [0, 1, 4, 9, 16]
# What kind of pattern does the graph make?


"""
=========== Changing the Axis Limits ===========
xlim() and ylim() control the visible area
of the graph.
"""



# --- Mini Task ---
# Try changing xmax to 5 and ymax to 12.
# What happens to the graph?


"""
=========== Custom Tick Marks ===========
Tick marks are the labels along the axes.
"""


# --- Mini Task ---
# Change the y tick labels to:
# ["0 dollars", "2 dollars", "4 dollars", "6 dollars", "8 dollars"]


"""
=========== Custom Tick Labels ===========
We can replace the labels entirely.
"""


"""
=========== Titles and Labels ===========
Graphs should always have:

• title
• x-axis label
• y-axis label
"""



# --- Mini Task ---
# Change the title to something like:
# "Store Revenue Over Time"
# Also change the axis labels.


"""
=========== Bar Graphs ===========
Bar graphs are good for comparing categories.

Each x value is the left edge of a bar.
Each y value is the height of a bar.
"""




# --- Mini Task ---
# Change bar_width to:
# 0.2
# 1.0
# How does that affect the bars?


"""
=========== Bar Colors ===========
We can change colors using color codes:

'r' = red
'g' = green
'b' = blue
'k' = black
"""




# --- Mini Task ---
# Try changing the colors tuple to:
# ("b", "b", "b", "b")
# What happens?


"""
=========== Pie Charts ===========
Pie charts show proportions of a whole.

Each value becomes a slice.
"""



# --- Mini Task ---
# Change values to:
# [20, 20, 20]
# What happens to the pie?


"""
=========== Pie Chart Labels ===========
Labels tell us what each slice represents.
"""



"""
=========== Pie Chart Colors + Title ===========
"""



# --- Mini Task ---
# Add another category:
# "coffee"
# Update the values list and the labels list
# so the chart still works.

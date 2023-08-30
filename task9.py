import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Load the data from Excel
df = pd.read_excel(r'C:\Users\Thippeswamy U-3061\PycharmProjects\pythonProject\ramp_up_python\heatmap_data.xlsx')

# Define a custom colormap based on your color_scale dictionary
color_scale = {
    'White': 'white',
    'Light Green': 'lime',
    'One level above light green': 'green',
    'Two levels above light green': 'darkgreen',
    'Two levels below dark green': 'darkred',
    'One level below dark green': 'red',
    'Dark Green': 'black',
    'One Level Above Light Green': 'lime',  # Add this entry
    'Lightgreen': 'lime',  # Add this entry
    'TWO level below darkgreen': 'darkred'  # Add this entry
}

cmap = ListedColormap([color_scale[color] for color in df['colors']])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Loop through the DataFrame to create colored cells
for index, row in df.iterrows():
    size = row['size']
    color = row['colors']
    rect = plt.Rectangle((index - 0.5, 0), 1, size, color=color_scale[color])
    ax.add_patch(rect)

# Set axis limits and labels
ax.set_xlim(-0.5, len(df) - 0.5)
ax.set_ylim(0, max(df['size']) + 1)
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df['Languages'], rotation=90)
ax.set_yticks(range(max(df['size']) + 1))
ax.set_xlabel('Languages')
ax.set_ylabel('Sizes')

# Create a legend for the colors
handles = [plt.Rectangle((0, 0), 1, 1, color=color_scale[color], label=color) for color in df['colors'].unique()]
ax.legend(handles=handles, title='Colors', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.tight_layout()
plt.title('Heatmap of Colors')
plt.show()

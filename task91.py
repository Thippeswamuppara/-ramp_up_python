# import pandas as pd
# import plotly.graph_objects as go
#
# # Color scale mapping
# color_scale = {
#     'White': 'rgb(255, 255, 255)',  # White
#     'Light Green': 'rgb(173, 255, 47)',  # Light green
#     'One level above light green': 'rgb(0, 255, 0)',  # Light green
#     'Two levels above light green': 'rgb(0, 128, 0)',  # Light green
#     'Two levels below dark green': 'rgb(0, 32, 0)',  # Dark green
#     'One level below dark green': 'rgb(0, 100, 0)',  # Dark green
#     'Dark Green': 'rgb(0, 64, 0)'  # Darkest green
# }
#
# # Read data from an Excel file
# df = pd.read_excel(r'C:\Users\Thippeswamy U-3061\PycharmProjects\pythonProject\ramp_up_python\heatmap_data.xlsx')
#
# # Map expertise levels to RGB values using the color_scale, using the default for unmatched levels
# df['Color'] = df['colors'].map(color_scale)
# label=df["Languages"].tolist()
# # Create the treemap
# fig = go.Figure(go.Treemap(
#     labels=df.apply(lambda row: f'{row["Languages"]} ({row["size"]})', axis=1),
#     parents=['']*len(label),
#     values=df['size'],
#     customdata=df['Color'],
#     hovertemplate='<b>Area:</b> %{label}<br><b>Team Size:</b> %{value}<br><b>Expertise:</b> %{customdata}',
#     marker=dict(
#         colorscale=['white', 'rgb(173, 255, 47)', 'rgb(0, 255, 0)', 'rgb(0, 128, 0)', 'rgb(0, 100, 0)', 'rgb(0, 64, 0)', 'rgb(0, 32, 0)'],
#     ),
# ))
#
# # Configure layout
# fig.update_layout(
#     title='Team Expertise Treemap',
#     template='plotly',
#     treemapcolorway=['rgb(255, 255, 255)']
# )
#
# # Show the treemap
# fig.show()
s = "defabc"
l1=[]
for i in range(len(s)):
    ascii = ord(s[i])
    for j in s:

        if ascii<ord[j]:
            ascii=ord[j]
    l1.append(ascii)



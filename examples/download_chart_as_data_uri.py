from ImageCharts import ImageCharts

# vertical bar chart
# 300px x 300px
# 2 data points: 60 and 40
# download chart image and generate a data URI string

chart_url = ImageCharts().cht('bvg').chs('300x300').chd('a:60,40').to_data_uri()

print(chart_url) # "data:image/png;base64,iVBORw0KGgo...

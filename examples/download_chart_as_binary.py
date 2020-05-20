from ImageCharts import ImageCharts

# vertical bar chart
# 300px x 300px
# 2 data points: 60 and 40
# download chart image

chart_url = ImageCharts().cht('bvg').chs('300x300').chd('a:60,40').to_binary()
print(chart_url) # b'\x89PNG\r\n\x1a\n\x00\x00...

from ImageCharts import ImageCharts

# vertical bar chart
# 300px x 300px
# 2 data points: 60 and 40
# get the generated URL
chart_url = ImageCharts().cht('bvg') .chs('300x300') .chd('a:60,40') .to_url()

print(chart_url) # https://image-charts.com/chart?cht=bvg&chs=300x300&chd=a%3A60%2C40

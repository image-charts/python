from ImageCharts import ImageCharts

# genertates a
# vertical bar chart (cht=bvg)
# of 300px x 300px (chs=300x300)
# with 2 data points: 60 and 40 (chd=a:60,40)
# and write it to /tmp/chart.png

ImageCharts().cht('bvg').chs('300x300').chd('a:60,40').to_file('/tmp/awesome_chart.png')

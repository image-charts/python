from ImageCharts import ImageCharts

# pie chart
# 700px x 190px
# 2 data points: 60 and 40
# 1 label per pie slice : "Hello" and "World"
# 1 gradient per pie slice
# enable paid-only features like high-resolution charts
# get the whole (HMAC signed) URL

chart_url = ImageCharts({'secret': 'SECRET_KEY'}).icac('ACCOUNT_ID').cht('p3').chs('700x190').chd('t:60,40').chl('Hello|World').chf('ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1').icretina('1').to_url()

print(chart_url)
# https://image-charts.com/chart?chd=t%3A60%2C40&chf=ps0-0%2Clg%2C45%2Cffeb3b%2C0.2%2Cf44336%2C1%7Cps0-1%2Clg%2C45%2C8bc34a%2C0.2%2C009688%2C1&chl=Hello%7CWorld&chs=700x190&cht=p3&icac=fgribreau&icretina=1&ichm=652f09953663bce161ac612af5f310f5abf7151b55337ef2a97e5e1cd559c8fb
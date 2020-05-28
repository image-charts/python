# -*- coding: utf-8 -*-

# Compatible with Python 3.6+

from urllib.parse import urlencode, quote_plus
import hmac, hashlib, codecs, json
from base64 import b64encode
import requests

class ImageCharts:
  """A python client for image-charts.com, a web service that generates static charts."""

  def __init__(self, options=None, previous=None) -> None:
    """Image-Charts constructor"""

    if previous is None:
      previous = {}
    if options is None:
      options = {}

    self.protocol = options['protocol'] if 'protocol' in options else 'https'
    self.host = options['host']  if 'host' in options else 'image-charts.com'
    self.port = options['port']  if 'port' in options else  443
    self.pathname = options['pathname']  if 'pathname' in options else '/chart'
    self.timeout = options['timeout']  if 'timeout' in options else 5000
    self.secret = options['secret']  if 'secret' in options else None
    self.query = previous
    self.request_headers = {}
    self.response_headers = {}

  def __clone(self, param: str, value :str):
    add = {}
    add[param] = value
    return ImageCharts({
      'protocol' : self.protocol,
      'host' : self.host,
      'port' : self.port,
      'pathname' : self.pathname,
      'timeout' : self.timeout,
      'secret' : self.secret
    }, {**self.query, **add})


  
  def cht(self, value: str):
    """bvg= grouped bar chart, bvs= stacked bar chart, lc=line chart, ls=sparklines, p=pie chart. gv=graph viz
	*         Three-dimensional pie chart (p3) will be rendered in 2D, concentric pie chart are not supported.
	*         [Optional, line charts only] You can add :nda after the chart type in line charts to hide the default axes.

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-type/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Chart type
    """
    return self.__clone('cht', value)

  
  def chd(self, value: str):
    """chart data

    [Reference documentation]{@link https://documentation.image-charts.com/reference/data-format/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - chart data
    """
    return self.__clone('chd', value)

  
  def chds(self, value: str):
    """You can configure some charts to scale automatically to fit their data with chds=a. The chart will be scaled so that the largest value is at the top of the chart and the smallest (or zero, if all values are greater than zero) will be at the bottom. Otherwise the &#34;&amp;lg;series_1_min&amp;gt;,&amp;lg;series_1_max&amp;gt;,...,&amp;lg;series_n_min&amp;gt;,&amp;lg;series_n_max&amp;gt;&#34; format set one or more minimum and maximum permitted values for each data series, separated by commas. You must supply both a max and a min. If you supply fewer pairs than there are data series, the last pair is applied to all remaining data series. Note that this does not change the axis range; to change the axis range, you must set the chxr parameter. Valid values range from (+/-)9.999e(+/-)199. You can specify values in either standard or E notation.

    [Reference documentation]{@link https://documentation.image-charts.com/reference/data-format/#text-format-with-custom-scaling}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - data format with custom scaling
    """
    return self.__clone('chds', value)

  
  def choe(self, value: str):
    """How to encode the data in the QR code. &#39;UTF-8&#39; is the default and only supported value. Contact our team if you wish to have support for Shift_JIS and/or ISO-8859-1.

    [Reference documentation]{@link https://documentation.image-charts.com/qr-codes/#data-encoding}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - QRCode data encoding
    """
    return self.__clone('choe', value)

  
  def chld(self, value: str):
    """QRCode error correction level and optional margin

    [Reference documentation]{@link https://documentation.image-charts.com/qr-codes/#error-correction-level-and-margin}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    @default '{param.default}'

    - value :str - QRCode error correction level and optional margin
    """
    return self.__clone('chld', value)

  
  def chxr(self, value: str):
    """You can specify the range of values that appear on each axis independently, using the chxr parameter. Note that this does not change the scale of the chart elements (use chds for that), only the scale of the axis labels.

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-axis/#axis-range}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Axis data-range
    """
    return self.__clone('chxr', value)

  
  def chof(self, value: str):
    """Some clients like Flowdock/Facebook messenger and so on, needs an URL to ends with a valid image extension file to display the image, use this parameter at the end your URL to support them. Valid values are &#34;.png&#34;, &#34;.svg&#34; and &#34;.gif&#34;. 
	*           Only QRCodes and GraphViz support svg output.

    [Reference documentation]{@link https://documentation.image-charts.com/reference/output-format/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    @default '{param.default}'

    - value :str - Image output format
    """
    return self.__clone('chof', value)

  
  def chs(self, value: str):
    """Maximum chart size for all charts except maps is 998,001 pixels total (Google Image Charts was limited to 300,000), and maximum width or length is 999 pixels.

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-size/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Chart size (&lt;width&gt;x&lt;height&gt;)
    """
    return self.__clone('chs', value)

  
  def chdl(self, value: str):
    """Format: &amp;lt;data_series_1_label&amp;gt;|...|&amp;lt;data_series_n_label&amp;gt;. The text for the legend entries. Each label applies to the corresponding series in the chd array. Use a + mark for a space. If you do not specify this parameter, the chart will not get a legend. There is no way to specify a line break in a label. The legend will typically expand to hold your legend text, and the chart area will shrink to accommodate the legend.

    [Reference documentation]{@link https://documentation.image-charts.com/reference/legend-text-and-style/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Text for each series, to display in the legend
    """
    return self.__clone('chdl', value)

  
  def chdls(self, value: str):
    """Specifies the color and font size of the legend text. &lt;color&gt;,&lt;size&gt;

    [Reference documentation]{@link https://documentation.image-charts.com/reference/legend-text-and-style/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    @default '{param.default}'

    - value :str - Chart legend text and style
    """
    return self.__clone('chdls', value)

  
  def chg(self, value: str):
    """Solid or dotted grid lines

    [Reference documentation]{@link https://documentation.image-charts.com/reference/grid-lines/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Solid or dotted grid lines
    """
    return self.__clone('chg', value)

  
  def chco(self, value: str):
    """You can specify the colors of a specific series using the chco parameter.
	*       Format should be &amp;lt;series_2&amp;gt;,...,&amp;lt;series_m&amp;gt;, with each color in RRGGBB format hexadecimal number.
	*       The exact syntax and meaning can vary by chart type; see your specific chart type for details.
	*       Each entry in this string is an RRGGBB[AA] format hexadecimal number.
	*       If there are more series or elements in the chart than colors specified in your string, the API typically cycles through element colors from the start of that series (for elements) or for series colors from the start of the series list.
	*       Again, see individual chart documentation for details.

    [Reference documentation]{@link https://documentation.image-charts.com/bar-charts/#examples}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    @default '{param.default}'

    - value :str - series colors
    """
    return self.__clone('chco', value)

  
  def chtt(self, value: str):
    """chart title

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-title/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - chart title
    """
    return self.__clone('chtt', value)

  
  def chts(self, value: str):
    """Format should be &#34;&lt;color&gt;,&lt;font_size&gt;[,&lt;opt_alignment&gt;,&lt;opt_font_family&gt;,&lt;opt_font_style&gt;]&#34;, opt_alignement is not supported

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-title/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - chart title colors and font size
    """
    return self.__clone('chts', value)

  
  def chxt(self, value: str):
    """Specify which axes you want (from: &#34;x&#34;, &#34;y&#34;, &#34;t&#34; and &#34;r&#34;). You can use several of them, separated by a coma; for example: &#34;x,x,y,r&#34;. Order is important.

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-axis/#visible-axes}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Display values on your axis lines or change which axes are shown
    """
    return self.__clone('chxt', value)

  
  def chxl(self, value: str):
    """Specify one parameter set for each axis that you want to label. Format &#34;&lt;axis_index&gt;:|&lt;label_1&gt;|...|&lt;label_n&gt;|...|&lt;axis_index&gt;:|&lt;label_1&gt;|...|&lt;label_n&gt;&#34;. Separate multiple sets of labels using the pipe character ( | ).

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-axis/#custom-axis-labels}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Custom string axis labels on any axis
    """
    return self.__clone('chxl', value)

  
  def chxs(self, value: str):
    """You can specify the range of values that appear on each axis independently, using the chxr parameter. Note that this does not change the scale of the chart elements (use chds for that), only the scale of the axis labels.

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-axis/#axis-label-styles}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Font size, color for axis labels, both custom labels and default label values
    """
    return self.__clone('chxs', value)

  
  def chm(self, value: str):
    """
	* format should be either:
	*   - line fills (fill the area below a data line with a solid color): chm=&lt;b_or_B&gt;,&lt;color&gt;,&lt;start_line_index&gt;,&lt;end_line_index&gt;,&lt;0&gt; |...| &lt;b_or_B&gt;,&lt;color&gt;,&lt;start_line_index&gt;,&lt;end_line_index&gt;,&lt;0&gt;
	*   - line marker (add a line that traces data in your chart): chm=D,&lt;color&gt;,&lt;series_index&gt;,&lt;which_points&gt;,&lt;width&gt;,&lt;opt_z_order&gt;
	*   - Text and Data Value Markers: chm=N&lt;formatting_string&gt;,&lt;color&gt;,&lt;series_index&gt;,&lt;which_points&gt;,&lt;width&gt;,&lt;opt_z_order&gt;,&lt;font_family&gt;,&lt;font_style&gt;
	*     

    [Reference documentation]{@link https://documentation.image-charts.com/reference/compound-charts/}
    * @example

    

    - value :str - compound charts and line fills
    """
    return self.__clone('chm', value)

  
  def chls(self, value: str):
    """line thickness and solid/dashed style

    [Reference documentation]{@link https://documentation.image-charts.com/line-charts/#line-styles}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - line thickness and solid/dashed style
    """
    return self.__clone('chls', value)

  
  def chl(self, value: str):
    """If specified it will override &#34;chdl&#34; values

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-label/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - bar, pie slice, doughnut slice and polar slice chart labels
    """
    return self.__clone('chl', value)

  
  def chma(self, value: str):
    """chart margins

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-margin/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - chart margins
    """
    return self.__clone('chma', value)

  
  def chdlp(self, value: str):
    """Position of the legend and order of the legend entries

    [Reference documentation]{@link https://documentation.image-charts.com/reference/legend-text-and-style/}
    * @example

    @default '{param.default}'

    - value :str - Position of the legend and order of the legend entries
    """
    return self.__clone('chdlp', value)

  
  def chf(self, value: str):
    """Background Fills

    [Reference documentation]{@link https://documentation.image-charts.com/reference/background-fill/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    @default '{param.default}'

    - value :str - Background Fills
    """
    return self.__clone('chf', value)

  
  def chan(self, value: str):
    """gif configuration

    [Reference documentation]{@link https://documentation.image-charts.com/reference/animation/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - gif configuration
    """
    return self.__clone('chan', value)

  
  def chli(self, value: str):
    """doughnut chart inside label

    [Reference documentation]{@link https://documentation.image-charts.com/pie-charts/#inside-label}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - doughnut chart inside label
    """
    return self.__clone('chli', value)

  
  def icac(self, value: str):
    """image-charts enterprise `account_id`

    [Reference documentation]{@link https://documentation.image-charts.com/enterprise/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - image-charts enterprise `account_id`
    """
    return self.__clone('icac', value)

  
  def ichm(self, value: str):
    """HMAC-SHA256 signature required to activate paid features

    [Reference documentation]{@link https://documentation.image-charts.com/enterprise/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - HMAC-SHA256 signature required to activate paid features
    """
    return self.__clone('ichm', value)

  
  def icff(self, value: str):
    """How to use icff to define font family as Google Font : https://developers.google.com/fonts/docs/css2

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-font/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Default font family for all text from Google Fonts. Use same syntax as Google Font CSS API
    """
    return self.__clone('icff', value)

  
  def icfs(self, value: str):
    """Default font style for all text

    [Reference documentation]{@link https://documentation.image-charts.com/reference/chart-font/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - Default font style for all text
    """
    return self.__clone('icfs', value)

  
  def iclocale(self, value: str):
    """localization (ISO 639-1)

    [Reference documentation]{@link }
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - localization (ISO 639-1)
    """
    return self.__clone('iclocale', value)

  
  def icretina(self, value: str):
    """Retina is a marketing term coined by Apple that refers to devices and monitors that have a resolution and pixel density so high — roughly 300 or more pixels per inch – that a person is unable to discern the individual pixels at a normal viewing distance.
	*           In order to generate beautiful charts for these Retina displays, Image-Charts supports a retina mode that can be activated through the icretina=1 parameter

    [Reference documentation]{@link https://documentation.image-charts.com/reference/retina/}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    

    - value :str - retina mode
    """
    return self.__clone('icretina', value)

  
  def icqrb(self, value: str):
    """Background color for QR Codes

    [Reference documentation]{@link https://documentation.image-charts.com/qr-codes/#background-color}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    @default '{param.default}'

    - value :str - Background color for QR Codes
    """
    return self.__clone('icqrb', value)

  
  def icqrf(self, value: str):
    """Foreground color for QR Codes

    [Reference documentation]{@link https://documentation.image-charts.com/qr-codes/#foreground-color}
    * @example
  * const chart = ImageCharts().{param.name}('{doc(example)}')
    @default '{param.default}'

    - value :str - Foreground color for QR Codes
    """
    return self.__clone('icqrf', value)

  

  def to_url(self) -> str:
    """Get the full Image-Charts API url (signed and encoded if necessary)"""

    def sign(query, secretKey):
      return codecs.getencoder('hex')(hmac.new(secretKey.encode('utf-8'), query.encode('utf-8'), hashlib.sha256).digest())[0].decode('utf-8')

    query_string = "&".join( [ param + '=' + (quote_plus(str(self.query[param]))) for param in self.query.keys() ] )
    url = '{protocol}://{host}:{port}{pathname}?'.format(protocol=self.protocol, host=self.host, port=self.port, pathname=self.pathname) + query_string

    if 'icac' in self.query and self.secret and len(self.secret) > 0:
      url += '&ichm=' + sign(query_string, self.secret)

    return url

  def to_binary(self):
    """Yield the content of the chart image as bytes (blocking)"""

    self.request_headers = {'user-agent': 'python-image-charts/latest' + (' ({icac})'.format(icac=self.query['icac']) if 'icac' in self.query and len(self.query['icac']) > 0 else '')}
    response = requests.get(self.to_url(), timeout=self.timeout, headers=self.request_headers)

    self.response_headers = response.headers;

    if response.status_code >= 200 and response.status_code < 300:
      return response.content

    if 'x-ic-error-validation' not in self.response_headers or len(self.response_headers['x-ic-error-validation']) == 0:
        raise Exception(self.response_headers['x-ic-error-code'])

    validation_message = json.loads(self.response_headers['x-ic-error-validation'])

    if not validation_message or len(validation_message) < 1:
      raise Exception(self.response_headers['x-ic-error-code'])

    raise Exception(validation_message[0]['message'])

  def to_data_uri(self) -> str:
    """Do a blocking request to Image-Charts API with current configuration and a base64 encoded data URI

    Return base64 data URI as str
    """
    encoding = 'base64'
    mimetype = 'image/gif' if 'chan' in self.query else 'image/png'
    encoded = b64encode(self.to_binary()).decode("utf-8")
    return 'data:{mimetype};{encoding},{encoded}'.format(mimetype=mimetype, encoding=encoding, encoded=encoded)

  def to_file(self, path) -> str:
    """Do a blocking request to Image-Charts API with current configuration and a base64 encoded data URI (blocking)

    """
    with open(path, 'wb') as f:
      f.write(self.to_binary())

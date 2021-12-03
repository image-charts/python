# Run tests from the repository root directory:
# $ python ImageCharts.test.py

# compatibility with both Python 2.x and 3.x
from __future__ import print_function
import os, sys
import unittest

sys.path.insert(0, '.')
# Run tests from the repository root directory:
# python ./ImageCharts.test.php

from ImageCharts import ImageCharts

class TestImageCharts(unittest.TestCase):
    def test__CanInstance(self):
      self.assertTrue(isinstance(ImageCharts(), ImageCharts))

    def test__to_url_works(self):
      self.assertEqual(ImageCharts().cht('p').chd('t:1,2,3').to_url(), 'https://image-charts.com:443/chart?cht=p&chd=t%3A1%2C2%2C3')

    def test__exposes_parameters_and_use_them(self):
      self.maxDiff = None
      from functools import reduce
      chart = ImageCharts()
      def call_method(chart, method):
          return getattr(chart, method)("plop")
      methods = [method for method in dir(ImageCharts()) if method.startswith('c') or method.startswith('ic')]
      query = "&".join([method + '=plop' for method in methods])
      self.assertEqual(reduce(call_method, methods, chart).to_url(), 'https://image-charts.com:443/chart?' + query)

    def test__adds_a_signature_when_icac_and_secrets_are_defined(self):
        self.assertEqual(
          (ImageCharts({ 'secret' : 'plop'})).cht('p').chd('t:1,2,3').chs('100x100').icac('test_fixture').to_url(),
          'https://image-charts.com:443/chart?cht=p&chd=t%3A1%2C2%2C3&chs=100x100&icac=test_fixture&ichm=71bd93758b49ed28fdabd23a0ff366fe7bf877296ea888b9aaf4ede7978bdc8d'
      )

    def test__rejects_if_a_chs_is_not_defined(self):
        with self.assertRaisesRegex(Exception, """"chs" is required"""):
          ImageCharts().cht('p').chd('t:1,2,3').to_binary()


    def test__rejects_if_a_icac_is_defined_without_ichm(self):
      with self.assertRaisesRegex(Exception, 'HMAC-SHA256 request signature'):
        ImageCharts().cht('p').chd('t:1,2,3').chs('100x100').icac('test_fixture').to_binary()

    def test__rejects_if_timeout_is_reached(self):
      with self.assertRaisesRegex(Exception, 'timed out'):
        ImageCharts({'timeout' : 0.01}).cht('p').chd('t:1,2,3').chs('100x100').chan('1200').to_binary()

    def test__to_binary_works(self):
      size = len(ImageCharts().cht('p').chd('t:1,2,3').chs('2x2').to_binary())
      self.assertTrue(size > 60, '{sz} > 60'.format(sz=size))

    def test__forwards_package_name_version_as_user_agent(self):
        chart = ImageCharts().cht('p').chd('t:1,2,3').chs('10x10')
        chart.to_binary()
        self.assertEqual(chart.request_headers['user-agent'], 'python-image-charts/latest')

    def test__forwards_package_name_version_icac_as_user_agent(self):
        chart = ImageCharts({'secret' : 'plop'}).cht('p').chd('t:1,2,3').chs('10x10').icac('MY_ACCOUNT_ID')
        try:
          chart.to_binary()
        except:
          pass
        self.assertEqual(chart.request_headers['user-agent'], 'python-image-charts/latest (MY_ACCOUNT_ID)')

    def test__throw_error_if_account_not_found(self):
      with self.assertRaisesRegex(Exception, """you must be an Image-Charts subscriber"""):
        ImageCharts({'secret' : 'plop'}).cht('p').chd('t:1,2,3').chs('10x10').icac('MY_ACCOUNT_ID').to_binary()

    def test__rejects_if_there_was_an_error(self):
      with self.assertRaisesRegex(Exception, """"chs" is required"""):
        ImageCharts().cht('p').chd('t:1,2,3').to_data_uri()

    def test__to_data_uri_works(self):
        self.assertEqual(ImageCharts().cht('p').chd('t:1,2,3').chs('2x2').to_data_uri()[:30], 'data:image/png;base64,iVBORw0K')

    def test__to_file_throw_exception_if_bad_path(self):
      with self.assertRaisesRegex(Exception, """No such file or directory"""):
        ImageCharts().cht('p').chd('t:1,2,3').chs('2x2').to_file('/tmp_oiqsjosijd/chart.png')

    def test__to_file_works(self):
      ImageCharts().cht('p').chd('t:1,2,3').chs('2x2').to_file('/tmp/chart.png')
      with open('/tmp/chart.png', 'rb') as f:
        f.close()

    def test__support_gif(self):
        self.assertEqual(ImageCharts().cht('p').chd('t:1,2,3').chan('100').chs('2x2').to_data_uri()[:30], 'data:image/gif;base64,R0lGODlh')

    def test__expose_the_protocol(self):
        self.assertEqual(ImageCharts().protocol, 'https')

    def test__let_protocol_to_be_user_defined(self):
        self.assertEqual(ImageCharts({ 'protocol' : 'http' }).protocol, 'http')

    def test__expose_the_host(self):
        self.assertEqual(ImageCharts().host, 'image-charts.com')

    def test__let_host_to_be_user_defined(self):
        self.assertEqual(ImageCharts({ 'host' : 'on-premise-image-charts.com' }).host,'on-premise-image-charts.com')

    def test__expose_the_pathname(self):
        self.assertEqual(ImageCharts().pathname, '/chart')

    def test__expose_the_port(self):
        self.assertEqual(ImageCharts().port, 443)

    def test__let_port_to_be_user_defined(self):
        self.assertEqual(ImageCharts({ 'port' : 8080 }).port, 8080)

    def test__expose_the_query(self):
        self.assertEqual(ImageCharts().query, {})

    def test__expose_the_query_user_defined(self):
        self.assertEqual(ImageCharts().cht('p').chd('t:1,2,3').icac('plop').query, {'chd' : 't:1,2,3', 'cht' : 'p', 'icac' : 'plop'})

if __name__ == '__main__':
  unittest.main()

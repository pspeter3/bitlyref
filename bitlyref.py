#!/usr/bin/python
from urllib import urlencode
from urlparse import urlsplit, urlunsplit, parse_qs

def add_referrer(uri, param, referrer):
  """ Adds a referrer to a url
  @parameter uri: long url to shorten
  @parameter referrer: referrer name
  @parameter param: parameter used for referrer
  """
  split = urlsplit(uri)
  params = parse_qs(split.query)
  if param in params:
    raise Exception('Referrer Collision Exception')
  params[param] = referrer
  qs = urlencode(params, True)
  url_tuple = (split.scheme, split.netloc, split.path, qs, split.fragment)
  return urlunsplit(url_tuple)

if __name__ == '__main__':
  # Set up the command line options
  from optparse import OptionParser
  usage = 'usage: %prog [options] url referrer'
  parser = OptionParser(usage)
  parser.add_option('-u', '--username', help='The bit.ly username')
  parser.add_option('-k', '--key', help='The bit.ly API key')
  parser.add_option('-p', '--param', help='The query string parameter', default='ref')
  (options, args) = parser.parse_args()
  if options.username is None:
    parser.error('Username is required')
  if options.key is None:
    parser.error('API Key is required. Go to https://bitly.com/a/your_api_key')
  if len(args) is not 2:
    parser.error('URL and Referrer are required')
  url = args[0]
  referrer = args[1]

  # Set up bitly
  import bitly_api
  bitly = bitly_api.Connection(options.username, options.key)
  referrer_url = add_referrer(url, options.param, referrer)
  short_url = bitly.shorten(referrer_url)

  print short_url['url']
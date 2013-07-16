#!/usr/bin/python
from urllib import urlencode
from urlparse import urlsplit, urlunsplit, parse_qs

def add_referrer(uri, referrer, param='ref'):
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
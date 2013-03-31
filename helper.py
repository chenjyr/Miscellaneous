import os
import re
import urllib2


def retrieveSourceFromURL(url):
  """
    Returns the GET data from url
  """
  usock = urllib2.urlopen(url)
  data  = usock.read()
  usock.close()
  return data


def parse(data, pattern):
  """
    Returns the list with each n-tuple corresponding to a row
    in the table we are interested in, given the data.
  """
  # Extract only the table section of the data back into data
  data = re.search(r'<table class="raceResults".*?</tr>(.*?)</table>',data).group(1)

  # Do the actual matching and return results of list of n-tuples
  pattern_c = re.compile(pattern, re.VERBOSE)
  match     = re.findall(pattern_c, data)

  return match


def writeCSV(name, location, year, headers, data):
  """
    Writes data to CSV format
  """  
  # Generate path and filename from information
  path     = '../CSVs/' + name + '/'
  filename = name.lower() + '_' + location.lower() + '_' + year + '.csv'
  
  # If path does not exist, create directory
  if not os.path.exists(path): os.makedirs(path)

  # Write results to file
  fo = open(path + filename, 'w')
  fo.write(",".join(headers) + "\n")
  for elem in data:
    fo.write(",".join(list(elem) + [year, location]) + "\n")



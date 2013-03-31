import helper

HEADER  = 0
PATTERN = 1

REGEXES = {
  'START_OF_ROW'     : r'<tr>\s*', 
  'COLUMN'           : r'<td[^>]*>([^<]*)</td>\s*', 
  'COLUMN_WITH_LINK' : r'<td[^>]*><a[^>]*>([^<]*)</a></td>\s*',
  'END_OF_ROW'       : r'</tr>'
}

# REGEXES['<td>...</td>']
# REGEXES['<td><a>...</a></td>']
HEADERS_AND_PATTERNS = {

  'pit_stops' : [ 

    ['Stops', 'No', 'Driver', 'Team', 'Lap', 'Time of Day', 'Time', 'Total Time', 'Year', 'Grand Prix'], 

    REGEXES['START_OF_ROW'] + 
    REGEXES['COLUMN'] * 2 +
    REGEXES['COLUMN_WITH_LINK'] * 2 +
    REGEXES['COLUMN'] * 4 + 
    REGEXES['END_OF_ROW']
  ],

  'fastest_laps' : [ 

    ['Pos', 'No', 'Driver', 'Team', 'Lap', 'Time of Day', 'Avg Speed', 'Time', 'Year', 'Grand Prix'],

    REGEXES['START_OF_ROW'] + 
    REGEXES['COLUMN'] * 2 +
    REGEXES['COLUMN_WITH_LINK'] * 2 +
    REGEXES['COLUMN'] * 4 +
    REGEXES['END_OF_ROW']
  ], 

  'fp1' : [ 

    ['Pos', 'No', 'Driver', 'Team', 'Time/Retired', 'Gap', 'Laps', 'Year', 'Grand Prix'],

    REGEXES['START_OF_ROW'] +
    REGEXES['COLUMN'] * 2 +
    REGEXES['COLUMN_WITH_LINK'] * 2 +
    REGEXES['COLUMN'] * 3 +
    REGEXES['END_OF_ROW']
  ],

  'fp2' : [ 

    ['Pos', 'No', 'Driver', 'Team', 'Time/Retired', 'Gap', 'Laps', 'Year', 'Grand Prix'],

    REGEXES['START_OF_ROW'] +
    REGEXES['COLUMN'] * 2 +
    REGEXES['COLUMN_WITH_LINK'] * 2 +
    REGEXES['COLUMN'] * 3 +
    REGEXES['END_OF_ROW']
  ],

  'fp3' : [ 

    ['Pos', 'No', 'Driver', 'Team', 'Time/Retired', 'Gap', 'Laps', 'Year', 'Grand Prix'],

    REGEXES['START_OF_ROW'] +
    REGEXES['COLUMN'] * 2 +
    REGEXES['COLUMN_WITH_LINK'] * 2 +
    REGEXES['COLUMN'] * 3 +
    REGEXES['END_OF_ROW']
  ],

  'qualifying' : [ 

    ['Pos', 'No', 'Driver', 'Team', 'Q1', 'Q2', 'Q3', 'Laps', 'Year', 'Grand Prix'],

    REGEXES['START_OF_ROW'] + 
    REGEXES['COLUMN'] * 2 + 
    REGEXES['COLUMN_WITH_LINK'] * 2 + 
    REGEXES['COLUMN'] * 4 +
    REGEXES['END_OF_ROW']
  ], 

  'race' : [ 

    ['Pos', 'No', 'Driver', 'Team', 'Laps', 'Time/Retired', 'Grid', 'Pts', 'Year', 'Grand Prix'],

    REGEXES['START_OF_ROW'] + 
    REGEXES['COLUMN'] * 2 +
    REGEXES['COLUMN_WITH_LINK'] * 2 +
    REGEXES['COLUMN'] * 4 +
    REGEXES['END_OF_ROW']
  ]

}


for this_type in HEADERS_AND_PATTERNS: 

  # File with each line of location, year, URL to parse
  fi = open('../inputs/' + this_type + '.txt', 'r')

  # For each input, retrieve data, then parse data and store it
  for line in fi:

    # Inputs of Location, Year, URL
    inputs = line.strip().split(',')
    
    # Only process if input is as expected to contain location, year, url
    if len(inputs) == 3:
      location  = inputs[0]
      year      = inputs[1]
      url       = inputs[2]

      # Retrieve data from URL
      data = helper.retrieveSourceFromURL(url)

      # Remove all newline carriages
      data = data.split('\r\n')
      data = "".join(data)

      # Parse data into proper format of list of n-tuples
      data = helper.parse(data, HEADERS_AND_PATTERNS[this_type][PATTERN])

      # Generate CSV file for result
      helper.writeCSV(
        this_type, 
        location, 
        year, 
        HEADERS_AND_PATTERNS[this_type][HEADER], 
        data)
    
    # Notify of invalid input parameters
    else:
      print "INVALID INPUT"








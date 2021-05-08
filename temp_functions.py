"""
THis file includes two functions
"""

def faht_to_celsius(temp_fahrnheit):
  """
  converts the input temperature from degrees Fahrenheit to degrees Celsius
  
  parameter:temp_fahrenheit
  return:converted_temp
  """
  
  conberted_temp=(temp_fahtenheit-32)/1.8
  return conberted__temp

def temp_classifier(temp_celsius):
  """
  accepts a temperarute value in Celsius that eoll be reclassified into integer numbers 0-3 based on following ctiretia
  
  parameter]temp_celsous
  return]
  Classiffied number(0~3)
  """
  
  if temp_celsius<-2:
    return 0
  elif temp_celsius<2:
    return 1
  elif temp_celsius<15:
    return 2
  elif temp_celsius>=15:
    return 3
 

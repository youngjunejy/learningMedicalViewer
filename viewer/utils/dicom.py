import math

# def getColorWindowLevel(reader, total_slices):
#   total_windows = 0
#   count = 0

#   for i in range(total_slices):
#     if(reader.HasMetaDataKey(i, '0028|1051')):
#       total_windows += float(reader.GetMetaData(i, '0028|1051'))
#       count += 1

#   average_window = total_windows / count
#   level = math.ceil(average_window / 2)

#   return average_window, level

def getColorWindowLevel(reader, total_slices):
  window = 0
  level = 0
  center_index = total_slices // 2

  if(reader.HasMetaDataKey(center_index, '0028|1051') and reader.HasMetaDataKey(center_index, '0028|1050')):
    window = float(reader.GetMetaData(center_index, '0028|1051'))
    level = float(reader.GetMetaData(center_index, '0028|1050'))

  return window, level
import math
import numpy as np
import vtkmodules.util.numpy_support as vtk_np

def getWindowLevel(imageData):
  window = 0
  level = 0
  
  numpy_array = vtk_np.vtk_to_numpy(imageData.GetPointData().GetScalars())
  percentile_1 = np.percentile(numpy_array, 0.1)
  percentile_99 = np.percentile(numpy_array, 99.9)
  window = float(percentile_99 - percentile_1)
  level = float(percentile_99 + percentile_1)/2
  return window, level
  
# def getDicomWindowLevel(reader):
#   window = 0
#   level = 0
#   index = 0

#   if(reader.HasMetaDataKey(index, '0028|1051') and reader.HasMetaDataKey(index, '0028|1050')):
#     window = float(reader.GetMetaData(index, '0028|1051'))
#     level = float(reader.GetMetaData(index, '0028|1050'))

#   return window, level
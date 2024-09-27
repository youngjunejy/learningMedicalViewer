# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkRenderingCore import (
    vtkImageSlice,
    vtkImageSliceMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
from vtkmodules.vtkCommonDataModel import vtkImageData
from vtkmodules.vtkCommonCore import VTK_DOUBLE, vtkDoubleArray
from vtkmodules.vtkCommonColor import vtkNamedColors

import SimpleITK as sitk
from SimpleITK.utilities.vtk import sitk2vtk

def main():
  reader = sitk.ImageSeriesReader()
  dicom_names = reader.GetGDCMSeriesFileNames('./sample-data/Circle of Willis')
  reader.SetFileNames(dicom_names)
  image = reader.Execute()
  
  imageData = sitk2vtk(image)
  
  mapper = vtkImageSliceMapper()
  # mapper.SetSliceNumber(2)
  mapper.SetInputData(imageData)
  
  actor = vtkImageSlice()
  actor.SetMapper(mapper)

  renderer = vtkRenderer()
  renderer.AddActor(actor)
  colors = vtkNamedColors()
  renderer.SetBackground(colors.GetColor3d('White'))
  renderer.ResetCamera()

  renderWindow = vtkRenderWindow()
  renderWindow.AddRenderer(renderer)

  renderWindowInteractor = vtkRenderWindowInteractor()

  renderWindowInteractor.SetRenderWindow(renderWindow)
  renderWindowInteractor.Initialize()
  renderWindowInteractor.Start()


if __name__ == "__main__":
    main()
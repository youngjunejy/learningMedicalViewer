from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderer
)
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkInteractionImage import (vtkImageViewer2, vtkResliceImageViewer)
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor
from vtkmodules.vtkCommonColor import vtkNamedColors

from core.resliceViewer import ResliceViewer

def main(argv):
  colors = vtkNamedColors()
  reader = vtkDICOMImageReader()
  reader.SetDirectoryName('./sample-data/Circle of Willis')
  reader.Update()

  renWin = vtkRenderWindow()
  renWin.SetWindowName('LearningMedicalViewer')
  renWin.SetSize(800, 800)

  # axialRenderer = vtkRenderer()
  # axialRenderer.SetViewport(0, 0.5, 0.5, 1)
  # axialRenderer.SetBackground(colors.GetColor3d('DodgerBlue'))
  # axialImageViewer = vtkImageViewer2()
  # axialImageViewer.SetInputConnection(reader.GetOutputPort())
  # axialImageViewer.SetRenderer(axialRenderer)
  # axialImageViewer.SetRenderWindow(renWin)
  # axialImageViewer.SetupInteractor(renWin.GetInteractor())
  # axialImageViewer.Render()
  # renWin.AddRenderer(axialRenderer)

  axialRenderer = vtkRenderer()
  axialRenderer.SetViewport(0, 0.5, 0.5, 1)
  axialRenderer.SetBackground(colors.GetColor3d('DodgerBlue'))
  axialImageViewer = vtkResliceImageViewer()
  axialImageViewer.SetSliceOrientationToXY()
  axialImageViewer.SetInputConnection(reader.GetOutputPort())
  axialImageViewer.SetRenderer(axialRenderer)
  axialImageViewer.SetRenderWindow(renWin)
  axialImageViewer.SetupInteractor(renWin.GetInteractor())
  axialImageViewer.Render()
  renWin.AddRenderer(axialRenderer)

  coronalRenderer = vtkRenderer()
  coronalRenderer.SetViewport(0, 0, 0.5, 0.5)
  coronalRenderer.SetBackground(colors.GetColor3d('DodgerBlue'))
  coronalImageViewer = vtkResliceImageViewer()
  coronalImageViewer.SetSliceOrientationToXZ()
  coronalImageViewer.SetInputConnection(reader.GetOutputPort())
  coronalImageViewer.SetRenderWindow(renWin)
  coronalImageViewer.SetRenderer(coronalRenderer)
  coronalImageViewer.SetupInteractor(renWin.GetInteractor())
  coronalImageViewer.Render()
  renWin.AddRenderer(coronalRenderer)

  sagittalRenderer = vtkRenderer()
  sagittalRenderer.SetViewport(0.5, 0, 1, 0.5)
  sagittalRenderer.SetBackground(colors.GetColor3d('DodgerBlue'))
  sagittalImageViewer = vtkResliceImageViewer()
  sagittalImageViewer.SetSliceOrientationToYZ()
  sagittalImageViewer.SetInputConnection(reader.GetOutputPort())
  sagittalImageViewer.SetRenderWindow(renWin)
  sagittalImageViewer.SetRenderer(sagittalRenderer)
  sagittalImageViewer.SetupInteractor(renWin.GetInteractor())
  sagittalImageViewer.Render()
  renWin.AddRenderer(sagittalRenderer)

  iren = vtkRenderWindowInteractor()
  iren.SetRenderWindow(renWin)
  iren.Initialize()
  iren.Start()

if __name__ == '__main__':
    import sys

    main(sys.argv)
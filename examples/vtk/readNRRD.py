#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import (vtkDICOMImageReader, vtkNrrdReader)
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor

def main():
    colors = vtkNamedColors()

    # Read the DICOM file
    reader = vtkNrrdReader()
    reader.SetFileName('./sample-data/CT-chest.nrrd')
    reader.Update()

    # Visualize
    image_viewer = vtkImageViewer2()
    image_viewer.SetInputConnection(reader.GetOutputPort())
    render_window_interactor = vtkRenderWindowInteractor()
    image_viewer.SetupInteractor(render_window_interactor)
    image_viewer.Render()
    image_viewer.GetRenderer().SetBackground(colors.GetColor3d("SlateGray"))
    image_viewer.GetRenderWindow().SetWindowName("Read NRRD")
    image_viewer.GetRenderer().ResetCamera()
    image_viewer.Render()

    render_window_interactor.Start()


if __name__ == "__main__":
    main()
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
from vtkmodules.vtkRenderingCore import (
    vtkActor2D,
    vtkRenderWindowInteractor,
    vtkTextMapper,
    vtkTextProperty
)
from vtkmodules.vtkCommonDataModel import vtkImageData
import numpy as np
from vtkmodules.util.numpy_support import vtk_to_numpy

def main():
    colors = vtkNamedColors()

    reader = vtkDICOMImageReader()
    reader.SetDirectoryName('./sample-data/Circle of Willis')
    reader.Update()
    image_data = vtkImageData.SafeDownCast(reader.GetOutput())
    image_array = vtk_to_numpy(image_data.GetPointData().GetScalars())
    dimensions = image_data.GetDimensions()
    image_array = np.reshape(image_array, (dimensions[2], dimensions[1], dimensions[0]))

    for i in range(100):
      for j in range(100):
        image_array[0, i, j] = 255

    image_viewer = vtkImageViewer2()
    image_viewer.SetInputConnection(reader.GetOutputPort())
    render_window_interactor = vtkRenderWindowInteractor()
    image_viewer.SetupInteractor(render_window_interactor)
    render_window_interactor.Render()

    image_viewer.SetSlice(0)
    image_viewer.Render()
    image_viewer.GetRenderer().ResetCamera()
    image_viewer.GetRenderer().SetBackground(colors.GetColor3d('SlateGray'))
    image_viewer.GetRenderWindow().SetSize(800, 800)
    image_viewer.GetRenderWindow().SetWindowName('ReadDICOMSeries')
    image_viewer.Render()
    render_window_interactor.Start()


if __name__ == '__main__':
    main()
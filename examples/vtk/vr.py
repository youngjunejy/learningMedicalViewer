#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import (vtkDICOMImageReader, vtkNrrdReader)
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor
import vtkmodules.vtkInteractionStyle
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPiecewiseFunction
from vtkmodules.vtkIOLegacy import vtkStructuredPointsReader
from vtkmodules.vtkRenderingCore import (
    vtkColorTransferFunction,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkVolume,
    vtkVolumeProperty
)
from vtkmodules.vtkRenderingVolume import vtkGPUVolumeRayCastMapper
# noinspection PyUnresolvedReferences
from vtkmodules.vtkRenderingVolumeOpenGL2 import vtkOpenGLRayCastImageDisplayHelper

def main():
    colors = vtkNamedColors()

    # Read the DICOM file
    reader = vtkNrrdReader()
    reader.SetFileName('.\sample-data\/nrrd\CT-chest.nrrd')
    reader.Update()

    colors = vtkNamedColors()
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    
    # Create transfer mapping scalar value to opacity.
    opacityTransferFunction = vtkPiecewiseFunction()
    opacityTransferFunction.AddPoint(20, 0.0)
    opacityTransferFunction.AddPoint(255, 0.2)

    # Create transfer mapping scalar value to color.
    colorTransferFunction = vtkColorTransferFunction()
    colorTransferFunction.AddRGBPoint(0.0, 0.0, 0.0, 0.0)
    colorTransferFunction.AddRGBPoint(64.0, 1.0, 0.0, 0.0)
    colorTransferFunction.AddRGBPoint(128.0, 0.0, 0.0, 1.0)
    colorTransferFunction.AddRGBPoint(192.0, 0.0, 1.0, 0.0)
    colorTransferFunction.AddRGBPoint(255.0, 0.0, 0.2, 0.0)
    
    # The property describes how the data will look.
    volumeProperty = vtkVolumeProperty()
    volumeProperty.SetColor(colorTransferFunction)
    volumeProperty.SetScalarOpacity(opacityTransferFunction)
    volumeProperty.ShadeOn()
    volumeProperty.SetInterpolationTypeToLinear()
    
    volumeMapper = vtkGPUVolumeRayCastMapper()
    volumeMapper.SetInputConnection(reader.GetOutputPort())

    volume = vtkVolume()
    volume.SetMapper(volumeMapper)
    volume.SetProperty(volumeProperty)

    ren.AddVolume(volume)
    ren.SetBackground(colors.GetColor3d('Wheat'))
    ren.GetActiveCamera().Azimuth(45)
    ren.GetActiveCamera().Elevation(30)
    ren.ResetCameraClippingRange()
    ren.ResetCamera()

    renWin.SetSize(600, 600)
    renWin.SetWindowName('SimpleRayCast')
    renWin.Render()

    iren.Start()


if __name__ == "__main__":
    main()
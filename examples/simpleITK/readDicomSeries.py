import SimpleITK as sitk
import sys
import os

reader = sitk.ImageSeriesReader()

dicom_names = reader.GetGDCMSeriesFileNames('./sample-data/Circle of Willis')

# print(dicom_names)

reader.SetFileNames(dicom_names)

image = reader.Execute()

# print(image)

size = image.GetSize()

print("Image size:", size[0], size[1], size[2])

if "SITK_NOSHOW" not in os.environ:
    sitk.Show(image, "Dicom Series")
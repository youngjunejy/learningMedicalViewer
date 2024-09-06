import numpy as np
import pydicom
import vtk

def computeIJKToRASMatrix(dicomFile):
    # 读取 DICOM 文件
    ds = pydicom.dcmread(dicomFile)

    # 提取 DICOM 元数据
    pixelSpacing = ds.PixelSpacing
    sliceThickness = ds.SliceThickness
    imageOrientationPatient = ds.ImageOrientationPatient
    imagePositionPatient = ds.ImagePositionPatient

    # 计算方向余弦矩阵
    orientationMatrix = np.array(imageOrientationPatient).reshape(2, 3)
    orientationMatrix = np.vstack([orientationMatrix, np.cross(orientationMatrix[0], orientationMatrix[1])])

    # 计算 IJK 到 RAS 的转换矩阵
    ijkToRAS = np.eye(4)
    ijkToRAS[:3, :3] = orientationMatrix * np.array([pixelSpacing[0], pixelSpacing[1], sliceThickness])
    ijkToRAS[:3, 3] = imagePositionPatient

    # 转换为 VTK 矩阵
    vtkMatrix = vtk.vtkMatrix4x4()
    for i in range(4):
        for j in range(4):
            vtkMatrix.SetElement(i, j, ijkToRAS[i, j])

    return vtkMatrix

# 示例使用
dicomFile = "path/to/dicom/file.dcm"
ijkToRASMatrix = computeIJKToRASMatrix(dicomFile)
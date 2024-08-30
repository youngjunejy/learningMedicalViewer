# learningMedicalViewer

## doing

- 实现 MPR 渲染，使用 vtkResliceCursor？去阅读开源项目如何实现，要看 3D slicer 如何实现。

## 计划

- 支持 DICOM 数据格式的相关功能
- UI 相关的工作靠后

## 功能

- [ ] 数据读取
  - [x] DICOM
  - [ ] NRRD
  - [ ] NIFTI
- [ ] 辅助观察
  - 渲染
    - [ ] MPR
    - [ ] CPR
    - [ ] SSD
    - [ ] MIP
    - [ ] MinIP
    - [ ] VR
    - [ ] VE
  - 操作
    - [ ] pan
    - [ ] zoom
    - [ ] rotate
    - [ ] window level
- [ ] 辅助诊断
  - [ ] 测量
  - [ ] 分割
  - [ ] 检测
  - [ ] 配准

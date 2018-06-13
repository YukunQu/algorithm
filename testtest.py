import nibabel as nib
import numpy as np

regisROI_img = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206/regis_ROI/100206_ATR_roi1_L.nii.gz')
oriROI_img = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/tract_ROI/ATR_roi1_L.nii.gz')
regisROI_img_data = regisROI_img.get_data()
oriROI_img_data  = oriROI_img.get_data()


value1 = []
for i in range(182):
    for j in range(218):
        for k in range(182):
            if oriROI_img_data[i][j][k] > 0:
                value1.append([i,j,k])

print(len(value1))

value2 = []
for i in range(145):
    for j in range(174):
        for k in range(145):
            if regisROI_img_data[i][j][k] > 0:
                value2.append([i,j,k])
print(len(value2))
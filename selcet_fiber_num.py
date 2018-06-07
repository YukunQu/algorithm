# -*- coding: utf-8 -*-
import save
moriRois = ['ATR_roi1_R.nii.gz', 'ATR_roi2_R.nii.gz',
            'CST_roi1_L.nii.gz', 'CST_roi2_L.nii.gz', 'CST_roi1_R.nii.gz', 'CST_roi2_R.nii.gz',
            'CGC_roi1_L.nii.gz', 'CGC_roi2_L.nii.gz', 'CGC_roi1_R.nii.gz', 'CGC_roi2_R.nii.gz',
            'HCC_roi1_L.nii.gz', 'HCC_roi2_L.nii.gz', 'HCC_roi1_R.nii.gz', 'HCC_roi2_R.nii.gz',
            'IFO_roi1_L.nii.gz', 'IFO_roi2_L.nii.gz', 'IFO_roi1_R.nii.gz', 'IFO_roi2_R.nii.gz',
            'ILF_roi1_L.nii.gz', 'ILF_roi2_L.nii.gz', 'ILF_roi1_R.nii.gz', 'ILF_roi2_R.nii.gz',
            'SLF_roi1_L.nii.gz', 'SLF_roi2_L.nii.gz', 'SLF_roi1_R.nii.gz', 'SLF_roi2_R.nii.gz',
            'UNC_roi1_L.nii.gz', 'UNC_roi2_L.nii.gz', 'UNC_roi1_R.nii.gz', 'UNC_roi2_R.nii.gz',
            'SLF_roi1_L.nii.gz', 'SLFt_roi2_L.nii.gz','SLF_roi1_R.nii.gz', 'SLFt_roi2_R.nii.gz']
# roi list
roi1 = []
for i in range(0, 34, 2):
    roi1.append('100206_'+moriRois[i])

roi2 = []
for i in range(1, 34, 2):
    roi2.append('100206_'+moriRois[i])

#tck filename list
tck = []
for i in range(0,34,2):
    tck.append('100206_'+moriRois[i][0:3]+moriRois[i][-9:-7]+'.tck')


streamline = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206/result/1M_20_01_20dynamic250_SD_Stream.tck'

for i in range(0,17,1):
    roi1[i] = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206/regis_ROI/'+roi1[i]
    roi2[i] = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206/regis_ROI/'+roi2[i]
    save.save_selectfiber(roi1[i],roi2[i],streamline,tck[i])
    print('Already completed:',i+1)
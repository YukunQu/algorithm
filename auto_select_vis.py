import numpy as np
import nibabel as nib
import nibabel.streamlines.tck as nibtck
from dipy.tracking import streamline
from nibabel import streamlines
import vis

#load
img_T1w = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206'
                   '/Structural image/T1w_acpc_dc_restore_brain1.25.nii.gz')
img_roi1 = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206/regis_ROI/100206_CGC_roi1_L.nii.gz')
img_roi2 = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206/regis_ROI/100206_CGC_roi2_L.nii.gz')
img_fiber = nibtck.TckFile.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206'
                                '/result/1M_20_01_20dynamic250_SD_Stream.tck').streamlines
roi_affine = img_roi1.affine
img_roi1_data = img_roi1.get_data().astype(bool)
img_roi2_data = img_roi2.get_data().astype(bool)

#select
roi1_streamlines = streamline.select_by_rois(img_fiber,[img_roi1_data],[True],mode='any',affine=roi_affine)
streamlines1 = list(roi1_streamlines)
roi2_streamlines = streamline.select_by_rois(streamlines1,[img_roi2_data],[True],mode='any',affine=roi_affine)
streamlines2 = list(roi2_streamlines)

#save
tractogram = streamlines.tractogram.Tractogram(streamlines=roi2_streamlines)
datdat = nibtck.TckFile(tractogram=tractogram)
datdat.save('100206_CGC_L.tck')

#visualize--------------------------------------------------------------------------------------------------------------
vis.fiber_simple_3d_show_advanced(img_T1w,streamlines2,colors=None, linewidth=1)
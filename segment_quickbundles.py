import numpy as np
import nibabel as nib
import nibabel.streamlines.tck as nibtck
from dipy.segment.clustering import QuickBundles
from dipy.viz import window,actor

T1w = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/subjects/100206/T1w_acpc_dc_restore_brain1.25.nii.gz')
roi = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/subjects/100206/ROI/R_Occipital.nii.gz')
img_fiber = nibtck.TckFile.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/subjects/100307/Diffusion/tractography'
                                '/Det/SD_Stream_angle20_cutoff0.1_length20_100_seedAC0.7_100k.tck')

affine = roi.affine
img_fiber = img_fiber.streamlines
qb_streamline = QuickBundles(1.0)
fiber_clusters = qb_streamline.cluster(img_fiber)

#roi_affine = roi.affine
#img_roi_data = roi.get_data()

# Enables/disables interactive visualization
interactive = True

# Make display objects
colormap = actor.create_colormap(np.arange(len(fiber_clusters)))
streamlines_actor = actor.line(fiber_clusters.centroids,colormap,linewidth=5)
#cc_ROI_actor = actor.contour_from_roi(img_roi_data,roi_affine,color=(0.8, 0.5, 0.31),
#                                      opacity=0.5)

img_T1w_data = T1w.get_data()
vol_actor = actor.slicer(img_T1w_data,affine)

vol_actor.display(x=72)
vol_actor2 = vol_actor.copy()
vol_actor2.display(z=50)

# Add display objects to canvas
r = window.Renderer()
r.add(vol_actor)
r.add(vol_actor2)
#r.add(cc_ROI_actor)
r.add(streamlines_actor)

# Save figures
if interactive:
    window.show(r)
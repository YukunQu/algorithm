from dipy.viz import window, actor
from dipy.viz.colormap import line_colors
import nibabel as nib
import nibabel.streamlines.tck as nibtck

img_T1w = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206'
                   '/Structural image/T1w_acpc_dc_restore_brain1.25.nii.gz')
img_roi1 = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206/regis_ROI/100206_SLF_roi1_L.nii.gz')
img_roi2 = nib.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206/regis_ROI/100206_SLF_roi2_L.nii.gz')
img_fiber = nibtck.TckFile.load('/nfs/s2/userhome/quyukun/workingdir/fiberdata/100206/selectedfiber/'
                                '100206_SLF_L.tck').streamlines

roi_affine = img_roi1.affine
img_roi1_data = img_roi1.get_data()
img_roi2_data = img_roi2.get_data()

# Enables/disables interactive visualization
interactive = True

# Make display objects
color = line_colors(img_fiber)
cc_streamlines_actor = actor.line(img_fiber, line_colors(img_fiber))
cc_ROI_actor1 = actor.contour_from_roi(img_roi1_data,affine=roi_affine,color=(0.7, 0.7, 0.7),
                                      opacity=0.5)
cc_ROI_actor2 = actor.contour_from_roi(img_roi2_data,roi_affine,color=(0.7, 0.7, 0.7),
                                      opacity=0.5)

img_T1w_data = img_T1w.get_data()
img_T1w_affine = img_T1w.get_data
vol_actor = actor.slicer(img_T1w_data,roi_affine)

vol_actor.display(x=72)
vol_actor2 = vol_actor.copy()
vol_actor2.display(z=50)

# Add display objects to canvas
r = window.Renderer()
r.add(vol_actor)
r.add(vol_actor2)
r.add(cc_streamlines_actor)
r.add(cc_ROI_actor1)
r.add(cc_ROI_actor2)

# Save figures

if interactive:
    window.show(r)
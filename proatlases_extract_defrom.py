import nibabel as nib
import numpy as np
import auto_deformable
#extract special fiber probability atlas from standard atlas,JHU-ICBM-tracts-prob-2mm.nii.gz.

#extract
pro_atlas_path = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/JHU-ICBM-tracts-prob-2mm.nii.gz'
output_name = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/Forceps_major_prob_2mm.nii.gz'

proatlas = nib.load(pro_atlas_path)
affine = proatlas.affine

proatlas_data = proatlas.get_data()
coordinate_shape = proatlas_data.shape[:3]

extract_atlas = np.zeros(coordinate_shape)

for i in range(proatlas_data.shape[0]):
    for j in range(proatlas_data.shape[1]):
        for k in range(proatlas_data.shape[2]):
            if proatlas_data[i][j][k][8] > 0 :
                extract_atlas[i][j][k] = proatlas_data[i][j][k][8]

#save as Nifti
dm_img = nib.Nifti1Image(extract_atlas,affine)
dm_img.to_filename(output_name)


subject_img = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/testAnts/T1w_acpc_dc_restore_brain1.25.nii.gz'
standard_T1w_img = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/testAnts/MNI152_T1_2mm_brain.nii.gz'
moving_image = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/testAnts/Forceps_major_prob_2mm.nii.gz'
subject_num  = '100206'
outputname = subject_num + '_'+ 'Forceps_major_prob_2mm.nii.gz'

auto_deformable.antsRegistration(subject_img,standard_T1w_img,subject_num)

auto_deformable.antApplyTransforms(subject_img,moving_image,subject_num,outputname)


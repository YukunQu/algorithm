import auto_deformable

# imput filename or path
fixed_image  = ''
moving_image = ''
subject_num  = ''
moving_images_path = ''
moving_images = ['ATR_roi1_L.nii.gz', 'ATR_roi2_L.nii.gz', 'ATR_roi1_R.nii.gz', 'ATR_roi2_R.nii.gz',
                'CST_roi1_L.nii.gz', 'CST_roi2_L.nii.gz', 'CST_roi1_R.nii.gz', 'CST_roi2_R.nii.gz',
                'CGC_roi1_L.nii.gz', 'CGC_roi2_L.nii.gz', 'CGC_roi1_R.nii.gz', 'CGC_roi2_R.nii.gz',
                'HCC_roi1_L.nii.gz', 'HCC_roi2_L.nii.gz', 'HCC_roi1_R.nii.gz', 'HCC_roi2_R.nii.gz',
                'FP_R.nii.gz', 'FP_L.nii.gz', 'FA_L.nii.gz', 'FA_R.nii.gz',
                'IFO_roi1_L.nii.gz', 'IFO_roi2_L.nii.gz', 'IFO_roi1_R.nii.gz', 'IFO_roi2_R.nii.gz',
                'ILF_roi1_L.nii.gz', 'ILF_roi2_L.nii.gz', 'ILF_roi1_R.nii.gz', 'ILF_roi2_R.nii.gz',
                'SLF_roi1_L.nii.gz', 'SLF_roi2_L.nii.gz', 'SLF_roi1_R.nii.gz', 'SLF_roi2_R.nii.gz',
                'UNC_roi1_L.nii.gz', 'UNC_roi2_L.nii.gz', 'UNC_roi1_R.nii.gz', 'UNC_roi2_R.nii.gz',
                'SLF_roi1_L.nii.gz', 'SLFt_roi2_L.nii.gz', 'SLF_roi1_R.nii.gz', 'SLFt_roi2_R.nii.gz']

#registration and applyTransforms
auto_deformable.antsRegistration(fixed_image,moving_image,subject_num)

for image in moving_images:
    auto_deformable.antApplyTransforms(fixed_image,image,subject_num)


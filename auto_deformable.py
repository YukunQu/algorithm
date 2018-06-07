def auto_deformable(fixed_image,moving_image,subject_num):

    # This process can register 40 ROI to one subject native space.
    #  fixed image to which we register the moving image,absolute path,type:string;
    #  moving image to be mapped to fixed space,absolute path,type:string;
    #  subject_num,type:string
    import subprocess
    # first,we try to acquire the affine matrix.
    subprocess.call('antsRegistrationSyNQuick.sh -d 3 -f {} -m {} -o {}'.format(fixed_image,moving_image,subject_num),
                    shell = True)
    print('Affine and Warp files acquired')
    # second,we registering 40 ROI to subject native space.Apparently,it needs a circulation.
    moriRois = ['ATR_roi1_L.nii.gz', 'ATR_roi2_L.nii.gz', 'ATR_roi1_R.nii.gz', 'ATR_roi2_R.nii.gz',
                'CST_roi1_L.nii.gz', 'CST_roi2_L.nii.gz', 'CST_roi1_R.nii.gz', 'CST_roi2_R.nii.gz',
                'CGC_roi1_L.nii.gz', 'CGC_roi2_L.nii.gz', 'CGC_roi1_R.nii.gz', 'CGC_roi2_R.nii.gz',
                'HCC_roi1_L.nii.gz', 'HCC_roi2_L.nii.gz', 'HCC_roi1_R.nii.gz', 'HCC_roi2_R.nii.gz',
                'FP_R.nii.gz', 'FP_L.nii.gz', 'FA_L.nii.gz', 'FA_R.nii.gz',
                'IFO_roi1_L.nii.gz', 'IFO_roi2_L.nii.gz', 'IFO_roi1_R.nii.gz', 'IFO_roi2_R.nii.gz',
                'ILF_roi1_L.nii.gz', 'ILF_roi2_L.nii.gz', 'ILF_roi1_R.nii.gz', 'ILF_roi2_R.nii.gz',
                'SLF_roi1_L.nii.gz', 'SLF_roi2_L.nii.gz', 'SLF_roi1_R.nii.gz', 'SLF_roi2_R.nii.gz',
                'UNC_roi1_L.nii.gz', 'UNC_roi2_L.nii.gz', 'UNC_roi1_R.nii.gz', 'UNC_roi2_R.nii.gz',
                'SLF_roi1_L.nii.gz', 'SLFt_roi2_L.nii.gz', 'SLF_roi1_R.nii.gz', 'SLFt_roi2_R.nii.gz']
    a = '1Warp.nii.gz'
    b = '0GenericAffine.mat'

    for i in moriRois:
        subprocess.call('antsApplyTransforms -d 3 -e 0 -i ./tract_ROI/{} -r {} -t {} -t {} -o {}'.format(i,
                        fixed_image,subject_num+a,subject_num+b,subject_num+'_'+i),shell = True)


auto_deformable('/nfs/s2/userhome/quyukun/workingdir/fiberdata/testAnts/T1w_acpc_dc_restore_brain1.25.nii.gz',
                '/nfs/s2/userhome/quyukun/workingdir/fiberdata/testAnts/MNI152_T1_2mm_brain.nii.gz','100206')
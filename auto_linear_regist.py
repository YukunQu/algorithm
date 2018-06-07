def auto_linear_regist(x,y):

    # This is a test file to code a process which can register 40 ROI to one subject native space.
    # x is ref that subject NIFIT file; y is part of name of output file.
    import subprocess
    # first,we try to acquire the affine matrix.

    subprocess.call('flirt -in MNI152_T1_2mm_brain.nii.gz -ref {} -omat affinematrix.mat'.format(x),shell=True)

    print('matrix acquired')

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

    for i in moriRois:
        subprocess.call("flirt -interp nearestneighbour -in ./tract_ROI/{} -ref {} -applyxfm -init affinematrix.mat "
                        "-out {}".format(i,x,y + i),shell = True)

auto_regist('T1w_acpc_dc_restore_brain1.25.nii.gz','brain1.25_')
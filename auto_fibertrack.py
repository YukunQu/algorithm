import subprocess
"""
5ttgen fsl T1w_acpc_dc_restore_brain1.25.nii.gz 5TT.mif -premasked

mrconvert data.nii.gz DWI.mif -fslgrad bvecs bvals -datatype float32 -stride 0,0,0,1

dwiextract DWI.mif - -bzero | mrmath - mean mean0.mif -axis 3

dwi2response dhollander DWI.mif RF_WM.txt RF_GM.txt RF_CSF.txt -voxels RF_voxels.mif

dwi2fod msmt_csd DWI.mif RF_WM.txt WM_FODs.mif RF_GM.txt GM.mif RF_CSF.txt CSF.mif -mask nodif_brain_mask.nii.gz

tckgen WM_FODs.mif 1M_20_01_20dynamic250_SD_Stream.tck -algorithm SD_Stream -act 5TT.mif -crop_at_gmwmi -seed_dynamic WM_FODs.mif -angle 20 -minlength 20 -maxlength 250 -select 1M -cutoff 0.1
"""
def auto_fibertrack():
    subprocess.call(''.format(),shell=True)

    subprocess.call(''.format(), shell=True)

    subprocess.call(''.format(), shell=True)

    subprocess.call(''.format(), shell=True)

    subprocess.call(''.format(), shell=True)

    print('fiber tarcking has finished. ')
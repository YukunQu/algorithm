import subprocess


def antsRegistration(fixed_image,moving_image,subject_num):
    #  fixed image to which we register the moving image,absolute path,type:string;
    #  moving image to be mapped to fixed space,absolute path,type:string;
    #  subject_num,type:string
    # first,we try to acquire the affine matrix and Warp.
    # all files need to be placed in same directory.
    subprocess.call('antsRegistrationSyNQuick.sh -d 3 -f {} -m {} -o {}'.format(fixed_image,moving_image,subject_num),
                    shell = True)
    print('Affine and Warp files acquired')

def antApplyTransforms(fixed_image,moving_image,subject_num,outputname):
    # second,we apply transforms to more moving images to subject native space.Apparently,it needs a circulation.
    a = '1Warp.nii.gz'
    b = '0GenericAffine.mat'
    subprocess.call('antsApplyTransforms -d 3 -e 0 -i {} -r {} -t {} -t {} -o {}'.format(moving_image,
                    fixed_image,subject_num+a,subject_num+b,outputname),shell = True)

a = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/testAnts/T1w_acpc_dc_restore_brain1.25.nii.gz'
b = '/nfs/s2/userhome/quyukun/workingdir/fiberdata/testAnts/MNI152_T1_2mm_brain.nii.gz'
c = '100206'
antsRegistration(a,b,c)


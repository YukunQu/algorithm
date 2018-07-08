import subprocess

def antsRegistration(fixed_image,moving_image,output_name):
    #  fixed image to which we register the moving image,absolute path,type:string;
    #  moving image to be mapped to fixed space,absolute path,type:string;
    subprocess.call('antsRegistrationSyNQuick.sh -d 3 -f {} -m {} -o {}'.format(fixed_image,moving_image,output_name),
                    shell = True)
    print('Affine and Warp files acquired')


def antsApplyTransforms_e0(fixed_image,moving_image,affine,warp,outputname):
    # t1 : path of GenericAffine.mat
    # t2 : path of Warp.nii.gz'
    subprocess.call('antsApplyTransforms -d 3 -e 0 -i {} -r {} -t {} -t {} -o {}'.format(moving_image,
                    fixed_image,affine,warp,outputname),shell = True)


def antsApplyTransforms_e3(fixed_image,moving_image,affine,warp,outputname):
    # t1 : path of GenericAffine.mat
    # t2 : path of Warp.nii.gz'
    subprocess.call('antsApplyTransforms -d 3 -e 3 -i {} -r {} -t {} -t {} -o {}'.format(moving_image,
                    fixed_image,affine,warp,outputname),shell = True)
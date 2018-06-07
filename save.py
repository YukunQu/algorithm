import nibabel as nib
from nibabel import streamlines
from dipy.tracking import streamline

def save_selectfiber(roi1,roi2,Ori_fiber,Out_fiber):
    # roi1 : roi coordinate             format:nii.gz
    # roi2 : roi coordinate             format:nii.gz
    # Ori_fiber : Original fiber        format:tck
    # Out_fiber : selected fiber name   format:tck
    #load(pathname)

    # load
    roi1 = nib.load(roi1)
    roi2 = nib.load(roi2)
    Ori_fiber = streamlines.TckFile.load(Ori_fiber)

    roi_affine = roi1.affine
    roi1_data = roi1.get_data().astype(bool)
    roi2_data = roi2.get_data().astype(bool)
    stream_lines = Ori_fiber.streamlines
    header = Ori_fiber.header
    data_per_streamline = Ori_fiber.tractogram.data_per_streamline
    data_per_point = Ori_fiber.tractogram.data_per_point
    affine_to_rasmm = Ori_fiber.tractogram.affine_to_rasmm

    #select
    roi1_streamlines = streamline.select_by_rois(stream_lines,[roi1_data],[True],mode='any',affine=roi_affine)
    streamlines1 = list(roi1_streamlines)
    roi2_streamlines = streamline.select_by_rois(streamlines1,[roi2_data],[True],mode='any',affine=roi_affine)
    streamlines2 = list(roi2_streamlines)

    #save
    save_streamline = streamlines.array_sequence.ArraySequence(streamlines2)

    tractogram = streamlines.tractogram.Tractogram(streamlines=save_streamline,data_per_streamline=data_per_streamline,
                                                   data_per_point=data_per_point,affine_to_rasmm=affine_to_rasmm)
    datdat = streamlines.tck.TckFile(tractogram=tractogram,header=header)
    datdat.save(Out_fiber)







from pydra.engine import specs
from pydra import ShellCommandTask


input_fields = [
    (
        "in_file",
        str,  #specs.File,
        {
            "help_string": "Input file.",
            "argstr": "-in {in_file}",
            "mandatory": True,
            "position": 0,
        },
    ),
    (
        "reference",
        str,  #specs.File,
        {
            "help_string": "Reference file. ",
            "argstr": "-ref {reference}",
            "mandatory": True,
            "position": 1,
        },
    ),
    (
        "angle_rep",
        str,  # (‘quaternion’ or ‘euler’)
        {
            "help_string": "Representation of rotation angles.",
            "argstr": "-anglerep {angle_rep}",
        },
    ),
    (
        "apply_isoxfm",
        float,
        {
            "help_string": "As applyxfm but forces isotropic resampling.",
            "argstr": "-applyisoxfm {apply_isoxfm}",
            "xor": (
                "apply_xfm",
            ),
        },
    ),
    (
        "apply_xfm",
        bool,
        {
            "help_string": (
                "Apply transformation supplied by in_matrix_file or uses_qform "
                "to use the affine matrix stored in the reference header."
            ),
            "argstr": "-applyxfm",
            "xor": (
                "apply_isoxfm",
            )
        },
    ),
    (
        "bbrslope",
        float,
        {
            "help_string": "Value of bbr slope.",
            "argstr": "-bbrslope {bbrslope}",
        },
    ),
    (
        "bbrtype", # (‘signed’ or ‘global_abs’ or ‘local_abs’)
        str,
        {
            "help_string": "Type of bbr cost function: signed [default], global_abs, local_abs.",
            "argstr": "-bbrtype {bbrtype}",
        },
    ),
    (
        "bgvalue",
        float,
        {
            "help_string": "Use specified background value for points outside FOV.",
            "argstr": "-setbackground {bgvalue}",
        },
    ),
    (
        "bins",
        int,
        {
            "help_string": "Number of histogram bins.",
            "argstr": "-bins {bins}",
        },
    ),
    (
        "coarse_search",
        int,
        {
            "help_string": "Coarse search delta angle.",
            "argstr": "-coarsesearch {coarse_search}",
        },
    ),
    (
        "cost",  # (‘mutualinfo’ or ‘corratio’ or ‘normcorr’ or ‘normmi’ or ‘leastsq’ or ‘labeldiff’ or ‘bbr’)
        str,
        {
            "help_string": "Cost function.",
            "argstr": "-cost {cost}",
        },
    ),
    (
        "cost_func",  # (‘mutualinfo’ or ‘corratio’ or ‘normcorr’ or ‘normmi’ or ‘leastsq’ or ‘labeldiff’ or ‘bbr’)
        str,
        {
            "help_string": "Cost function.",
            "argstr": "-searchcost {cost_func}",
        },
    ),
    (
        "datatype",  # (‘char’ or ‘short’ or ‘int’ or ‘float’ or ‘double’)
        str,
        {
            "help_string": "Force output data type.",
            "argstr": "-datatype {datatype}",
        },
    ),
    (
        "display_init",
        bool,
        {
            "help_string": "Display initial matrix.",
            "argstr": "-displayinit",
        },
    ),
    (
        "dof",
        int,
        {
            "help_string": "Number of transform degrees of freedom.",
            "argstr": "-dof {dof}",
        },
    ),
    (
        "echospacing",
        float,
        {
            "help_string": "Value of EPI echo spacing - units of seconds.",
            "argstr": "-echospacing {echospacing}",
        },
    ),
    (
        "fieldmap",
        str,
        {
            "help_string": "Fieldmap image in rads/s - must be already registered to the reference image.",
            "argstr": "-fieldmap {fieldmap}",
        },
    ),
    (
        "fieldmapmask",
        str,
        {
            "help_string": "Mask for fieldmap image.",
            "argstr": "-fieldmapmask {fieldmapmask}",
        },
    ),
    (
        "fine_search",
        int,
        {
            "help_string": "Fine search delta angle.",
            "argstr": "-finesearch {fine_search}",
        },
    ),
    (
        "force_scaling",
        bool,
        {
            "help_string": "Force rescaling even for low-res images.",
            "argstr": "-forcescaling",
        },
    ),
    (
        "in_matrix_file",
        str,
        {
            "help_string": "Input 4x4 affine matrix.",
            "argstr": "-init {in_matrix_file}",
        },
    ),
    (
        "in_weight",
        str,
        {
            "help_string": "File for input weighting volume.",
            "argstr": "-inweight {in_weight}",
        },
    ),
    (
        "interp",  # (‘trilinear’ or ‘nearestneighbour’ or ‘sinc’ or ‘spline’)
        str,
        {
            "help_string": "Final interpolation method used in reslicing.",
            "argstr": "-interp {interp}",
        },
    ),
    (
        "min_sampling",
        float,
        {
            "help_string": "Set minimum voxel dimension for sampling.",
            "argstr": "-minsampling {min_sampling}",
        },
    ),
    (
        "no_clamp",
        bool,
        {
            "help_string": "Do not use intensity clamping.",
            "argstr": "-noclamp",
        },
    ),
    (
        "no_resample",
        bool,
        {
            "help_string": "Do not change input sampling.",
            "argstr": "-noresample",
        },
    ),
    (
        "no_resample_blur",
        bool,
        {
            "help_string": "Do not use blurring on downsampling.",
            "argstr": "-noresampblur",
        },
    ),
    (
        "no_search",
        bool,
        {
            "help_string": "Set all angular searches to ranges 0 to 0.",
            "argstr": "-nosearch",
        },
    ),
    (
        "out_file",
        str,
        {
            "help_string": "Registered output file.",
            "argstr": "-out {out_file}",
            "position": 2,
        },
    ),
    (
        "out_matrix_file",
        str,
        {
            "help_string": "Output affine matrix in 4x4 asciii format.",
            "argstr": "-omat {out_matrix_file}",
            "position": 3,
            "output_file_template": "{in_file}_flirt.mat",
        },
    ),
    (
        "padding_size",
        int,
        {
            "help_string": "For applyxfm: interpolates outside image by size.",
            "argstr": "-paddingsize {padding_size}",
        },
    ),
    (
        "pedir",
        int,
        {
            "help_string": "Phase encode direction of EPI - 1/2/3=x/y/z & -1/-2/-3=-x/-y/-z.",
            "argstr": "-pedir {pedir}",
        },
    ),
    (
        "ref_weight",
        str,
        {
            "help_string": "File for reference weighting volume.",
            "argstr": "-refweight {ref_weight}",
        },
    ),
    (
        "rigid2D",
        bool,
        {
            "help_string": "Use 2D rigid body mode - ignores dof.",
            "argstr": "-2D",
        },
    ),
    (
        "schedule",
        str,
        {
            "help_string": "Replaces default schedule.",
            "argstr": "-schedule {schedule}",
        },
    ),
    (
        "searchr_x",
        list,
        {
            "help_string": "Search angles along x-axis, in degrees.",
            "argstr": "-searchrx {searchr_x}",
        },
    ),
    (
        "searchr_y",
        list,
        {
            "help_string": "Search angles along y-axis, in degrees.",
            "argstr": "-searchry {searchr_y}",
        },
    ),
    (
        "searchr_z",
        list,
        {
            "help_string": "Search angles along z-axis, in degrees.",
            "argstr": "-searchrz {searchr_z}",
        },
    ),
    (
        "sinc_width",
        int,
        {
            "help_string": "Full-width in voxels.",
            "argstr": "-sincwidth {sinc_width}",
        },
    ),
    (
        "sinc_window",  # (‘rectangular’ or ‘hanning’ or ‘blackman’)
        str,
        {
            "help_string": "Sinc window.",
            "argstr": "-sincwindow {sinc_window}",
        },
    ),
    (
        "uses_qform",
        bool,
        {
            "help_string": "Initialize using sform or qform.",
            "argstr": "-usesqform",
        },
    ),
    (
        "verbose",
        int,
        {
            "help_string": "Verbose mode, 0 is least.",
            "argstr": "-verbose {verbose}",
        },
    ),
    (
        "wm_seg",
        str,
        {
            "help_string": "White matter segmentation volume needed by BBR cost function.",
            "argstr": "-wmseg {wm_seg}",
        },
    ),
    (
        "wmcoords",
        str,
        {
            "help_string": "White matter boundary coordinates for BBR cost function.",
            "argstr": "-wmcoords {wmcoords}",
        },
    ),
    (
        "wmnorms",
        str,
        {
            "help_string": "White matter boundary normals for BBR cost function.",
            "argstr": "-wmnorms {wmnorms}",
        },
    )
]

ApplyXFM_input_spec = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))

output_fields = [
    (
        "out_file",
        specs.File,
        {
            "help_string": "Path/name of registered file (if generated).",
            "requires": ["out_file"],
            "output_file_template": "{out_file}",
        },
    ),
    (
        "out_matrix_file",
        specs.File,
        {
            "help_string": "Path/name of calculated affine transform (if generated).",
            "requires": ["out_matrix_file"],
            "output_file_template": "{out_matrix_file}",
        },
    ),
]

ApplyXFM_output_spec = specs.SpecInfo(
    name="Output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class ApplyXFM(ShellCommandTask):
    """
    Example
    -------
    >>> task = ApplyXFM()
    >>> task.inputs.in_file = "structural.nii"
    >>> task.inputs.in_matrix_file = "trans.mat"
    >>> task.inputs.out_file = "newfile.nii"
    >>> task.inputs.reference = "mni.nii"
    >>> task.inputs.apply_xfm = True
    >>> task.cmdline
    'flirt -in structural.nii -ref mni.nii -out newfile.nii -omat structural_flirt.mat -applyxfm -init trans.mat'
    """
    input_spec = ApplyXFM_input_spec
    output_spec = ApplyXFM_output_spec
    executable = "flirt"

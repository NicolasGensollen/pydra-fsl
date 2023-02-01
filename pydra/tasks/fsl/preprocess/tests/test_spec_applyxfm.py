import pytest
from pathlib import Path
from ..applyxfm import ApplyXFM


@pytest.mark.parametrize("inputs, outputs", [({"reference": 'f"{in_file}"'}, ["out_file", "out_matrix_file"])])
def test_ApplyXFM(test_data, inputs, outputs):
    in_file = Path(test_data) / "test.nii.gz"
    if inputs is None:
        inputs = {}
    for key, val in inputs.items():
        try:
            inputs[key] = eval(val)
        except:
            pass
    task = ApplyXFM(in_file=in_file, **inputs)
    assert set(task.generated_output_names) == set(["return_code", "stdout", "stderr"] + outputs)

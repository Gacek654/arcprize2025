import importlib.util
import os
import numpy as np
import numpy.testing as npt

# Dynamically import the module because the filename contains a hyphen.
FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'arc-prize.py')
_spec = importlib.util.spec_from_file_location('arc_prize', FILE_PATH)
_arc_prize = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_arc_prize)

flood_fill_border_zero_to_two = _arc_prize.flood_fill_border_zero_to_two


def test_flood_fill_border_zero_to_two():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    expected = np.array([
        [2, 2, 2, 2, 2],
        [2, 2, 1, 2, 2],
        [2, 1, 1, 1, 2],
        [2, 2, 1, 2, 2],
        [2, 2, 2, 2, 2]
    ])

    result = flood_fill_border_zero_to_two(grid)
    npt.assert_array_equal(result, expected)

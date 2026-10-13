"""
Data path management for HWM14 model data files.
"""

from os import environ, fsencode
from pathlib import Path

DATA_FILES = ("hwm123114.bin", "dwm07b104i.dat", "gd2qd.dat")

# Length of the Fortran buffer that receives HWMPATH (findandopen in hwm14.f90).
_HWMPATH_MAX = 1024


def check_data_path(path: str) -> None:
    """
    Raise FileNotFoundError unless the Fortran code will find every data file in ``path``.

    When the Fortran code can't find a data file it terminates the whole
    interpreter, so this has to be caught before any model call.
    """
    if len(fsencode(path)) > _HWMPATH_MAX:
        raise FileNotFoundError(
            f"HWM14 data path is longer than {_HWMPATH_MAX} bytes, "
            f"so the model can't open its data files: {path}"
        )
    missing = [name for name in DATA_FILES if not (Path(path) / name).is_file()]
    if missing:
        raise FileNotFoundError(
            f"HWM14 data files missing from {path}: {', '.join(missing)}. "
            "The pyhwm2014 installation is incomplete; reinstall it."
        )


# Set HWMPATH to the location of the data files.
HWMPATH: str = str(Path(__file__).parent / "data")
check_data_path(HWMPATH)
environ["HWMPATH"] = HWMPATH

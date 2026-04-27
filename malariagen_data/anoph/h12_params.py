"""Parameter definitions for H12 analysis functions."""

from typing import Optional, Sequence, Union

from typing_extensions import Annotated, TypeAlias

from . import base_params

window_sizes: TypeAlias = Annotated[
    Sequence[int],
    """
    The sizes of windows (number of SNPs) used to calculate statistics within.
    """,
]

window_sizes_default: window_sizes = (100, 200, 500, 1000, 2000, 5000, 10000, 20000)

window_size: TypeAlias = Annotated[
    int,
    """
    The size of windows (number of SNPs) used to calculate statistics within.
    """,
]

multi_window_size: TypeAlias = Annotated[
    Union[window_size, dict[str, int]],
    """
    The size of windows (number of SNPs) used to calculate statistics within. Can
    be a single value, in which case the same window size will be used for all
    cohorts. Can also be a mapping from cohort identifiers to values, in case
    you need to provide different window sizes for different cohorts.
    """,
]

cohort_size_default: Optional[base_params.cohort_size] = None

min_cohort_size_default: base_params.min_cohort_size = 15

max_cohort_size_default: base_params.max_cohort_size = 50

apply_hampel: TypeAlias = Annotated[
    bool,
    """
    If True, apply a Hampel filter to the H12 values to remove isolated
    outliers that are unlikely to represent true selection signals.
    """,
]
apply_hampel_default: apply_hampel = False

hampel_window: TypeAlias = Annotated[
    int,
    """
    The number of neighbouring windows on each side to use when applying
    the Hampel filter.
    """,
]
hampel_window_default: hampel_window = 5

hampel_t: TypeAlias = Annotated[
    float,
    """
    The threshold multiplier for the Hampel filter. Windows whose H12 value
    differs from the local median by more than `hampel_t` scaled MADs are
    replaced by the median.
    """,
]
hampel_t_default: hampel_t = 3.0

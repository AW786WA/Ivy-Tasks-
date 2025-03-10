import ivy
import ivy.functional.frontends.paddle as paddle
from ivy.func_wrapper import (
    with_supported_dtypes,
    with_unsupported_dtypes,
)
from ivy.functional.frontends.paddle.func_wrapper import to_ivy_arrays_and_back
# Defines the `greater_equal` function with dtype support and Ivy array conversion
@with_supported_dtypes(
    {
        "2.5.1 and below": (
            "bool",
            "float16",
            "float32",
            "float64",
            "int32",
            "int64",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
def greater_equal(x, y, name=None):
    return ivy.greater_equal(x, y)
# Example usage
# Sample inputs to demonstrate the expected behavior
# Result returns the truth value of x>=y, an ivy.array
x = ivy.array([1, 2, 3])
y = ivy.array([1, 3, 2])
result = ivy.greater_equal(x, y)
print(result)
# global
import ivy
import ivy.functional.frontends.tensorflow as tf_frontend
import ivy.functional.frontends.paddle as paddle
ivy.set_backend("tensorflow")
from ivy.func_wrapper import (
    with_supported_dtypes,
    with_unsupported_dtypes,
)
from ivy.functional.frontends.paddle.func_wrapper import to_ivy_arrays_and_back

@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def abs(x, name=None):
    return ivy.abs(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def acos(x, name=None):
    return ivy.acos(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def acosh(x, name=None):
    return ivy.acosh(x)


@with_unsupported_dtypes(
    {"2.5.1 and below": ("bool", "unsigned", "int8", "float16", "bfloat16")}, "paddle"
)
@to_ivy_arrays_and_back
def add(x, y, name=None):
    return ivy.add(x, y)


@with_unsupported_dtypes(
    {"2.5.1 and below": ("bool", "unsigned", "int8", "float16", "bfloat16")}, "paddle"
)
@to_ivy_arrays_and_back
def add_(x, y, name=None):
    return ivy.inplace_update(x, add(x, y))


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def addmm(input, x, y, beta=1.0, alpha=1.0, name=None):
    value = alpha * ivy.matmul(x, y) + (beta * input)
    return value


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def amax(x, axis=None, keepdims=False):
    if axis is None:
        return ivy.max(x)
    if isinstance(axis, int):
        axis = [axis]
    for i in range(len(axis)):
        if axis[i] < 0:
            axis[i] += x.ndim
    for i in axis:
        if i < 0 or i >= x.ndim:
            raise ValueError("axis {} is out of range [-{}:{}]".format(i, 0, x.ndim))
    return ivy.max(x, axis=axis, keepdims=keepdims)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def amin(x, axis=None, keepdim=False, name=None):
    return ivy.min(x, axis=axis, keepdims=keepdim)


@with_supported_dtypes(
    {"2.5.1 and below": ("complex64", "complex128", "float32", "float64")},
    "paddle",
)
@to_ivy_arrays_and_back
def angle(x, name=None):
    return ivy.angle(x)


@with_supported_dtypes({"2.5.0 and below": "bool"}, "paddle")
@to_ivy_arrays_and_back
def any(x, axis=None, keepdim=False, name=None):
    return ivy.any(x, axis=axis, keepdims=keepdim)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def asin(x, name=None):
    return ivy.asin(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def asinh(x, name=None):
    return ivy.asinh(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def atan(x, name=None):
    return ivy.atan(x)


@with_unsupported_dtypes({"2.4.2 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def atan2(x, y, name=None):
    return ivy.atan2(x, y)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def atanh(x, name=None):
    return ivy.atanh(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def ceil(x, name=None):
    return ivy.ceil(x)


@with_unsupported_dtypes({"2.4.2 and below": ("int16", "float16")}, "paddle")
@to_ivy_arrays_and_back
def conj(x, name=None):
    return ivy.conj(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def cos(x, name=None):
    return ivy.cos(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def cosh(x, name=None):
    return ivy.cosh(x)


@with_supported_dtypes(
    {"2.5.1 and below": ("int32", "int64", "float16", "float32", "float64", "bool")},
    "paddle",
)
@to_ivy_arrays_and_back
def count_nonzero(x, axis=None, keepdim=False, name=None):
    return ivy.astype(ivy.count_nonzero(x, axis=axis, keepdims=keepdim), ivy.int64)


@with_supported_dtypes(
    {
        "2.5.1 and below": (
            "int32",
            "int64",
            "float32",
            "float64",
            "complex64",
            "complex128",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
def cumprod(x, dim=None, dtype=None, name=None):
    return ivy.cumprod(x, axis=dim, dtype=dtype)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def deg2rad(x, name=None):
    return ivy.deg2rad(x)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def diff(x, n=1, axis=-1, prepend=None, append=None, name=None):
    return ivy.diff(x, n=n, axis=axis, prepend=prepend, append=append)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def digamma(x, name=None):
    digamma_fun = ivy.digamma
    return ivy.array(digamma_fun(x), dtype=x.dtype)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def divide(x, y, name=None):
    return ivy.divide(x, y)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def erf(x, name=None):
    return ivy.erf(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def exp(x, name=None):
    return ivy.exp(x)


@with_supported_dtypes({"2.5.1 and below": ("float16", "float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def expm1(x, name=None):
    return ivy.expm1(x)


@with_supported_dtypes(
    {"2.5.1 and below": ("bfloat16", "float32", "float64")}, "paddle"
)
@to_ivy_arrays_and_back
def floor(x, name=None):
    return ivy.floor(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def floor_divide(x, y, name=None):
    return ivy.floor_divide(x, y)


@with_unsupported_dtypes({"2.5.1 and below": "bfloat16"}, "paddle")
@to_ivy_arrays_and_back
def fmax(x, y, name=None):
    return ivy.fmax(x, y)


@with_unsupported_dtypes({"2.5.1 and below": "bfloat16"}, "paddle")
@to_ivy_arrays_and_back
def fmin(x, y, name=None):
    return ivy.fmin(x, y)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def frac(x, name=None):
    y = ivy.trunc(x)
    return ivy.subtract(x, y)


@with_supported_dtypes({"2.5.1 and below": ("int32", "int64")}, "paddle")
@to_ivy_arrays_and_back
def gcd(x, y, name=None):
    return ivy.gcd(x, y)


@with_supported_dtypes(
    {"2.5.1 and below": ("float16", "float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def heaviside(x, y, name=None):
    return ivy.heaviside(x, y)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def inner(x, y, name=None):
    result = ivy.inner(x, y)
    if (x.shape == () and y.shape == (1,)) or (x.shape == (1,) and y.shape == ()):
        result = result.reshape((1,))
    elif x.shape == (1,) and y.shape == (1,):
        result = result.reshape((1,))
    return result


@with_supported_dtypes(
    {"2.5.1 and below": ("float16", "float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def isfinite(x, name=None):
    return ivy.isfinite(x)


@with_supported_dtypes(
    {"2.5.1 and below": ("float16", "float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def isinf(x, name=None):
    return ivy.isinf(x)


@with_supported_dtypes(
    {"2.5.1 and below": ("float16", "float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def isnan(x, name=None):
    return ivy.isnan(x)


@with_supported_dtypes(
    {"2.5.1 and below": ("float16", "float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def kron(x, y, name=None):
    return ivy.kron(x, y)


@with_supported_dtypes({"2.5.1 and below": ("int32", "int64")}, "paddle")
@to_ivy_arrays_and_back
def lcm(x, y, name=None):
    return ivy.lcm(x, y)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def lerp(x, y, weight, name=None):
    return ivy.lerp(x, y, weight)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def lgamma(x, name=None):
    return ivy.lgamma(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def log(x, name=None):
    return ivy.log(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def log1p(x, name=None):
    return ivy.log1p(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def log2(x, name=None):
    return ivy.log2(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def logit(x, eps=None, name=None):
    return ivy.logit(x, eps=eps)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def max(x, axis=None, keepdim=False, name=None):
    return ivy.max(x, axis=axis, keepdims=keepdim)


# maximum
@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def maximum(x, y, name=None):
    return ivy.maximum(x, y)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def min(x, axis=None, keepdim=False, name=None):
    return ivy.min(x, axis=axis, keepdims=keepdim)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def minimum(x, y, name=None):
    return ivy.minimum(x, y)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def mm(input, mat2, name=None):
    return ivy.matmul(input, mat2)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def multiply(x, y, name=None):
    return ivy.multiply(x, y)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def nanmean(x, axis=None, keepdims=False):
    return ivy.nanmean(x, axis=axis, keepdims=keepdims)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def nansum(x, axis=None, dtype=None, name=None):
    return ivy.nansum(x, axis=axis, dtype=dtype)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int8", "int16", "int32", "int64")},
    "paddle",
)
@to_ivy_arrays_and_back
def neg(x, name=None):
    return ivy.negative(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def outer(x, y, name=None):
    return ivy.outer(x, y)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def pow(x, y, name=None):
    return ivy.pow(x, y)


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def prod(x, axis=None, keepdim=False, dtype=None, name=None):
    return ivy.prod(x, axis=axis, keepdims=keepdim, dtype=dtype)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def rad2deg(x, name=None):
    return ivy.rad2deg(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def reciprocal(x, name=None):
    return ivy.reciprocal(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def remainder(x, y, name=None):
    return ivy.remainder(x, y)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def round(x, name=None):
    return ivy.round(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def rsqrt(x, name=None):
    return 1 / ivy.sqrt(x)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def sgn(x, name=None):
    return ivy.sign(x, np_variant=True)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def sign(x, name=None):
    return ivy.sign(x, np_variant=False)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def sin(x, name=None):
    return ivy.sin(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def sinh(x, name=None):
    return ivy.sinh(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def sqrt(x, name=None):
    return ivy.sqrt(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def square(x, name=None):
    return ivy.square(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def stanh(x, scale_a=0.67, scale_b=1.7159, name=None):
    # TODO this function will be simplified as soon as the ivy.stanh(x,a,b) is added
    exp_ax = ivy.exp(ivy.multiply(scale_a, x))
    exp_minus_ax = ivy.exp(ivy.multiply(-scale_a, x))
    numerator = ivy.subtract(exp_ax, exp_minus_ax)
    denominator = ivy.add(exp_ax, exp_minus_ax)
    ret = ivy.multiply(scale_b, ivy.divide(numerator, denominator))
    return ret


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def subtract(x, y, name=None):
    return ivy.subtract(x, y)


@with_supported_dtypes(
    {
        "2.5.1 and below": (
            "float64",
            "int64",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
def sum(x, axis=None, dtype=None, keepdim=False, name=None):
    return ivy.sum(
        x,
        axis=axis,
        keepdims=keepdim,
        dtype=dtype,
    )


@with_supported_dtypes(
    {"2.5.1 and below": ("float32", "float64", "int32", "int6")}, "paddle"
)
@to_ivy_arrays_and_back
def take(
    x,
    index,
    mode="raise",
    name=None,
):
    if mode not in ["raise", "wrap", "clip"]:
        raise ValueError(
            "'mode' in 'take' should be 'raise', 'wrap', 'clip', but received {}."
            .format(mode)
        )
    x = ivy.reshape(x, (-1,))
    if mode == "clip":
        index = ivy.clip(index, 0, x.shape[-1] - 1)
    elif mode == "wrap":
        index = ivy.where(index < 0, index % x.shape[-1], index)
        index = ivy.where(index >= x.shape[-1], index % x.shape[-1], index)
    return ivy.gather(x, index, axis=0)


@with_unsupported_dtypes({"2.5.1 and below": ("float16", "bfloat16")}, "paddle")
@to_ivy_arrays_and_back
def tan(x, name=None):
    return ivy.tan(x)


@with_supported_dtypes({"2.5.1 and below": ("float32", "float64")}, "paddle")
@to_ivy_arrays_and_back
def tanh(x, name=None):
    return ivy.tanh(x)


@with_supported_dtypes(
    {"2.4.2 and below": ("float32", "float64", "int32", "int64")}, "paddle"
)
@to_ivy_arrays_and_back
def trunc(x, name=None):
    return ivy.trunc(x)

from ivy.core.framework import ivy
from ivy.core.config import RuntimeConfig
from ivy_framework_hooks import to_ivy_arrays_and_back, with_supported_dtypes


# Defines the `diff` function with dtype support and Ivy array conversion
@with_supported_dtypes(
    {
        "2.5.1 and below": (
            "float16",
            "float32",
            "float64",
            "bool",
            "int32",
            "int64",
        )
    },
    "paddle",
)
@to_ivy_arrays_and_back
def diff(x, n=1, axis=-1, prepend=None, append=None, name=None):
    return ivy.diff(x, n=n, axis=axis, prepend=prepend, append=append)

# Example usage:
x = ivy.array([1, 4, 5, 2], dtype='float32')  # Creates a synthetic array
result = diff(x, n=1, axis=-1, prepend=None, append=None)
print(result)

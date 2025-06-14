"""Signal generator module for PhaseLine.

Provides functions to generate standard waveforms:
sine, square, and triangle.
"""

from typing import Tuple

import numpy as np
from numpy.typing import NDArray

TWO_PI = 2 * np.pi


def generate_time_array(
    duration: float = 1.0, sampling_rate: int = 1000
) -> NDArray[np.float64]:
    """Generate a 1D array of time samples.

    Args:

        duration: Duration of the signal in seconds.
        sampling_rate: Number of samples per second.

    Returns:

        A NumPy array of time values.
    """
    return np.linspace(
        start=0, stop=duration, num=int(duration * sampling_rate), endpoint=False
    )


def sine_wave(
    freq: float = 5.0,
    amplitude: float = 1.0,
    duration: float = 1.0,
    sampling_rate: int = 1000,
) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Generate a sine wave signal.

    Args:

        freq: Frequency of the wave in Hz.
        amplitude: Peak amplitude.
        duration: Length of time the signal spans.
        sampling_rate: Number of samples per second.

    Returns:

        Tuple containing time and amplitude arrays.
    """
    t = generate_time_array(duration=duration, sampling_rate=sampling_rate)
    return t, amplitude * np.sin(TWO_PI * freq * t)


def square_wave(
    freq: float = 5.0,
    amplitude: float = 1.0,
    duration: float = 1.0,
    sampling_rate: int = 1000,
) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Generate a square wave signal.

    Args:

        freq: Frequency of the wave in Hz.
        amplitude: Peak amplitude.
        duration: Length of time the signal spans.
        sampling_rate: Number of samples per second.

    Returns:

        Tuple containing time and amplitude arrays.
    """
    t = generate_time_array(duration=duration, sampling_rate=sampling_rate)
    return t, amplitude * np.sign(np.sin(TWO_PI * freq * t))


def triangle_wave(
    freq: float = 5.0,
    amplitude: float = 1.0,
    duration: float = 1.0,
    sampling_rate: int = 1000,
) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Generate a triangle wave signal.

    Args:

        freq: Frequency of the wave in Hz.
        amplitude: Peak amplitude.
        duration: Length of time the signal spans.
        sampling_rate: Number of samples per second.

    Returns:

        Tuple containing time and amplitude arrays.
    """
    t = generate_time_array(duration=duration, sampling_rate=sampling_rate)
    triangle = 2 * np.abs(2 * ((t * freq) % 1) - 1) - 1
    return t, amplitude * triangle

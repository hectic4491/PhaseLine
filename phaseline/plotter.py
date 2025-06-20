"""Plotter module for PhaseLine.

Handles waveform visualization, supporting both:
1. Saving png images generated by matplotlib to 'graphs/' for offline use and testing.
2. Return raw time & amplitude arrays for Flask integration.
"""

import os

import matplotlib.pyplot as plt

from phaseline.signal_generator import sine_wave, square_wave, triangle_wave

# Create 'graphs/' directory if it doesn't exist
GRAPH_DIR = os.path.join(os.path.dirname(__file__), "../graphs")
os.makedirs(GRAPH_DIR, exist_ok=True)


def plot_waveform(waveform, title="Waveform", filename=None):
    """Plot a waveform with Matplotlib.

    Args:
        waveform: Tuple of (time, amplitude) arrays.
        title: Title of the plot.
        filename: If provided, saves the plot instead of returning data.

    Returns:
        dict: {"time": time, "amplitude": amplitude} if Flask integration is needed.
    """
    time, amplitude = waveform

    if filename:
        # Save the plot as an image for offline use
        filepath = os.path.join(GRAPH_DIR, filename)
        plt.figure(figsize=(6, 4))
        plt.plot(time, amplitude)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title(title)
        plt.grid(True)
        plt.savefig(filepath, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Saved plot to: {filepath}")
        return None  # no data returned when making an image

    # Otherwise, return raw data for Flask integration
    return {"time": time.tolist(), "amplitude": amplitude.tolist()}


if __name__ == "__main__":
    plot_waveform(
        waveform=sine_wave(), title="Sine Wave", filename="sine_wave.png"
)
    plot_waveform(
        waveform=square_wave(), title="Square Wave", filename="square_wave.png"
    )
    plot_waveform(
        waveform=triangle_wave(), title="Triangle Wave", filename="triangle_wave.png"
    )

# TODO : add type hints to the function signatures

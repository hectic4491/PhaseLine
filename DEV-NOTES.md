# Development notes for PhaseLine
	---
## 2025-06-13  20:00:00
### Software Requirements for PhaseLine:
#### PhaseLine
> A Python-powered oscilloscope that visualizes, analyzes, and dissects waveforms in real time. It includes both synthetic and live audio input options and offers time-domain and frequency-domain views. Inspired by experience in recording music, mathematical training in PDEs and Fourier analysis, and grounded in professional test automation practices.


#### Core Features
- Real-time waveform visualization of sine, square, triangle, and audio waveforms.
- Live audio input via microphone (...optional stretch goal using sounddevice or pyaudio... we'll see...).
- Time-domain plot and frequency-domain spectrum using FFT.
- Triggering control: zero-crossing detection to mimic actual scope triggering.
- Adjustable sample rate and buffer window.
- pytest test suite for waveform integrity, sampling logic, and FFT accuracy.
- Containerized with Docker for portable deployment and reproducibility.


#### Mathematical Integrations
- Overlay Fourier series approximations and watch partial sums converge in real time.
- Simulate the wave equation (D'Alembert's formula) with pulse inputs to demonstrate propagation.
- Interactive GUI toggle between mathematical modes: “Live Mode”, “Analytical View”, “Fourier Breakdown”.


#### Testing Components with pytest
- Validate waveform accuracy (e.g., sine wave has correct period/amplitude).
- Confirm buffer length and timing align with sample rate.
- Check FFT resolution and spectral peaks for generated tones.
- Mock real-time audio input and verify response curve.
- Use fixtures to simulate various waveform settings.


#### Docker Integration
- Runs in a self-contained container with python, matplotlib, pytest, (...optional GUI backend... ).


#### Documentation
-README with waveform demos, screenshots, and short video demos (GIFs or YouTube).
-Walkthrough of how you used mathematical concepts for spectral analysis and signal decomposition.
-Notes on how this mimics hardware signal testing in embedded systems.

---

## 2025-06-13  21:00:00
### Development Notes - Rob
I structured the project's directory and early config files.
MIT License will be used.
Version control will be tracked with git.
git initiated and .gitignore created.
Remote repo at: git@github.com:hectic4491/PhaseLine.git
venv created; the interpreter, pip and necessary dependencies are local.

create and activate venv:
#### Bash
> python3 -m venv venv
> source venv/bin/activate


Project source code in phaseline/ directory, tests will be implemented in tests/ directory.


requirements.txt gives us the list of runtime necessary project dependencies:
- numpy
- matplotlib
- scipy
#### Bash
> pip install -r requirements.txt


requirements-dev.txt gives us the list of development project dependencies.
- setuptools
- black 
- isort
- pylint
- pytest
 #### Bash
> pip install -r requirements-dev.txt

---

## 2025-06-13  21:30:00
### Development Notes - Rob
signal_generator.py

...Write what I made...
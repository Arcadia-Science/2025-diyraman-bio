# APPLY CALIBRATION
# last updated 2025-01-31

# The DIY Raman system used in this project typically needs daily calibration to minimize the
# peak positional error in the Raman spectra. This script applies the calibration from the
# generate_calibration notebook to the sample spectra.

# Inputs:
# - Sample spectra (CSV) - in the /data/raw/ folder
# - Pixel to nanometer linear equation coefficients (CSV) - neon coefficients file in the
#       /data/processed/calibration folder
# - Raman shift linear equation coefficients (CSV) - acetonitrile coefficients file in the
#       /data/processed/calibration folder

# Outputs:
# - Calibrated and processed sample spectra (CSV)
# - Quick plots of processed data (PNG)

# 1. Imports

import os
from tkinter import Tk, filedialog

import arcadia_pycolor as apc
import matplotlib.pyplot as plt
import pandas as pd
from pybaselines.whittaker import airpls
from scipy.signal import medfilt

apc.mpl.setup()

# 2. Load sample data (select multiple files in same folder), set output folder

root = Tk()
root.withdraw()
sample_files = filedialog.askopenfilenames(title="Select the sample data files")
root.destroy()

sample_folder_path = os.path.dirname(sample_files[0])

date = sample_folder_path[sample_folder_path.rfind("raw/") + 4 :]
output_folder_path = os.path.join(
    sample_folder_path[0 : sample_folder_path.rfind("raw/")],
    "processed/processed_data",
    date,
)

# 3. Load calibration data (you can select the parameters that match the sample data)

root = Tk()
root.withdraw()
neon_coefficients = filedialog.askopenfilename(title="Select the neon calibration file")
acetonitrile_coefficients = filedialog.askopenfilename(
    title="Select the acetonitrile calibration file",
)
root.destroy()

neon_coefficients = pd.read_csv(neon_coefficients)
acetonitrile_coefficients = pd.read_csv(acetonitrile_coefficients)

neon_slope = neon_coefficients["Slope"][0]
neon_intercept = neon_coefficients["Intercept"][0]
acetonitrile_slope = acetonitrile_coefficients["Slope"][0]
acetonitrile_intercept = acetonitrile_coefficients["Intercept"][0]

# 4. Make functions for calibration


def pixel_to_nanometers(pixel):
    return pixel * neon_slope + neon_intercept


def wavelength2shift(wavelength, excitation=532):
    shift = ((1.0 / excitation) - (1.0 / wavelength)) * (10**7)
    return shift


def raman_shift_adjustment(raman_shift):
    return raman_shift * acetonitrile_slope + acetonitrile_intercept


# 5. Apply calibration to sample data

for sample_file in sample_files:
    sample_data = pd.read_csv(sample_file)
    sample_data["Wavelength (nm)"] = pixel_to_nanometers(sample_data["Pixels #"])
    sample_data["Raman shift (cm-1)"] = wavelength2shift(sample_data["Wavelength (nm)"])
    sample_data["Raman shift (cm-1) adjusted"] = raman_shift_adjustment(
        sample_data["Raman shift (cm-1)"],
    )

    sample_data["Filtered Intensity (a.u.)"] = medfilt(sample_data["Intensity (a.u.)"], 5)
    baseline = airpls(
        sample_data["Intensity (a.u.)"],
        lam=1000000,
        diff_order=1,
        max_iter=50,
        tol=0.001,
    )[0]
    sample_data["Baselined Filtered Intensity (a.u.)"] = (
        sample_data["Filtered Intensity (a.u.)"] - baseline
    )
    sample_data.to_csv(os.path.join(output_folder_path, os.path.basename(sample_file)), index=False)

    # 6. Plot processed data

    plt.figure(figsize=(10, 6))
    plt.plot(
        sample_data["Raman shift (cm-1) adjusted"],
        sample_data["Intensity (a.u.)"],
        color="blue",
    )
    plt.xlabel("Raman Shift (cm$^{-1}$)")
    plt.ylabel("Intensity (a.u.)")
    plt.title("Processed Raman Spectrum")
    plt.savefig(
        os.path.join(output_folder_path, os.path.basename(sample_file).replace(".csv", ".png")),
    )
    plt.close()

print("Calibration applied to sample data.")

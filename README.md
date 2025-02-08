# DIY Raman spectroscopy for biological research

[![run with conda](https://img.shields.io/badge/run%20with-conda-3EB049?labelColor=000000&logo=anaconda)](https://docs.conda.io/projects/miniconda/en/latest/)

## Purpose

This repository accompanies the pub, "DIY Raman spectroscopy for biological research." It contains the data acquired and analyzed in this effort, Jupyter notebooks for calibration and figure generation, and a summary of data from the spectral library.

## Installation and Setup

This repository uses conda to manage software environments and installations. You can find operating system-specific instructions for installing miniconda [here](https://docs.conda.io/projects/miniconda/en/latest/). After installing conda and [mamba](https://mamba.readthedocs.io/en/latest/), run the following command to create the pipeline run environment.

```{bash}
TODO: Replace <NAME> with the name of your environment
mamba env create -n <NAME> --file envs/dev.yml
conda activate <NAME>
```

<details><summary>Developer Notes (click to expand/collapse)</summary>

1. Install your pre-commit hooks:

    ```{bash}
    pre-commit install
    ```

    This installs the pre-commit hooks defined in your config (`./.pre-commit-config.yaml`).

2. Export your conda environment before sharing:

    As your project develops, the number of dependencies in your environment may increase. Whenever you install new dependencies (using either `pip install` or `mamba install`), you should update the environment file using the following command.

    ```{bash}
    conda env export --from-history --no-builds > envs/dev.yml
    ```

    `--from-history` only exports packages that were explicitly added by you (e.g., the packages you installed with `pip` or `mamba`) and `--no-builds` removes build specification from the exported packages to increase portability between different platforms.
</details>

## Data

The data shared here is collected on the DIY spontaneous Raman system at Arcadia Science, which is the OpenRaman Starter Edition (532 nm excitation), originally created by Luc B (https://www.open-raman.org/about/). The input files are the raw data in CSV format collected from a range of biological research samples that are in the Arcadia spectral library and calibration standards. The outputs include calibration equations for each acquisition day, calibrated data with additional pre-processing, quick look graphs for each sample's data, and performance metrics for the system. 

## Overview

### Description of the folder structure

* [data/](./data/): Data for each sample presented in the pub. It contains folders for raw data (meaning as acquired on the spectrometer) and processed (meaning calibrated or otherwise modified) These are organized into subfolders for each date. 
* [notebooks/](./notebooks/): Jupyter notebooks for gnenerating calibration correction equations and plotting processed data to generate the figures shown in the pub.
* [scripts/](./scripts/): Python scripts for applying calibration correction to acquired data and generating quick plots. 
* [envs/](./envs): This repository uses conda to manage software installations and versions.
* [figures/](./figures): Base images used for the figures in the pub. The final pub figures are edited in Adobe Illustrator. 
* [spectral_library/](./spectral_library): The spectral library includes peak positions for all samples collected in this pub. 
* [`LICENSE`](./LICENSE): License specifying the re-use terms for the code in this repository.
* [`README.md`](./README.md): File outlining the contents of this repository and how to use them.
* * [.github/](./.github), [.vscode/](./.vscode), [.gitignore](./.gitignore), [.pre-commit-config.yaml](./.pre-commit-config.yaml), [Makefile](./Makefile), [pyproject.toml](./Makefile): Files that control the development environment of the repository.

### Methods

TODO: Include a brief, step-wise overview of analyses performed.

> Example:
>
> 1.  Download scripts using `download.ipynb`.
> 2.  Preprocess using `./preprocessing.sh -a data/`
> 3.  Run Snakemake pipeline `snakemake --snakefile Snakefile`
> 4.  Generate figures using `pub/make_figures.ipynb`.

### Compute Specifications

We executed this project on an Apple MacBook Pro machine running macOS Sonoma version 14.5. The machine has 36 GB memory and an Apple M3 Max chip, though these configurations is not required for running the calibration and analysis. 

## Contributing

See how we recognize [feedback and contributions to our code](https://github.com/Arcadia-Science/arcadia-software-handbook/blob/main/guides-and-standards/guide-credit-for-contributions.md).

---
## For Developers

This section contains information for developers who are working off of this template. Please adjust or edit this section as appropriate when you're ready to share your repo.

### GitHub templates
This template uses GitHub templates to provide checklists when making new pull requests. These templates are stored in the [.github/](./.github/) directory.

### VSCode
This template includes recommendations to VSCode users for extensions, particularly the `ruff` linter. These recommendations are stored in `.vscode/extensions.json`. When you open the repository in VSCode, you should see a prompt to install the recommended extensions.

### `.gitignore`
This template uses a `.gitignore` file to prevent certain files from being committed to the repository.

### `pyproject.toml`
`pyproject.toml` is a configuration file to specify your project's metadata and to set the behavior of other tools such as linters, type checkers etc. You can learn more [here](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

### Linting
This template automates linting and formatting using GitHub Actions and the `ruff` linter. When you push changes to your repository, GitHub will automatically run the linter and report any errors, blocking merges until they are resolved.

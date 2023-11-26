# Python Manager

This repository outlines scripts and configurations for managing multiple Python environments. It facilitates easy switching between two Python versions, referred to as `p0` and `p2`.

## Setup

### Bash Configuration

To set up the aliases in Bash for environment switching, add these lines to your `.bashrc` or `.bash_profile`:

```bash
alias p0='/path/to/python310/python -m pip'
alias p2='/path/to/python312/python -m pip'
alias p0i='/path/to/python310/python -m pip install'
alias p2i='/path/to/python312/python -m pip install'
```

Replace `/path/to/python310` and `/path/to/python312` with the actual paths to your Python installations.

### PowerShell Configuration

For PowerShell users, add this function to your PowerShell profile script:

```powershell
function Set-Pip {
    param (
        [string]$version
    )
    if ($version -eq "p0") {
        $Global:PIP_COMMAND = "/path/to/python310/python -m pip"
    } elseif ($version -eq "p2") {
        $Global:PIP_COMMAND = "/path/to/python312/python -m pip"
    } else {
        Write-Host "Version not recognized."
    }
}

function pip {
    & $Global:PIP_COMMAND $args
}
```

Again, replace `/path/to/python310` and `/path/to/python312` with your specific Python paths.

## Usage

### In Bash
- Switch environments using `p0` for Python 310 and `p2` for Python 312.
- Directly install packages using `p0i package_name` for Python 310 and `p2i package_name` for Python 312.

### In PowerShell
- Set the environment with `Set-Pip p0` for Python 310 or `Set-Pip p2` for Python 312.
- Then use `pip install package_name` for package installations.

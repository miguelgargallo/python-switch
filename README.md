# Python Manager

This repository outlines scripts and configurations for managing multiple Python environments. It facilitates easy switching between two Python versions, referred to as `p0` and `p2`.

## Setup

### Bash Configuration

To set up the aliases in Bash for environment switching, add these lines to your `.bashrc` or `.bash_profile`:

```bash
alias p0='/path/to/python310/python'
alias p2='/path/to/python312/python'
alias p0m='/path/to/python310/python -m pip'
alias p2m='/path/to/python312/python -m pip'
alias p0i='/path/to/python310/python -m pip install'
alias p2i='/path/to/python312/python -m pip install'
```

Replace `/path/to/python310` and `/path/to/python312` with the actual paths to your Python installations.

### PowerShell Configuration

For PowerShell users, include this function in your PowerShell profile script (typically located at `$HOME\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`):

```powershell
function Set-PythonEnvironment {
    param (
        [string]$version
    )
    if ($version -eq "p0") {
        $Global:PYTHON_COMMAND = "/path/to/python310/python"
    } elseif ($version -eq "p2") {
        $Global:PYTHON_COMMAND = "/path/to/python312/python"
    } else {
        Write-Host "Version not recognized."
    }

    $Global:PIP_COMMAND = "$Global:PYTHON_COMMAND -m pip"
}

function python {
    & $Global:PYTHON_COMMAND $args
}

function pip {
    & $Global:PIP_COMMAND $args
}
```

Replace `/path/to/python310` and `/path/to/python312` with your specific Python paths.

## Usage

### In Bash
- Switch environments using `p0` for Python 310 and `p2` for Python 312.
- Directly install packages using `p0i package_name` for Python 310 and `p2i package_name` for Python 312.

### In PowerShell
- Set the environment using `Set-PythonEnvironment p0` for Python 310 or `Set-PythonEnvironment p2` for Python 312.
- Run Python scripts with `python script_name.py`.
- Manage Python packages with `pip install package_name`.

![image](https://github.com/miguelgargallo/pythonmanager/assets/5947268/df70f2ed-bcee-4661-9ba3-87f951fff391)


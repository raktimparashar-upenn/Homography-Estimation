# HW1

## Prepare the env

We use `anaconda` (`miniconda`) to manage the python environment. Please install it before you start.

Below is a command to create a virtual environment.
```shell
conda create -n cis580_22_fall  python=3.8
```

To use this env in the current terminal 

```shell
source activate cis580_22_fall
```

Note, when working in IDE, you should select the interpreter to be this virtue environment. For example, in VSCode (after you install the python development plugins), you can press `F1` and type `select interpreter` to select the virtue environment.

Install the required pkgs:

```shell
pip install -r requirements.txt
```

Note, we already provide the VSCode debugging config in the `.vscode` folder, you can select the `Run HW1` and press `F5` to start debugging. (to select a debug configuration, press `F1` and type `Debug: select and start debugging`, once selected this config, you can directly press `F5` in the future to use the same config)

# TODO

Search `STUDENT CODE START` in the project and complete the code slots.
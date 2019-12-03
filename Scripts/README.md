# ipynb_to_rst

Aim: Develop a Python tool, which converts ipynb files to rst files.

## 1 The files in the folder `tests` are our original jupyter notebooks.

1. The file `information_consumption_smoothing-v3.ipynb` == `info.ipynb`

2. The file `Inventory_sales_smoothing-v6.ipynb` == `inv.ipynb`

## 2 The file `ipynb_to_rst.py` is the version 0.03 of our Python script.

1. It enables us to produce a .rst file from a .ipnyb file

2. In order to achieve that, after saving this .py file into your directory, you can type the following code in your terminal

`python ipynb_2_rst.py [filename.ipynb] -o [filename.rst]`

In our testing examples, we have

`python ipynb_2_rst.py info.ipynb -o infox.rst`

and 

`python ipynb_2_rst.py inv.ipynb -o invx.rst`

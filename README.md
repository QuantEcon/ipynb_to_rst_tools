# ipynb_to_rst_tools
Tools, scripts and instructions for converting Jupyter notebooks to RST files

## Instructions from Brandon and Tom


### Conversion method for pandoc

To  load on Manjaro Dell

1. Must have pandoc 2.6 or newer

   to get it 

      * yay pandoc -bin 

      * on ubuntu via package manager or via debian

   check version via

   ```pandoc --version [in a terminal]```

   (If you see a lower numbered version of pandoc, do ) 

   ```conda deactivate```  (in a terminal)


To get things to work in a terminal -- in the directory where the *.ipynb is

1.  This step is necessary only if you want to strip out the bad $ \alpha $ stuff

    In a bash terminal issue command

    ```python latex_space_strip.py  [myinputfile.ipynb] -o [myoutputfile.ipynb]```

2.  issue this command in a bash terminal

    pandoc [myfilenamenew.pynb] -f ipynb+tex_math_dollars -t rst -s -o [newfilename.rst]

    for example -- this worked on Feb 22, 2019 in Singapore

    ```pandoc test23.ipynb -f ipynb+tex_math_dollars -t rst -s -o test23.rst```

     

    





  
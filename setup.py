from cx_Freeze import setup, Executable

setup(name="higlightPDF",
      version="0.1",
      description="",
      executables=[Executable("higlightPDF.py")])

# cx_Freeze does not support building a single file exe, where all of the libraries for your application are embedded in one executable file.

# You can use IExpress to compress the build directory from cx_Freeze into a self-extracting archive: an exe which unpacks your application into a temporary directory and runs it. IExpress is a utility that’s included with Windows, intended for making installers, but it works equally well if you tell it to run the cx_Freeze-built exe after extraction.

# Alternatively, you can create a self extracting archive using 7zip. This is a bit more complex than using IExpress, but might provide more flexibility, and allows you to build your application using only open source tools.

# compile with "python .\setup.py build"

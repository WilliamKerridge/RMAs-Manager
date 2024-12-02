from setuptools import setup, find_packages

setup(
    name="rma_manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt6==6.6.1",
        "pandas==2.1.4",
        "openpyxl==3.1.2",
        "pywin32==306; sys_platform == 'win32'",
        "matplotlib==3.8.2",
        "pillow==10.1.0",
        "pyinstaller==6.3.0",
        "PyMuPDF==1.23.8",
        "python-dotenv==1.0.0",
        "bcrypt==4.1.2",
    ],
    python_requires=">=3.8",
)
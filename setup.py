from setuptools import setup

setup(
    name="ffmpeg-wrapper",
    version="1.0.0",
    py_modules=['wrapper'],
    entry_points={
        "console_scripts": [
            "fw = wrapper:run_wrapper",
        ],
    }
)
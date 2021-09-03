from setuptools import setup

setup(
    name="apivideo_cli",
    version="1.0",
    packages=["av_cli"],
    include_package_data=True,
    install_requires=["click", "api.video"],
    entry_points="""
        [console_scripts]
        avcli=av_cli.av_cli:cli
    """,
)

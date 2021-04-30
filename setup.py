"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem-team@api.video
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "api.video"
VERSION = "0.0.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "python_dateutil >= 2.5.3",
  "setuptools >= 21.0.0",
  "urllib3 >= 1.25.3"
]

setup(
    name=NAME,
    version=VERSION,
    description="api.video Python API client",
    author="api.video ecosystem team",
    author_email="ecosystem-team@api.video",
    url="https://github.com/apivideo/python-api-client",
    keywords=["api.video", "sdk", "api client", "video", "live", "hls"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    Full documentation can be found in the project repository: https://github.com/apivideo/python-api-client
    """
)

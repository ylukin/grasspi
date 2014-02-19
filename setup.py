from setuptools import setup

setup(name='grasspi',
      version='0.1',
      description='A smart irrigation controller for the RaspberryPi',
      url='https://github.com/ylukin/grasspi',
      author='ylukin',
      author_email='ylukin@users.noreply.github.com',
      license='MIT',
      packages=['grasspi'],
      install_requires=[
          'config',
	  'pyserial',
	  'smbus-cffi',
      ],
      include_package_data=True,
      zip_safe=False)

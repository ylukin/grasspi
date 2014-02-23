from setuptools import setup

setup(name='grasspi',
      version='0.1',
      description='A smart irrigation controller for the RaspberryPi',
      url='https://github.com/ylukin/grasspi',
      author='ylukin',
      author_email='ylukin@users.noreply.github.com',
      license='MIT',
      packages=['grasspi', 'grasspi.wmr928', 'grasspi.wunderground'],
      install_requires=[
          'config',
	  'pyserial',
	  'smbus-cffi',
      ],
      scripts=['bin/grasspi_cli.py', 'bin/grasspi_initial_config.py'],
      include_package_data=True,
      data_files=[('/etc/grasspi',['cfg/config.cfg'])],
      zip_safe=False)

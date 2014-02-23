grasspi
=======

Installation
------------

To install, download latest package from https://github.com/ylukin/grasspi/tree/master/packages, then::

    tar zxvf grasspi-x.x.tar.gz
    cd grasspi-x.x
    python setup.py install

This will 
* install a Python module "grasspi" into your site-packages that can be imported into your project
* install other packages needed by grasspi (config, pyserial, etc..), see setup.py for complete list
* install a cli module "grasspi_cli.py" into your PYTHONPATH to execute the main program  

Configuration
-------------

You need to add a config file in /etc/grasspi/config.cfg

Uninstall
-------------

To remove grasspi, you can use pip::

    pip uninstall grasspi

	

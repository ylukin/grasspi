grasspi
=======

Installation
------------

To install, download latest package from https://github.com/ylukin/grasspi/tree/master/packages, then::

    tar zxvf grasspi-x.x.tar.gz
    cd grasspi-x.x
    sudo python setup.py install

This will 
* install a Python module "grasspi" into your site-packages that can be imported into your project
* install other packages needed by grasspi (config, pyserial, etc..), see setup.py for complete list
* install a CLI module "grasspi_cli.py" into your PATH to execute the main program  

Configuration
-------------

You need to add a config file in /etc/grasspi/config.cfg

If using the included CLI module grasspi_cli.py, add the following to your crontab::

    0/5 * * * * root /usr/local/bin/grasspi_cli.py

Uninstall
-------------

To remove grasspi, you can use pip::

    sudo pip uninstall grasspi
    sudo rm /usr/local/bin/grasspi_cli.py

	

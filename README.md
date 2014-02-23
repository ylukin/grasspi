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
* install a CLI module "grasspi_initial_config.py" into your PATH to setup initial environment
* create /etc/grasspi and copy initial config.cfg into it

Configuration
-------------

You need to run "grasspi_initial_config.py" before running the main program.

Add the following to your crontab to run the main program periodically::

    0/5 * * * * root /usr/local/bin/grasspi_cli.py

Uninstall
-------------

To remove grasspi, you can use pip::

    sudo pip uninstall grasspi
    sudo rm /usr/local/bin/grasspi_cli.py
    sudo rm -rf /etc/grasspi

	

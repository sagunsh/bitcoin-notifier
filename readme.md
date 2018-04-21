# Bitcoin Notifier

A desktop notifier that notifies bitcoin price in USD ($).

## Getting Started

Clone the repository

    $ git clone https://github.com/sagunsh/bitcoin-notifier.git
    $ cd bitcoin-notifier

## Prerequisites

You will need to have `Python 3` installed in your device to run the code. You can get one [here](https://www.python.org/downloads/).

### Libraries
* notify2 : to implement the desktop notifier
* requests : to get the latest bitcoin price

You don't have to worry about installing these libraries as I have created a `requirements.txt` file. Here's the command to install these dependencies:

    $ pip install -r requirements.txt

It is often the case that you might have both Python 2 and 3 installed so `pip` is reserved by Python 2. In that case, run this command for Python 3:

    $ pip3 install -r requirements.txt

You may need help from `sudo` during the installation.

Another way and probably the better way to install these dependencies is using `virtualenv`. Check out [this article](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to know more about virtualenvs and how to use them.

## Running the code

    $ python main.py
    or
    $ python3 main.py
    
You will see a notification on the top-right corner of your screen. It will appear for around 10 seconds and will be show pop every 1 minute. You can change the parameters.
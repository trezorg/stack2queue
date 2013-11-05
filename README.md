stack2queue
==================

Queue by 2 stack on python

Install
-------

Install by cloning from the GitHub repo:

    $ git clone git://github.com/trezorg/stack2queue.git
    $ cd stack2queue
    $ python setup.py test
    $ python setup.py build
    $ python setup.py install


Example
-------

    from stack2queue.queue import StackQueue

    queue = StackQueue(1, 2, 3)
    queue.isEmpty()
    queue.size()
    queue.dequeue()
    queue.enqueue(1)
    queue.enqueue(1, 2, 3)
    queue.get()

SL challenge
============

* Challenge source : https://github.com/sortlist/jobs

Misc doc :
* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet


Plan :
* Create PostgresSQL local instance and py config file
* Py Bottle
    * Architecture
    * Design Test(s)
        * https://docs.python.org/3/library/unittest.html
        * http://docs.python-guide.org/en/latest/writing/tests/
* Angular JS architecture
    * Architecture
    * Design Test(s)
        * https://jasmine.github.io/1.3/introduction.html
        * view-source:file:///Users/ludovicgustin/Downloads/jasmine-standalone-2.8.0/SpecRunner.html
        * https://docs.angularjs.org/guide/unit-testing
* Dev phase
* Documentation to run

SUB-TASKS :
* TODO : ~~refresh angular list when adding a new agency (no refresh)~~
* TODO : ~~bower material dependencies~~
* TODO : ~~error/success messages~~
* TODO : responsive behaviour
* TODO : testing
* (TODO) : custom style into proper CSS
* (TODO) : refactor agency-list and creator into isolated angular components



### INSTALLATION
1. Install python 2.7.X https://www.python.org/
2. Install bower https://bower.io/
3. `bower install` from root dir to load js libs
4. Postgres SQL :
    * Create an instance of postgres DB https://www.postgresql.org/
    * Edit `python SLConfig.py` to map your instance
    * `python SLModels.py` to create schema
5. Run the server `python SLServer.py`
6. Enjoy from http://localhost:8080
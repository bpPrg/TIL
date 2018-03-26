# Date: March 18, 2018

# To highlight the words ERROR and FAIL in the error log
pip3 install colout
pip install colout

Then,
If we find the word ERRROR or FAIL at the end of line, the whole line will be
highlighted.

cat a.log 2>&1 | colout '(.*ERROR$)|(.*FAIL$)|(\(.*\))' red,yellow,black bold

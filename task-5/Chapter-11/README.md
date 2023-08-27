1. assert spam >= 10, 'The spam variable is less than 10.'

2. Either assert eggs.lower() != bacon.lower() 'The eggs and bacon variables are the same!' or assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'

3. assert False, 'This assertion always triggers.'

4. To be able to call logging.debug(), you must have these two lines at the start of your program:

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
%(levelname)s -  %(message)s')

5. To be able to send logging messages to a file named programLog.txt with logging.debug(), you must have these two lines at the start of your program:

import logging
>>> logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
format=' %(asctime)s -  %(levelname)s -  %(message)s')

6. DEBUG, INFO, WARNING, ERROR, and CRITICAL

7. logging.disable(logging.CRITICAL)

8. You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages. You can create logging messages. Logging messages provides a timestamp.

9. The Step In button will move the debugger into a function call. The Step Over button will quickly execute the function call without stepping into it. The Step Out button will quickly execute the rest of the code until it steps out of the function it currently is in.

10. After you click Continue, the debugger will stop when it has reached the end of the program or a line with a breakpoint.

11. A breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line.

12. To set a breakpoint in Mu, click the line number to make a red dot appear next to it.

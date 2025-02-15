**Debugging**

Three kinds of errors can occur in a program: syntax errors, runtime errors,
and semantic errors. It is useful to distinguish between them in order to
track them down more quickly.

**Syntax error**: “Syntax” refers to the structure of a program and the rules
about that structure. If there is a syntax error anywhere in your program,
Python does not run the program. It displays an error message
immediately.

**Runtime error**: If there are no syntax errors in your program, it can start
running. But if something goes wrong, Python displays an error message
and stops. This type of error is called a runtime error. It is also called an
exception because it indicates that something exceptional has happened.

**Semantic error**: The third type of error is “semantic”, which means
related to meaning. If there is a semantic error in your program, it runs
without generating error messages, but it does not do what you intended.
Identifying semantic errors can be tricky because it requires you to work
backward by looking at the output of the program and trying to figure
out what it is doing.

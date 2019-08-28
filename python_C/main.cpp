#include <stdio.h>
#include "Python.h"

int main(void) {
  printf("Hello C++\n");
  
  Py_Initialize();

  if (Py_IsInitialized()) {
	PyRun_SimpleString("print (\'Hello Python\'\n)");
	Py_Finalize();
  }else
	printf("Python Not Intialized \n");
  return 0;
}

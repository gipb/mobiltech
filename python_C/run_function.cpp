#include <Python.h>

int
main(int argc, char *argv[])
{
  PyObject *pName, *pModule, *pFunc;
  PyObject *pArgs, *pValue;
  int i;
  wchar_t** argvs = (wchar_t**)calloc(1, sizeof(wchar_t*)*(argc-1));
  for (i=0; i<argc-1; ++i){
	wchar_t* _arg = Py_DecodeLocale(argv[i+1], NULL);
	argvs[i] = _arg;
  }
  
  Py_Initialize();
  pName = PyUnicode_FromString(argv[1]);
  /* Error checking of pName left out */

  pModule = PyImport_Import(pName);
  Py_DECREF(pName);
  
  if (pModule != NULL) {
	pFunc = PyObject_GetAttrString(pModule, argv[2]);
	/* pFunc is a new reference */
	
	if (pFunc && PyCallable_Check(pFunc)) {
	  pArgs = PyTuple_New(argc-3);
	  Py_Main(argc-1,argvs);
	  for (i = 0; i < argc - 3; ++i) {
		pValue = PyUnicode_FromString(argv[i+3]);
		if (!pValue) {
		  Py_DECREF(pArgs);
		  Py_DECREF(pModule);
		  fprintf(stderr, "Cannot convert argument\n");
		  return 1;
		}

		PyTuple_SetItem(pArgs, i, pValue);
	  }
	  pValue = PyObject_CallObject(pFunc, pArgs);
	  Py_DECREF(pArgs);
	  if (pValue != NULL) {
		printf("Result of call : %ld\n", PyLong_AsLong(pValue));
		Py_DECREF(pValue);
	  }
	  else {
		Py_DECREF(pFunc);
		Py_DECREF(pModule);
		PyErr_Print();
		fprintf(stderr, "Call failed\n");
		return 1;
	  }
	}
	else {
	  if (PyErr_Occurred())
		PyErr_Print();
	  fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);
	}
	Py_XDECREF(pFunc);
	Py_DECREF(pModule);
  }
  else {
	PyErr_Print();
	fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);
	return 1;
  }
  /*if (Py_FinalizeEx() < 0) {
	return 120;
  }*/
  Py_Finalize();
  free(argvs);
  return 0;
}

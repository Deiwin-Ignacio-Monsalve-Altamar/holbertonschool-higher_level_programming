#include <Python.h>
#include <object.h>

/**
 * print_python_list_info - print list
 * @p: PyObject
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{

	long int len;
	long int i = 0;
	PyObject *item;

	len = PyList_Size(p);
	PyListObject *aux = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", aux->allocated);

	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		if (PyFloat_Check(item))
			printf("Element %d: float\n", i);
		if (PyTuple_Check(item))
			printf("Element %d: tuple\n", i);
		if (PyList_Check(item))
			printf("Element %d: list\n", i);
		if (PyLong_Check(item))
			printf("Element %d: int\n", i);
		if (PyUnicode_Check(item))
			printf("Element %d: str\n", i);
	}
}

#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - Determine if is polindrome
 * @p: list
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	unsigned long aux = 0, length;
	PyObject *item;

	PyListObject *aux_object = (PyListObject *)p;

	length = PyList_Size(p);
	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", aux_object->allocated);

	for ( ; aux < length; aux++)
	{
		item = PyList_GetItem(p, aux);
		printf("Element %li: %s\n", aux, Py_TYPE(item)->tp_name);
	}
}

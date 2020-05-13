# MatrixCalculator
Никитина Полина, Б05-921

Калькулятор для матриц, умеющий находить сумму, разность и поэлементное произведение двух матриц.

Команды доступные клиенту:

	 add_matrix - post-запрос, позволяющих передать серверу размеры двух матриц, а также сами матрицы.
				  Ввод: клиент вводит сначала размеры первой матрицы (количество строк и столбцов) и саму матрицу, сохраняя её вид, а затем вторую матрицу аналогичным образом.
				  Пример для одной матрицы:
				  >Please, enter number of rows:
				  >2
				  >Please, enter number of columns:
				  >2
				  >Please, enter first matrix:
				  >2 3
				  >3 1
				  >(Ctrl+D)

	     amount - get-запрос, позволяющий получить сумму последних введенных матриц.

	 difference - get-запрос, позволяющий получить разность последних введенных матриц.

    composition - get-запрос, позволяющий получить поэлементное произведение последних введенных матриц.

	       exit - команда для завершения программы.
	    		  Пример:
	    		  >Are you sure you want to leave (Y/N)?
	    		  >Y
	    		  >Goodbye!

Все get-запросы при вводе несовметимых матриц выводят сообщение об этом.


# include <math.h>
# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <assert.h>
# include <limits.h>
# include <stdbool.h>


int* getMilitaryStrength (int A_size_row, int A_size_cols, int* A, int* result_size)
{

}

int main()
{
int res_size;
int * res;

int _A_rows = 0;
int _A_cols = 0;
scanf("%d", & _A_rows);
scanf("%d", & _A_cols);

int ** _A = (int **)
malloc(_A_rows * sizeof(int *));
int _A_init_i = 0;
for (_A_init_i = 0; _A_init_i < _A_rows; ++_A_init_i)
{
    _A[_A_init_i] = (int *)
malloc(_A_cols * (sizeof(int)));
}

int
_A_i, _A_j;
for (_A_i = 0;
_A_i < _A_rows;
_A_i + +) {
for (_A_j = 0; _A_j < _A_cols; _A_j++) {
int _A_item;
scanf("%d", & _A_item);

_A[_A_i][_A_j] = _A_item;
}
}

res = getMilitaryStrength(_A_rows, _A_cols, _A, & res_size);
for (res_i=0; res_i < res_size; res_i++) {

printf("%d\n", res[res_i]);

}

return 0;

}
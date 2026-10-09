#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
#include<mlfw_matrix.h>
#include<mlfw_vector.h>
#include<mlfw_operations.h>

int main()
{
int age;
char sex;
double bmi;
int children;
bool smoker;
double charges;
char tmp[100];
char m;
int regionNumber;

mlfw_mat_double * min_max_matrix;
dimension_t min_max_matrix_rows,min_max_matrix_columns;
double min;
double max;
index_t r,c;
double scaled_value,value;

mlfw_row_vec_double *featured_vector;
mlfw_column_vec_double *parameter_vector_scaled;
mlfw_column_vec_double *parameter_vector;
mlfw_column_vec_double *predicted_value_vector;
FILE *file;
printf("--------------------------------------------------------\n");
printf("---------------Hospital Charges Predictor---------------\n");
printf("--------------------------------------------------------\n");

min_max_matrix=mlfw_mat_double_from_csv("insurance_min_max.csv");
if(min_max_matrix==NULL)
{
printf("Unable to unscaled data\n");
return 0;
}
mlfw_mat_double_get_dimension(min_max_matrix,&min_max_matrix_rows,&min_max_matrix_columns);

//mlfw_mat_double_destroy(min_max_matrix);

file=fopen("model.csv","r");
if(file==NULL)
{
printf("model.csv does not exists\n");
return 0;
}
//age,sex,bmi,children,smoker,region,charges

printf("Enter age (0-150): ");
scanf("%d",&age);
if(age<=0 || age>150) 
{
printf("Wrong age range\n");
return 0; 
}
__fpurge(stdin);

printf("Enter sex(M/F): ");
m=getchar();
if(m=='M' || m=='m') sex='M';
else sex='F';
__fpurge(stdin);

printf("Enter BMI: ");
scanf("%lf",&bmi);
if(bmi<=0)
{
printf("Wrong BMI: %lf\n",bmi);
return 0;
}
__fpurge(stdin);

printf("Enter children count: ");
scanf("%d",&children);
__fpurge(stdin);

printf("Is smoker?(Y/N): ");
m=getchar();
if(m=='Y' || m=='y') smoker=true;
else smoker=false;
__fpurge(stdin);

printf("Region (southwest/southeast/northwest/northeast): ");
scanf("%s",tmp);
if(strcmp(tmp,"southwest")==0) regionNumber=1;
else if(strcmp(tmp,"southeast")==0) regionNumber=2;
else if(strcmp(tmp,"northwest")==0) regionNumber=3;
else if(strcmp(tmp,"northeast")==0) regionNumber=4;
else 
{
printf("Wrong region selected\n");
return 0;
}
featured_vector=mlfw_row_vec_double_create_new(12);
if(featured_vector==NULL)
{
printf("Low on memory\n");
return 0;
}
//age,sex,bmi,children,smoker,region,charges

mlfw_row_vec_double_set(featured_vector,0,1.0);
mlfw_row_vec_double_set(featured_vector,1,(double)age);
mlfw_row_vec_double_set(featured_vector,2,sex=='M'?1:0);
mlfw_row_vec_double_set(featured_vector,3,sex=='F'?1:0);
mlfw_row_vec_double_set(featured_vector,4,bmi);
mlfw_row_vec_double_set(featured_vector,5,(double)children);
mlfw_row_vec_double_set(featured_vector,6,smoker==true?1:0);
mlfw_row_vec_double_set(featured_vector,7,smoker==false?1:0);
mlfw_row_vec_double_set(featured_vector,8,regionNumber==1?1:0);
mlfw_row_vec_double_set(featured_vector,9,regionNumber==2?1:0);
mlfw_row_vec_double_set(featured_vector,10,regionNumber==3?1:0);
mlfw_row_vec_double_set(featured_vector,11,regionNumber==4?1:0);

parameter_vector_scaled=mlfw_column_vec_double_from_csv("model.csv");
if(parameter_vector_scaled==NULL)
{
printf("Low on memory\n");
mlfw_row_vec_double_destroy(featured_vector);
return 0;
}
parameter_vector=mlfw_column_vec_double_create_new(12);
if(parameter_vector==NULL)
{
printf("Low in memory\n");
mlfw_row_vec_double_destroy(featured_vector);
mlfw_column_vec_double_destroy(parameter_vector_scaled);
return 0;
}

for(c=1;c<12;c++)		//Last 2 columns to update
{
min=mlfw_mat_double_get(min_max_matrix,0,c-1);
max=mlfw_mat_double_get(min_max_matrix,1,c-1);
scaled_value=mlfw_column_vec_double_get(parameter_vector_scaled,c);
value=((scaled_value*(max-min))+min);
mlfw_column_vec_double_set(parameter_vector,c,value);
}

predicted_value_vector=mlfw_multiply_double_row_vector_with_column_vector(featured_vector,parameter_vector);
if(predicted_value_vector==NULL)
{
printf("Low on memory\n");
mlfw_row_vec_double_destroy(featured_vector);
mlfw_column_vec_double_destroy(parameter_vector);
return 0;
}
charges=mlfw_column_vec_double_get(predicted_value_vector,0);

mlfw_row_vec_double_destroy(featured_vector);
mlfw_column_vec_double_destroy(parameter_vector);
mlfw_column_vec_double_destroy(predicted_value_vector);
mlfw_column_vec_double_destroy(parameter_vector_scaled);
printf("Predicted Charges in USD: %10.2lf\n",charges);
return 0;
}

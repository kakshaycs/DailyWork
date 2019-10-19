#include<stdio.h>



void makeSet(int *Set , int size)
{
	for(int i=0; i< size; i++)
		Set[i]=i;
}



int findSet(int *Set, int size, int x)
{
  if(!(x>=0 && x < size))
  	return -1;
  if (Set[x]==x)
  	return x;
  else return (Set[x] = findSet(Set,size,Set[x]));
}



void Union(int *Set, int size, int root1, int root2)
{
   if(findSet(Set,size,root1)==findSet(Set,size,root2))
   	return ;
   if(!(root1 >= 0 && root1 < size && root2 >= 0 && root2 < size))
   	return ;

   Set[root1]=root2;

}


// fast Union method 
// in general approch m union cost O(n*m)
//Union by Size,Union by height

void makeSet2(int *Set, int size)
{
	for(int i=size-1; i>=0; i--)
		Set[i]=-1;
}

int findSet2(int *Set, int size,int x)
{
	if(!(x>=0 && x<size))
		return -1;
	if(Set[x]==-1)
		return x;
	else return (Set[x]=findSet2(Set,size,Set[x]));
}

void UnionbySize(int *Set, int size, int root1, int root2)
{
  if((findSet2(Set,size,root1)==findSet2(Set,size,root2))&& findSet2(Set,size,root1!=-1))
  	return;
  if(Set[root2]<Set[root1])
  {
  	Set[root1]=root2;
  	Set[root2]+=Set[root1];
  }
  else
  {
  	Set[root2]=root1;
  	Set[root1]+=Set[root2];
  }

}

void UnionbyRank(int *Set, int size, int root1, int root2)
{
  if ((findSet2(Set,size,root1)==findSet2(Set,size,root2))&& findSet2(Set,size,root1!=-1))
  	return;
  if (Set[root2]<Set[root1])
  	Set[root1]=root2;
  else
  {
  	if (Set[root2] == S[root1])
  	{
  		S[root1]--;
  		S[root2]=root1;
  	}
  }
	
}

int main()
{

 int n=100;
 int Set[n];
 makeSet(Set , n);
 for(int i=0;i<10;i++)
 	printf("%d  ",Set[i] );



}
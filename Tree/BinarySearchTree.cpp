#include<bits/stdc++.h>
#include <stdio.h> 
#include <iostream>

using namespace std;

struct Node
{
	int value;
	struct Node* left;
	struct Node* right;
};

struct Node* newNode(int key)
{
	struct Node* temp = (struct Node*) malloc(sizeof(struct Node));
	temp->left=NULL;
	temp->right=NULL;
	temp->value = key;
	return temp;
}

struct Node * minValueNode(struct Node* node) 
{ 
    struct Node* current = node; 
  
    /* loop down to find the leftmost leaf */
    while (current && current->left != NULL) 
        current = current->left; 
  
    return current; 
} 


struct Node* deleteNode(struct Node* root, int key) 
{
    if (root == NULL) return root; 
	 
    if (key < root->value) 
        root->left = deleteNode(root->left, key); 

    else if (key > root->value) 
        root->right = deleteNode(root->right, key); 
  
    else
    { 
        if (root->left == NULL) 
        { 
            struct Node *temp = root->right; 
            free(root); 
            return temp; 
        } 
        else if (root->right == NULL) 
        { 
            struct Node *temp = root->left; 
            free(root); 
            return temp; 
        } 
  
        struct Node* temp = minValueNode(root->right); 
        root->value = temp->value; 
        root->right = deleteNode(root->right, temp->value); 
    } 
    return root; 
} 



struct Node* insert(struct Node* root ,int key)
{
	 if (root == NULL)
	 	return newNode(key);
	 else if (root->value > key)
	       root->left = insert(root->left, key);	
	else
	    root->right = insert(root->right, key);
	return root;   
}

void postOrder(struct Node* root)
{
	if (root !=NULL)
	{
		postOrder(root->left);
		postOrder(root->right);
		cout<<root->value<<" ";
	}
}

void inOrder(struct Node* root)
{
	if (root!=NULL)
	{
	   	inOrder(root->left);
		cout<<root->value<<" ";
		inOrder(root->right);	
	}
}

void preOrder(struct Node* root)
{
	if (root!=NULL)
	{
		cout<<root->value<<" ";
	   	preOrder(root->left);
		preOrder(root->right);	
	}
}

int main()
{
	struct Node* root = NULL;
	root = insert(root,50);
	root = insert(root,30);
	root = insert(root,70);
	root = insert(root,10);
	root = insert(root,40);
	
	root = insert(root,60);
	root = insert(root,80);
	preOrder(root);
	cout<<endl;
	postOrder(root);
	root = deleteNode(root,10);
	cout<<endl;
	inOrder(root);
	
	return 0;
}

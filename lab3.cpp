#include <iostream>
#include <new>

using namespace std;

class Node {
public:
    int data;
    Node *next;
    Node(int x, Node *n)
    {data=x;
    next=n;}
};
class Queue {
private:
    Node* front;
    Node* rear;
    int count;

public:
    Queue() : front(nullptr), rear(nullptr), count(0) {}

    void enqueue(int x) {
        Node* newNode = new Node(x, nullptr);
        if (rear == nullptr) {
            front = rear = newNode;
        } else {
            rear->next = newNode;
            rear = newNode;
        }
        count++;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return;
        }
        Node* temp = front;
        front = front->next;
        if (front == nullptr) {
            rear = nullptr;
        }
        delete temp;
        count--;
    }

    int top() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        return front->data;
    }

    bool isEmpty() {
        return front == nullptr;
    }

    int size() {
        return count;
    }
    void print(){
        for(Node *p=front; p!=nullptr; p=p->next){
                    cout<<p->data<<endl;
                };
    }
};
int main()
{
   /*do{
    cout<<"Enter a node value/Press enter -1 to exit: ";
    cin>>input;

    if(input !=-1){
        if(h==nullptr){
            h=new Node(input, nullptr);
            p=h;}
        else{
            p->next=new Node(input, nullptr);
            p=p->next;
        }
    }
   }
   while(input!=-1);*/

   Queue *q=new Queue();
    int choice, value;

do {

        cout << "\nWhich operation you want to take:" << endl;
        cout << "1. enqueue(int)" << endl;
        cout << "2. dequeue()" << endl;
        cout << "3. top()" << endl;
        cout << "4. isEmpty()" << endl;
        cout << "5. size()" << endl;
        cout << "6. print queue" << endl;
        cout << "-1. EXIT" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter the value to add: ";
                cin >> value;
                q->enqueue(value);
                break;
            case 2:
                q->dequeue();
                break;
            case 3:
                cout << "Top is: " << q->top() << endl;
                break;
            case 4:
                cout << "Queue " << (q->isEmpty() ? "empty" : "full") << endl;
                break;
            case 5:
                cout << "Queue size: " << q->size() << endl;
                break;
            case 6:
                q->print();
                break;
            case -1:
                cout << "Exit..." << endl;
                break;
            default:
                cout << "Invalid entry!" << endl;
        }
    } while (choice != -1);

    return 0;
}

#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;
    int num;
    int capacity;

public:
    Stack(int initialCapacity) {
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }


    void push(int x) {
        if (num == capacity - 1) {
            increaseCapacity();
        }
        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = head;
        head = newNode;
        num++;
        cout << x << " pushed to stack." << endl;
    }


    int pop() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        Node* temp = head;
        int poppedValue = temp->data;
        head = head->next;
        delete temp;
        num--;
        cout << poppedValue << " popped from stack." << endl;
        return poppedValue;
    }


    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return head->data;
    }


    bool isEmpty() {
        return num < 0;
    }


    void increaseCapacity() {
        capacity *= 2;
        cout << "Stack capacity increased to " << capacity << endl;
    }


    bool deleteElement(int val) {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return false;
        }
        Node* current = head;
        Node* previous = nullptr;
        while (current != nullptr) {
            if (current->data == val) {
                if (previous == nullptr) {

                    head = current->next;
                } else {

                    previous->next = current->next;
                }
                delete current;
                num--;
                cout << val << " deleted from stack." << endl;
                return true;
            }
            previous = current;
            current = current->next;
        }
        cout << "Element not found!" << endl;
        return false;
    }
    void showCurrentSize() {
        cout << "Current number of elements in the stack: " << num + 1 << endl;
    }
        void showCapacity() {
        cout << "Current stack capacity is: " << capacity << endl;
    }
};

int main() {
    Stack stack(3);

    int input;
    cout << "Enter numbers to push to the stack (-1 to stop): " << endl;

    while (true) {
        cin >> input;
        if (input == -1) break;
        stack.push(input);
    }

    int choice;
    do {
       cout << "\nSelect an operation:" << endl;
        cout << "1. Push an element" << endl;
        cout << "2. Pop an element" << endl;
        cout << "3. Peek the top element" << endl;
        cout << "4. Check if the stack is empty" << endl;
        cout << "5. Increase stack capacity" << endl;
        cout << "6. Delete an element" << endl;
        cout << "7. Show stack capacity" << endl;
        cout << "8. Show current size (number of elements)" << endl;
        cout << "0. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int value;
                cout << "Enter a value to push: ";
                cin >> value;
                stack.push(value);
                break;
            }
            case 2:
                stack.pop();
                break;
            case 3:
                cout << "Top element is: " << stack.peek() << endl;
                break;
            case 4:
                if (stack.isEmpty()) {
                    cout << "Stack is empty." << endl;
                } else {
                    cout << "Stack is not empty." << endl;
                }
                break;
            case 5:
                stack.increaseCapacity();
                break;
            case 6: {
                int value;
                cout << "Enter a value to delete: ";
                cin >> value;
                stack.deleteElement(value);
                break;
            }
            case 7:
                stack.showCapacity();
                break;
            case 8:
                stack.showCurrentSize();
                break;
            case 0:
                cout << "Exiting program." << endl;
                break;
            default:
                cout << "Invalid choice. Try again." << endl;
        }
    } while (choice != 0);

    return 0;
}

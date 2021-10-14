 #include<iostream>
 using namespace std;

 class student{
     public:
        string name;
        string major;
        double gpa;
        student(string aname, string amajor, double agpa){
            name =aname;
            major = amajor;
            gpa = agpa;
        }
        bool honras(){
            if(gpa >= 3.5) return true;
            return false;
        }
 };

 int main(){
     
     student student1("joao", "coisas", 2.5);
     student student2("paulo", "ota coisa", 3.6);

     cout << student1.honras() << endl;
     cout << student2.honras() << endl;
     
     return 0; 
}
#include<iostream>
using namespace std;

class movie{
    private:
        string rating;
    public:
        string title;
        string director;
        movie(string atitle, string adirector){
            title = atitle;
            director = adirector;
            setrating(rating);
        }
        void setrating(string arating){
            if(arating == "G" || arating == "PG" || arating == "PG-13" || arating == "R" || arating == "NR"){
                rating = arating;}
            else{
                rating = "NR";}  
        }
        string getrating(){
            return rating;
        }
};

int main(){

    movie vingador("Os vingadores", "John Cena");

    vingador.setrating("PG-13");

    cout << vingador.getrating() << endl;


    return 0;
}
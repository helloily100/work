#include <iostream>
#include <map>
using namespace;
public class Card {
    private:
        char suit;
        char value;
    public:
        Card( )// create a “default” card
        Card( char r, char s ){
            suit = r;
            value = s;
        }// constructor to create a card, setting the rank and suit 
        void setCard( char r, char s){
        suit = r;
        vlaue = s;
        } //set existing card to new values 
        int getValue( ){
            if (value == 'A'){
                return 0;
            }
            if (value == 'J' || 'Q' || 'K'){
                return 10;
            }
            return int(value);
        }// return the point value of the card. Ace = 1, 2 thru 10, Jack = 10, Queen = 10, King = 10 
        void display( ){

        }// display the card using 2 fields… Ace of Spade:AS, Ten of Diamond:10D, Queen of Heart:QH, Three of Club:3C. (If you want to get fancy, you can use these symbols for the suit ♠, ♣, ♥, ♦)
}

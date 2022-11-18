#include <iostream>
using namespace std;
public class Deck {
	private:
		int top;
	public:
		Deck( ){
		deck[52];
	} // constructor which creates a deck of 52 cards. Ace of Spades on top, followed by the rest of the spades in order, followed by Hearts, Diamonds and Clubs.
		void refreshDeck(); // reset the deck so it looks like a new deck.
		{
			deck[52]
		}
		Card deal( ) // deal a card from the top of the deck.
		{
			top++;
		}
		void shuffle( )// shuffle the cards in the deck.
		{

		}
		bool isEmpty( ) // true is deck is empty, false if the deck is not empty
		{
			if ( top == 52)[
				return true;
			] else {
				return false;
			}
		}
		void display( ); // show all the cards in the deck: 13 columns and 4 rows.
		{
			
		}
}
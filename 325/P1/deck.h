#ifndef DECK_H
#define DECK_H
using namespace std;
public class Deck {
	private:
		deck[];
	public:
		Deck( )// constructor which creates a deck of 52 cards. Ace of Spades on top, followed by the rest of the spades in order, followed by Hearts, Diamonds and Clubs.
		void refreshDeck(); // reset the deck so it looks like a new deck.
		Card deal( ) // deal a card from the top of the deck.
		void shuffle( ){} // shuffle the cards in the deck.
		bool isEmpty( ) // true is deck is empty, false if the deck is not empty
		void display( ); // show all the cards in the deck: 13 columns and 4 rows.
}

#endif
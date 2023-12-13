#include <ncurses.h>

int main()
{
	// init ncurses
	initscr();
	// initscr is called first, but other init functions my be called later:
	// - raw(): normally user input is stored in a buffer, and passed with enter, with raw() it is passed straight on
	// - noecho(): disable default user input echo
	// - keypad(stdscr, TRUE): enables read of arrow keys F* keys, etc

	printw("helloworld"); // ncurses-specific printf
	refresh(); // think of it as flush, dump etc
	getch();

	// stop ncurses
	endwin();
}

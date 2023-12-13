#include <ncurses.h>

int main()
{
	// The ncurses methods below all work on the "deafult" (stdscr) window.

	// If you want to specify the cursor position,
	// call the methods that have the 'mv' (move) prefix: mvprintw(y, x, string).
	// The cursor can be moved without also printing, with move(y, x).

	// If you created a new window and want to work with that,
	// call the methods that have the 'w' prefix: wprintw(window, string), wrefresh(window).

	// If you want to work on a specific window and move the cursor,
	// call the methods that have the 'mvw' prefix: mvwprintw(window, y, x, string).

	int ch;

	initscr();
	raw();
	keypad(stdscr, TRUE);
	noecho();

	printw("Type any character to see it in bold\n");

	// If raw() hadn't been called,
	// we have to press enter before it gets to the program
	ch = getch();

	// Without keypad enabled, this will not get to us either
	// Without noecho() an escape characters might have been printed
	if (ch == KEY_F(1))
	{
		printw("F1 Key pressed");
	}
	else
	{
		printw("The pressed key is ");
		attron(A_BOLD); // switching on bold attriubte
		printw("%c", ch);
		attroff(A_BOLD); // switching off bold attribute
		printw("\n");

		// When priting a character with addch()
		// an alternative way to attron() and attroff()
		// is to OR the attribute with the char.
	}
	refresh();

	getch();
	endwin();
	return 0;
}
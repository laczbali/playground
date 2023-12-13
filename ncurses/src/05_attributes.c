#include <ncurses.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    /*
    Attirbute list:
        A_NORMAL        Normal display (no highlight)
        A_STANDOUT      Best highlighting mode of the terminal.
        A_UNDERLINE     Underlining
        A_REVERSE       Reverse video
        A_BLINK         Blinking
        A_DIM           Half bright
        A_BOLD          Extra bright or bold
        A_PROTECT       Protected mode
        A_INVIS         Invisible or blank mode
        A_ALTCHARSET    Alternate character set
        A_CHARTEXT      Bit-mask to extract a character
        COLOR_PAIR(n)   Color-pair number n

    If you want to use more than one attribute at a time,
    use the OR operator (|) to combine them: attron(A_BOLD | A_UNDERLINE)

    attron() and attroff() are used to switch the specified attributes on and off.
    attrset() is used to set the attributes, overriding the current options.
    attr_get() is used to get the current attributes.
    The attr methods also have variants with the 'w' prefix.

    chgat() can be used to change the attributes of a given number of characters,
    starting at the current cursor position.
    */

    int ch, prev, row, col;
    prev = EOF;
    FILE *fp;
    int y, x;

    if (argc != 2)
    {
        printf("Usage: %s <a c file name>\n", argv[0]);
        exit(1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        perror("Cannot open input file");
        exit(1);
    }
    initscr();
    getmaxyx(stdscr, row, col);

    // read the file till we reach the end
    while ((ch = fgetc(fp)) != EOF)
    {
        getyx(stdscr, y, x); // get the current curser position
        if (y == (row - 1))  // are we are at the end of the screen
        {
            printw("<-Press Any Key->"); // tell the user to press a key
            getch();
            clear();    // clear the screen
            move(0, 0); // start at the beginning of the screen
        }
        if (prev == '/' && ch == '*') // If it is / and * then only switch bold on
        {
            attron(A_STANDOUT);      // turn bold on
            getyx(stdscr, y, x);     // get the current curser position
            move(y, x - 1);          // back up one space
            printw("%c%c", '/', ch); // The actual printing is done here
        }
        else
        {
            printw("%c", ch);
        }

        refresh();
        if (prev == '*' && ch == '/')
        {
            attroff(A_STANDOUT); // Switch it off once we got * and then /
        }
        prev = ch;
    }

    getch();
    endwin();
    fclose(fp);
    return 0;
}
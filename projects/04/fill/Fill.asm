// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(BEGIN)
    @SCREEN
    D=A

    @PIXEL_POSITION
    M=D

    @KBD
    D=M

    @WHITE
    D; JEQ

    @BLACK
    0; JMP

(BLACK)
    @KBD_INPUT
    M=-1

    @LOOP
    0; JMP

(WHITE)
    @KBD_INPUT
    M=0

    @LOOP
    0; JMP

(LOOP)
    @KBD_INPUT
    D=M

    @PIXEL_POSITION
    A=M
    M=D

    @PIXEL_POSITION
    M=M+1
    D=M

    @KBD
    D=D-A

    @BEGIN
    D; JEQ

    @LOOP
    0; JMP

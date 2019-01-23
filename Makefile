getc:
	gcc doot.c -o getc

run: getc
	./getc

all: getc

clean:
	rm getc

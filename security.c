#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int main() {
	FILE *f;
	char *buf;
	size_t fsize;
	char s[32];
	char *lines[512];
	size_t i;
	char *j, **k, *firstcol, *test, *lastcol, *res;

	if(getuid() != 0) {
		fprintf(stderr, "must be run as root\n");
		return 1;
	}

	f = fopen("/etc/shadow", "r");
	if(!f) f = fopen("/etc/passwd", "r");
	fseek(f, 0, SEEK_END);
	fsize = ftell(f);
	rewind(f);

	buf = malloc(fsize * sizeof(char));
	fread(buf, sizeof(char), fsize, f);
	
	i = 0;
	lines[i++] = buf;
	for(j = buf; (j - buf) < fsize; j++)
		if(*j == '\n')
			lines[i++] = j + 1;
	lines[i] = NULL;

	printf("Enter a password: ");
	gets(s);

	for(k = lines; *k; k++) {
		firstcol = strchr(*k, ':');
		if(!firstcol) continue;
		lastcol = strchr(firstcol + 1, ':');
		if(!lastcol) continue;
		*lastcol = 0;
		test = strrchr(firstcol, '$');
		if(!test) continue;
		*test++ = 0;
		firstcol = strchr(firstcol, '$');
		res = crypt(s, firstcol);
		// printf("salt: %s\nresult: %s\ntest: %s\n", firstcol, res, test);
		*(test - 1) = '$';
		if(!strcmp(crypt(s, strchr(firstcol, '$')), firstcol)) {
			printf("password matches some user\n");
			return 0;
		}
	}

	printf("password does not match any user\n");
	return 1;
}

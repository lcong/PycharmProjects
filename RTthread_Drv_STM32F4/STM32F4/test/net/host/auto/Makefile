CC = gcc
OBJS = %.o
INCPATH = -I. -I../../include
CFLAGS = -Wall -g
OBJS = $(subst .c,.o,$(wildcard *.c))
RM = rm -f

all:
	@echo Use \"make win32\" or \"make linux\" instead.

win32:
	$(MAKE) target\
		BIN="runcase.exe"\
		LIBS="-lwsock32 -lnetapi32"

linux:
	$(MAKE) target\
		BIN="runcase"\
		LIBS="-lpthread"

target: $(BIN)

$(BIN):$(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS) $(LIBS)

%.o:%.c
	$(CC) $(INCPATH) $(CFLAGS) -c $<

clean:
	$(RM) *.o


.PHONY: all clean

all: clean
	pyinstaller clipps.py --add-binary copyicon.gif:copyicon.gif

run:
	./dist/clipps/clipps

clean:
	mkdir -p ./dist ./build
	touch clipps.spec
	rm -r ./dist ./build clipps.spec
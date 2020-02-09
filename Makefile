.PHONY: all clean dev run

all: clean
	mkdir -p ~/.clipps
	cp copyicon.gif ~/.clipps/copyicon.gif
	pip install -r requirements.txt
	pyinstaller clipps.py --onefile --windowed --icon=copyicon.gif

dev:
	pyinstaller clipps.py --onefile --windowed

run:
	./dist/clipps/clipps

clean:
	mkdir -p ./dist ./build
	touch clipps.spec
	rm -r ./dist ./build clipps.spec
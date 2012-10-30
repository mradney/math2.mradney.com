build: clean
	liquidluck build
clean:
	-rm -r output
deploy:
	liquidluck build
	ghp-import output
	git push origin gh-pages
view: clean
	liquidluck server

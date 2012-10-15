build:
	rm -r output
	liquidluck build
deploy:
	liquidluck build
	ghp-import output
	git push origin gh-pages
preview:
	rm -r output
	liquidluck server

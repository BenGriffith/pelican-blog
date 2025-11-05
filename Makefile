github:
	pelican content -o output -s publishconf.py
	ghp-import output -b gh-pages -n 
	git push origin gh-pages --force
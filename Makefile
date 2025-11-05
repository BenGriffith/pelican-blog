github:
	python -m pelican content -o output -s publishconf.py
	ghp-import output -b gh-pages -n -c bengriffith.dev
	git push origin gh-pages --force

rebuild:
	python -m pelican content -o output -s publishconf.py
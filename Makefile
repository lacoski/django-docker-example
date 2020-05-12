freeze:
	pip freeze | grep -v "pkg-resources" > requirements/dev.txt

freeze-docker:
	pip freeze | grep -v "pkg-resources" > requirements/docker.txt

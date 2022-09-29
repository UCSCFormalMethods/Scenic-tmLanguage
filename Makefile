.PHONY: all ci-test test release devenv publish

all: devenv release

ci-test: release
#	Run tests
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/src/Scenic.syntax.yaml

# 	Check if the version specified in "package.json" matches the latest git tag
	@if [ \
		`cat package.json | grep -e '^[[:space:]]*"version":' | sed -e 's/[[:space:]]*"version":[[:space:]]*"\(.*\)",/\1/'` \
		!= \
		`git describe --tags --abbrev=0 | sed -e 's/v\([[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\).*/\1/'` \
	] ; \
		then echo "Error: package.version != git.tag" && exit 1 ; fi

update-test:
#	Run tests and overwrite the output
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/src/Scenic.syntax.yaml --overwrite-tests

test: ci-test
	atom -t test/atom-spec

devenv:
	npm install --dev

release:
	./node_modules/.bin/syntaxdev build-plist --in grammars/src/Scenic.syntax.yaml --out grammars/Scenic.tmLanguage

	./node_modules/.bin/syntaxdev build-cson --in grammars/src/Scenic.syntax.yaml --out grammars/Scenic.cson

	./node_modules/.bin/syntaxdev scopes --syntax grammars/src/Scenic.syntax.yaml > misc/scopes

	./node_modules/.bin/syntaxdev atom-spec --package-name Scenic --tests test/**/*.py --syntax grammars/src/Scenic.syntax.yaml --out test/atom-spec/scenic-spec.js

publish: test
	apm publish patch
	rm -rf ./node_modules/syntaxdev
	vsce publish

ALFRED_WORKFLOW_PATH ?= ~/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows
BUNDLE_ID = io.uechi.alfred-workflow-ghq
PACKAGE_FILE = info.plist
SYMLINK_TARGET = ${ALFRED_WORKFLOW_PATH}/${BUNDLE_ID}
WORKFLOW_NAME = ghq

default: package

package:
	rm -f ${WORKFLOW_NAME}.alfredworkflow
	cd workflow; zip -r ../${WORKFLOW_NAME}.zip *
	mv ${WORKFLOW_NAME}.zip ${WORKFLOW_NAME}.alfredworkflow

link:
	ln -sf "$(PWD)/workflow" "${SYMLINK_TARGET}"

unlink:
	rm "${SYMLINK_TARGET}"

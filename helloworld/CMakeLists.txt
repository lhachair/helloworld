

# Add target to project dependency list
PROJECT_TARGET_ADD(helloworld)
	# Define project Targets
	ADD_LIBRARY(${TARGET_NAME} MODULE helloworld.c)

	# Binder exposes a unique public entry point
	SET_TARGET_PROPERTIES(${TARGET_NAME} PROPERTIES
	PREFIX "afb-"
		LABELS "BINDING"
		OUTPUT_NAME ${TARGET_NAME}
	)


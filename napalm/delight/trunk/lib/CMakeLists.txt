CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

#set(ilmbase_COMPONENTS Imath Half)
#set(boost_COMPONENTS serialization)

drd_find_packages(PREFIX pkgs AUTO)

INCLUDE_DIRECTORIES(.)

FILE(GLOB_RECURSE cpp_files "*.cpp")
ADD_LIBRARY ( napalmDelight STATIC ${cpp_files} )
TARGET_LINK_LIBRARIES(napalmDelight ${pkgs_LIBRARIES})
INSTALL ( TARGETS napalmDelight DESTINATION lib )

# install the headers
FILE(GLOB_RECURSE h_files "*.h")
drd_install_files( ${h_files} DESTINATION include )

drd_install_cmake(
	DESTINATION 	cmake
	INCLUDE_DIRS	include 		${pkgs_INCLUDE_DIRS}
	LIBRARY_DIRS 	lib 			${pkgs_LIBRARY_DIRS}
	LIBRARIES		napalmDelight 	${pkgs_LIBRARIES}
	DEFINITIONS						${pkgs_DEFINITIONS}
)

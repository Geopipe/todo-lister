#!/usr/bin/env python
# See README.md
# Copyright (c) 2017 Geopipe, Inc.

import sys, os
import clang.cindex
import argparse

def find_comments(node):
	if node.kind.is_declaration():
		print("Statement at %s:%s:%s" % \
			(node.location.file, node.location.line, node.location.column))
		if None != node.brief_comment:
			print node.brief_comment

	# Recurse for children of this node
	for c in node.get_children():
		find_comments(c)

def main():
	index = clang.cindex.Index.create()
	tu = index.parse(sys.argv[1])
	print 'Translation unit:', tu.spelling
	find_comments(tu.cursor)

if __name__ == "__main__":
	main()

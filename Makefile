# Makefile for source rpm: fedora-logos
# $Id$
NAME := fedora-logos
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
